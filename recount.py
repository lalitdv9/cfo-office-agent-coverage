#!/usr/bin/env python3
"""
recount.py — regenerate every number reported in the paper from the released
artifacts, and fail loudly if the paper and the data disagree.

Run from the repository root:

    python3 recount.py

It reads coverage_matrix.csv, governance_scorecard.csv, included_papers.csv and
screening.csv, prints every count the paper reports, and checks each against the
value asserted in the manuscript. Any mismatch is an error, not a warning: the
point of this script is that the paper and the artifact cannot drift apart.
"""

import csv
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DIMS = ("PROV", "SOD", "TIE", "REP")

# Values asserted in the manuscript. Update here and in the .tex together.
ASSERTED = {
    "screened": 120,
    "corpus": 60,
    "eligible": 38,
    "scored": 32,
    "pending": 6,
    "core": 17,
    "other": 15,
    "cells": 82,
    "core_none": 4,
    "all_none": 10,
    "kappa_agree": 23,
    "kappa_n": 24,
}


def rows(name, sub=""):
    path = os.path.join(HERE, sub, name) if sub else os.path.join(HERE, name)
    if not os.path.exists(path):
        sys.exit("missing artifact: %s" % path)
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def leaf_columns(header):
    return [c for c in header if c and c[0].isdigit() and "." in c]


def main():
    screening = rows("screening.csv")
    corpus = rows("included_papers.csv")
    matrix = rows("coverage_matrix.csv")
    gov = rows("governance_scorecard.csv")

    scored = [r for r in matrix if "PENDING" not in r["band"]]
    pending = [r for r in matrix if "PENDING" in r["band"]]
    leaves = leaf_columns(matrix[0].keys())

    cells = sum(1 for r in scored for c in leaves if (r[c] or "").strip())
    core = [r for r in gov if r["band"].strip() == "core"]
    other = [r for r in gov if r["band"].strip() != "core"]

    def tally(rs):
        out = {}
        for d in DIMS:
            c = Counter((r[d] or "").strip().upper() for r in rs)
            out[d] = (c.get("Y", 0), c.get("P", 0))
        none = sum(
            1 for r in rs
            if not any((r[d] or "").strip().upper() in ("Y", "P") for d in DIMS)
        )
        return out, none

    core_t, core_none = tally(core)
    all_t, all_none = tally(gov)

    # PRISMA screening reconciliation, checked (not just reported): of 120
    # screened, 46 were straight yes/13 pending-that-entered-corpus give the
    # 59 search-derived corpus rows, plus 1 identified outside the search =
    # 60-item corpus; 48 remain genuinely unresolved.
    resolution = [r.get("resolution", "") for r in screening]
    n_unresolved = sum(1 for x in resolution if x == "unresolved:no-decision-at-cutoff")
    n_resolved_into_corpus = sum(1 for x in resolution if x == "resolved:entered-corpus")
    n_yes = sum(1 for r in screening if (r.get("final_include") or "").strip() == "yes")
    n_search_derived = n_yes + n_resolved_into_corpus
    n_outside_search = len(corpus) - n_search_derived

    got = {
        "screened": len(screening),
        "corpus": len(corpus),
        "eligible": len(matrix),
        "scored": len(scored),
        "pending": len(pending),
        "core": len(core),
        "other": len(other),
        "cells": cells,
        "core_none": core_none,
        "all_none": all_none,
        "prisma_unresolved": n_unresolved,
        "prisma_resolved_into_corpus": n_resolved_into_corpus,
        "prisma_search_derived_corpus": n_search_derived,
        "prisma_outside_search": n_outside_search,
    }
    ASSERTED.update({
        "prisma_unresolved": 48,
        "prisma_resolved_into_corpus": 13,
        "prisma_search_derived_corpus": 59,
        "prisma_outside_search": 1,
    })

    # Inter-coder agreement, recomputed rather than quoted.
    try:
        a = {(r["bibkey"], r["leaf"]): r["committed_code"].strip().lower()
             for r in rows("intercoder_sample.csv")}
        b = {(r["bibkey"], r["leaf"]): r["my_code"].strip().lower()
             for r in rows("intercoder_recode.csv")}
        keys = sorted(set(a) & set(b))
        agree = sum(1 for k in keys if a[k] == b[k])
        n = len(keys)
        cats = sorted(set(list(a[k] for k in keys) + list(b[k] for k in keys)))
        po = agree / n
        pe = sum((sum(1 for k in keys if a[k] == c) / n) *
                 (sum(1 for k in keys if b[k] == c) / n) for c in cats)
        kappa = (po - pe) / (1 - pe)
        got["kappa_agree"], got["kappa_n"] = agree, n
    except SystemExit:
        kappa = None

    print("=" * 62)
    print("COUNTS  (artifact vs. manuscript)")
    print("=" * 62)
    bad = []
    for k, v in got.items():
        exp = ASSERTED.get(k)
        ok = exp is None or v == exp
        if not ok:
            bad.append((k, v, exp))
        print("  %-12s %6s   %s" % (k, v, "ok" if ok else "MISMATCH (paper: %s)" % exp))

    print("\nGOVERNANCE TALLIES  (Y/P)")
    print("  core  (n=%d): %s; measure none: %d"
          % (len(core), "; ".join("%s %d/%d" % (d, *core_t[d]) for d in DIMS), core_none))
    print("  all   (n=%d): %s; measure none: %d"
          % (len(gov), "; ".join("%s %d/%d" % (d, *all_t[d]) for d in DIMS), all_none))

    if kappa is not None:
        print("\nINTER-CODER: %d/%d exact agreement, Cohen's kappa = %.4f"
              % (got["kappa_agree"], got["kappa_n"], kappa))

    # Leaf coverage, for the taxonomy figure shading.
    full, partial = [], []
    for c in leaves:
        vals = {(r[c] or "").strip().upper() for r in scored if (r[c] or "").strip()}
        if "F" in vals:
            full.append(c)
        elif vals:
            partial.append(c)
    empty = [c for c in leaves if c not in full and c not in partial]
    print("\nLEAF COVERAGE (%d leaves)" % len(leaves))
    print("  full (%d):    %s" % (len(full), ", ".join(full)))
    print("  partial (%d): %s" % (len(partial), ", ".join(partial)))
    print("  EMPTY (%d):   %s" % (len(empty), ", ".join(empty)))

    # Source-quality flags live in included_papers.csv, not the matrix.
    flags = Counter((r.get("verification") or "").strip() for r in corpus)
    print("\nSOURCE-QUALITY FLAGS (included_papers.csv)")
    for k, v in sorted(flags.items()):
        if k:
            print("  %-28s %d" % (k, v))

    if bad:
        print("\n%d MISMATCH(ES) between artifact and manuscript:" % len(bad))
        for k, v, exp in bad:
            print("  %s: artifact=%s paper=%s" % (k, v, exp))
        sys.exit(1)
    print("\nAll reported counts reproduce from the released artifacts.")


if __name__ == "__main__":
    main()
