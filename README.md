# The Office of the CFO as a Distinct, Under-Benchmarked Domain for AI Agents

Released artifacts for the paper *Capability Is Not
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
| `protocol.md` | Registered protocol (§11 documents the coding procedure and what the re-code check does and does not show): research questions, databases, time window (Jan 2023 – 16 Jul 2026), inclusion/exclusion criteria, and the logged search deviations |
| `search_log.csv` | Every query run |
| `screening.csv` | All 120 title/abstract records with decisions and exclusion codes. `final_include` is the final decision (`yes`/`no`/`pending`); the `resolution` column records provenance for rows that were pending at the title/abstract cutoff. 13 of them, marked `resolved:entered-corpus`, were later read and admitted, so they carry `final_include=yes` with `resolution` retained as the provenance flag; 48 remain `unresolved:no-decision-at-cutoff` (`final_include=pending`). This gives 59 search-derived corpus records (46 straight `yes` + 13 later admissions); a 60th was identified outside the systematic search. |
| `included_papers.csv` | The 60-item corpus, with per-row source-quality flags (`preprint`, `verification`) |
| `pending_48_resolution.csv` | Post-cutoff decision for each of the 48 records unresolved at the 16 July 2026 cutoff: decision, leaves touched, effect on the eight empty leaves, evidence grade (title + screening note, abstract, full text, or public task prompts) and reason. AI-coded and not yet ratified by a human; it does not change any count at the cutoff. `recount.py` checks its totals (39 cleared, 9 not ruled out). |
| `notes/` | Per-paper evidence notes; each reported number traces to an exact quotation with its section |
| `coverage_matrix.csv` | Leaf-level coverage: 38 eligible rows (32 scored, 6 pending) × 34 leaves |
| `governance_scorecard.csv` | Provenance / segregation-of-duties / tie-out / repetition coding, with per-row justification |
| `reliability_synthesis.csv` | The basic-versus-composed pairs behind the reliability table. `include_in_table` marks which rows appear in the paper's Table 2 |
| `reliability_synthesis_README.md` | Which 5 of the 7 candidate rows appear in Table 2, and why the other 2 are excluded |
| `intercoder_sample.csv`, `intercoder_recode.csv` | The 24-cell dual-coding sample and the blind re-code |
| `cfo_task_tree.md` | The task taxonomy with the one-line operational definition fixed for each leaf before scoring |
| `build_extra_tables.py` | Rebuilds the governance and reliability LaTeX tables; runs end-to-end from this repo |
| `build_matrix.py` | Provenance code showing how `coverage_matrix.csv` was assembled. Not independently executable -- its second input was a working-directory scratch file never included in this release. See the note at the top of the file. |
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

Every negative claim is dated ("as of July 2026") rather than asserted as
permanent.

## License

Artifacts are released under CC BY 4.0. The analyzed works remain under their own
licenses; evidence notes quote source text only to the extent needed to justify a
coding decision.
