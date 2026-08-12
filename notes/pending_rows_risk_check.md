# Empty-leaf risk check on the 6 pending rows

Assessment level: title + `ta_reason` field from screening.csv, checked against
the keyword vocabulary of the paper's 8 empty leaves. NOT a full-text read.
These rows remain pending and unscored in coverage_matrix.csv and
governance_scorecard.csv; nothing here changes that status.

## Empty-leaf keyword vocabulary used
2.7 cost/profitability: cost|profitab|margin|unit econ
3.2 FX/rate risk:       fx|foreign exch|interest.rate|hedg
3.4 working capital:    working capital|receivable|payable|dso|dpo|inventor
4.1 tax provision:      provision|asc 740|deferred tax|effective tax
4.3 transfer pricing:   transfer pricing|intercompany pric
5.1 earnings release:   earnings call|earnings release|guidance|investor relation
5.3 shareholder engmt:  shareholder|proxy|activist
6.3 synergies/PMI:      merger|acquisit|synerg|integration|pmi|due dilig

## The 6 rows, and where they'd plausibly land if scored

| bibkey | title | plausible leaf(s) | empty-leaf match? |
|---|---|---|---|
| acctreasoning2025 | Accounting Reasoning in LLMs | 1.1 / 1.5 | no |
| finrulebench2026 | FinRule-Bench: Joint Reasoning over Financial Tables and Principles | 1.5 | no |
| finverbench2026 | FinVerBench: Benchmark Validity and Calibration in LLM Financial Statement Verification | 1.5 / 1.7 | no |
| xbrlagent2024 | XBRL Agent: LLMs for Financial Report Analysis | 1.7 | no |
| xbrltagrec2026 | XBRLTagRec: Extreme Financial Numeral Labeling | 1.7 | no |
| lava2025 | LAVA: Logic-Aware Validation and Augmentation for Financial Document Auditing | 1.6 / audit band | no |

## Result
All 6 cluster around leaves 1.1 (journal entries), 1.5 (technical accounting),
1.6 (internal controls / SOX), and 1.7 (statutory reporting / XBRL) —
every one of which is already non-empty in the scored matrix (leaves 1.1, 1.7
are FULL; 1.5, 1.6 are PARTIAL). None of the 6 matches the keyword vocabulary
of any of the 8 empty leaves.

This does not promote these rows to scored, and does not make the "none of the
6 addresses an empty leaf" claim a full-text finding. It converts an
unverified assertion into a title-level check with a documented method,
consistent with how forcebench2026 was assessed (notes/2607_19409.md).

## Why they are pending rather than excluded or scored
5 of 6 carried a firm include_ta=yes at title/abstract screening, on par with
the 32 rows that were fully scored (25/32 scored rows also carried yes).
Exclusion did not apply because none looked off-topic. 4 of the 6 entered via
the direct arXiv sweep (2026-07-16); 2 (xbrlagent2024, lava2025) entered via
reference snowballing off an already-included row, which by construction runs
last in any search protocol. All 6 are the last candidates admitted before the
registered 16 July 2026 cutoff; the full-text reading pass did not reach them
in time. This is an arrival-order artifact of a time-boxed protocol, not a
quality judgment against these 6 specifically.
