# reliability_synthesis.csv -- how its 7 rows map to the paper

7 candidate rows. The `include_in_table` column is authoritative and machine-
checkable: **5 rows appear in Table 2** (`include_in_table=yes`), **2 are
excluded** (`include_in_table=no`), each for a stated reason.

In Table 2: `cfagentbench2026`, `finmaster2025`, `finmaster2025b`,
`finbalance2026`, `workstreambench2026` (cited in the paper as MBABench, its
current title -- the benchmark was renamed between arXiv versions; see
`custom.bib`).

Excluded from Table 2:

| bibkey | why excluded |
|---|---|
| `bigfinancebench2026` | Its rubric-versus-answer comparison is two different metrics, not a reference/degraded pair on the same metric. |
| `enterprisearena2026` | Its comparison point (survival to a 132-month horizon) is a ceiling on a single long-horizon task, not a single-step reference score with a comparable degraded score. Discussed in the paper's prose (Sec. 5.1), not tabulated. |

`build_extra_tables.py` reads `include_in_table` directly and only emits rows
marked `yes`, so the generated table and this file cannot drift apart from
each other. Whether that generated table matches the exact wording and number
formatting of the paper's typeset Table 2 is not separately checked here --
compare `reliability_table.tex` against the paper by eye if that matters for
your purposes.
