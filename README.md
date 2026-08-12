# The Office of the CFO as a Distinct, Under-Benchmarked Domain for AI Agents

Released artifacts for the FinNLP 2026 submission *Capability Is Not
Deployability: The Office of the CFO as a Distinct, Under-Benchmarked Domain for
AI Agents*. Anonymous for review.

Every count reported in the paper is derived from the files here. To check that
the paper and this repository agree:

```
python3 recount.py
```

The script recomputes the corpus counts, the justified-cell count, the
governance tallies, the inter-coder agreement and Cohen's kappa, and the
full/partial/empty status of all 34 taxonomy leaves. It exits non-zero if any
number disagrees with the manuscript.

## Contents

| File | What it is |
|---|---|
| `protocol.md` | Registered protocol: research questions, databases, time window (Jan 2023 – Aug 2026), inclusion/exclusion criteria, and the logged search deviations |
| `search_log.csv` | Every query run |
| `screening.csv` | All 120 title/abstract records with decisions and exclusion codes |
| `included_papers.csv` | The 60-item corpus, with per-row source-quality flags (`preprint`, `verification`) |
| `notes/` | Per-paper evidence notes; each reported number traces to an exact quotation with its section |
| `coverage_matrix.csv` | Leaf-level coverage: 38 eligible rows (32 scored, 6 pending) × 34 leaves |
| `governance_scorecard.csv` | Provenance / segregation-of-duties / tie-out / repetition coding, with per-row justification |
| `reliability_synthesis.csv` | The basic-versus-composed pairs behind the reliability table |
| `intercoder_sample.csv`, `intercoder_recode.csv` | The 24-cell dual-coding sample and the blind re-code |
| `cfo_task_tree.md` | The task taxonomy with the one-line operational definition fixed for each leaf before scoring |
| `build_matrix.py`, `build_extra_tables.py` | Scripts that rebuild the paper's tables |
| `recount.py` | Verification script described above |

## Coding vocabulary

Coverage cells: `F` end-to-end, `P` partial, blank none.
Governance cells: `Y` measured, `P` partial or indirect, `N` not measured.

Rows whose band is marked `PENDING-FULLTEXT` are excluded from every count in
the paper.

## Correcting this map

The paper's gap claims are falsifiable by construction. If a benchmark we mark
absent exists, it can be added as a row and the counts regenerated. Because
removal is monotone with respect to empty cells, excluding rows can never create
a gap we report — only adding rows can close one.

Every negative claim is dated ("as of August 2026") rather than asserted as
permanent.

## License

Artifacts are released under CC BY 4.0. The analyzed works remain under their own
licenses; evidence notes quote source text only to the extent needed to justify a
coding decision.
