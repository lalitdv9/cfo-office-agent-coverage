# reliability_synthesis.csv -- how its 7 rows map to the paper

7 candidate rows. **4 appear in Table 2** (composition/repetition degradation
pairs): `cfagentbench2026`, `finmaster2025`, `finmaster2025b`,
`workstreambench2026` (cited in the paper as MBABench, its current title --
the benchmark was renamed between arXiv versions; see `custom.bib`).

**3 are deliberately excluded from Table 2**, each for a stated reason:

| bibkey | why excluded from Table 2 | where it appears instead |
|---|---|---|
| `finbalance2026` | Construct mismatch: it measures self-report-versus-replay divergence on a single attempt, not the same task made harder. Table 2 is specifically about composition/repetition degradation. | Governance section (Sec. 6), as the paper's central provenance finding: a 52% wrong-document rate and a 26--41pp self-report/replay gap. |
| `bigfinancebench2026` | Its rubric-versus-answer comparison is two different metrics, not a reference/degraded pair on the same metric. | Not tabulated; mentioned as excluded in the Table 2 caption. |
| `enterprisearena2026` | Its comparison point (survival to a 132-month horizon) is a ceiling on a single long-horizon task, not a single-step reference score with a comparable degraded score. | Discussed in prose (Sec. 5.1) alongside Table 2, not inside it. |

This file is the raw candidate set `build_extra_tables.py` draws from; the
exclusions above are a judgment applied when writing the paper, not a property
the CSV encodes on its own. `recount.py` does not currently check the 7-vs-4
split -- verify it by reading this table against the paper's Table 2 directly.
