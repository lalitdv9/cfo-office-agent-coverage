# WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

> NOTE (2026-07-16): file renamed from mbabench2026.md — verified paper name is WorkstreamBench; "MBABench" appears nowhere in the paper.

- arXiv ID: 2605.22664
- Authors: Thomson Yen (1), Julian Poeltl (2), Harshith Srinivas Gear (1), Yilin Meng (1), Joshua Fan (1), Adam Shen (1), Yili Liu (1), Ali Bauyrzhan (1), Siri Du (1), Haoyang Liu (1), Daniel Guetta (1), Hongseok Namkoong (1). Affiliations: (1) Decision, Risk, and Operations Division, Columbia Business School; (2) ESB Business School, Reutlingen University.
- Status: full-text fetched: Y (https://arxiv.org/html/2605.22664v1, full HTML body incl. Sections 1-8 and appendix TOC; figures are images and not readable as text)

## NAMING VERIFICATION (requested check)
The paper's name is **WorkstreamBench** throughout (title, section headings, running text). The string "MBABench" appears **nowhere** in the fetched full text (case-insensitive grep: 0 matches). The only MBA-related sentence is about annotator effort: "In total, 2 MBAs and 3 finance professionals spent 700+ hours." (Section 5). Any citation of this paper as "MBABench" is not supported by the fetched source.

## Summary
WorkstreamBench evaluates LLM agents on constructing complete, multi-sheet financial Excel workbooks end-to-end from high-level instructions, rather than the atomic edit/QA tasks of prior spreadsheet benchmarks. Tasks are curated from the Financial Modeling World Cup (FMWC), ModelOff, and the Wall Street Prep training curriculum, and are manually annotated by type (3-statement modeling, DCF, etc.) and difficulty (levels 1-5). Because deliverable quality in finance is multi-dimensional, the authors define a taxonomy of Accuracy, Formula, and Format criteria with fine-grained sub-dimensions (e.g., avoid hardcoding, logic readability), scored by an LLM judge whose verdicts were validated against expert annotations. They evaluate both proprietary GUI agents (Claude Web, Claude for Excel, ChatGPT for Excel, ChatGPT Agent/Pro) collected via a Playwright pipeline and API agents run in an in-house harness. Claude Web is the strongest agent overall at 69.1/100, and all agents degrade sharply as task difficulty increases. The authors conclude that current agents cannot yet reliably produce professional-quality financial spreadsheets.

## Tasks covered
End-to-end financial spreadsheet construction: 3-statement modeling, DCF valuation, forecasting, scenario analysis, trading-simulation style modeling; sources FMWC, ModelOff, WSP; difficulty levels 1-5 (level 5 has only 7 tasks per Figure 6 caption). An exact total task count is not stated in the fetched text.

## Eval method
Rubric + LLM-as-judge (pass/fail per sub-dimension criterion, weighted into a 0-100 composite). Explicitly departs from exact-match evaluation. Judge validated on synthetic perturbations and real agent attempts against expert labels.

## Data realism
Real professional/competition materials (FMWC, ModelOff, Wall Street Prep) "designed to reflect real workplace expectations" (Section 4). Not synthetic, not templated; not live company documents either — competition/training tasks.

## Agent scope
Single-agent, multi-step end-to-end artifact construction (full workbook deliverables). Two agent classes: GUI product agents (proprietary harnesses) and API agents (common in-house agentic framework).

## Key numbers (exact quotes)
- Best score ~69/100 CONFIRMED (69.1): "Even the strongest agent, Claude Web, attains only 69.1 out of 100 overall, and experiences notable performance drop as task difficulty increases (53.4/100 at difficulty level 4)." (Section 6, Benchmark Results paragraph)
- Judge validity: "on grading agent attempts, the judge achieves a 0.92 accuracy, 0.88 balanced accuracy, and 0.85 F1 score when measured against 408 expert annotations." (Section 5)
- Annotation effort: "In total, 2 MBAs and 3 finance professionals spent 700+ hours." (Section 5)
- Task scarcity at top difficulty: "the larger standard error at level 5 task difficulty stems from a low number of tasks (7)." (Figure 6 caption, Section 6)

## Relevance to CFO-office taxonomy
FP&A / financial-modeling deliverable production: the spreadsheet-artifact slice of CFO-office work (modeling, forecasting, scenario analysis), with evaluation criteria mirroring how finance teams review deliverables (auditability, readability, modifiability).

## UNVERIFIED items
- Exact total number of benchmark tasks (not stated anywhere in fetched text; only per-difficulty distribution shown in Figure 4 image).
- Per-agent composite scores other than Claude Web 69.1 (reported only in Figure 2 image).
- The alternate name "MBABench" — NOT FOUND in the paper; treat as an incorrect claim.
