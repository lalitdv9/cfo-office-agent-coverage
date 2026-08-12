# finch2025 — FINCH: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows

- **Title:** FINCH: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows
- **arXiv ID:** 2512.13168 (fetched https://arxiv.org/html/2512.13168v1, full text)
- **Authors:** "FINCH members" ([email removed]); Appendix A full list: Haoyu Dong (Univ. of Chinese Academy of Sciences, corresponding), Pengkun Zhang (SCUT), Yan Gao (Zhongguancun Academy), Xuanyu Dong (Harvest Fund), Yilin Cheng (Fudan/Zhongguancun), Mingzhe Lu (UCAS), Adina Yakefu (Hugging Face), Shuxin Zheng (Zhongguancun Academy)
- **Status:** fulltext read (HTML v1, body + appendices A–E)

## Summary
Benchmark of 172 composite, enterprise-grade finance & accounting (F&A) workflows (384 tasks) over 1,710 spreadsheets (27M cells) plus PDFs/Word/images, sourced from authentic enterprise workspaces — primarily Enron (~15,000 spreadsheets, 500,000 emails, 150 employees) and EUSES, plus securities/asset-management firms, World Bank, Canadian and British governments. Workflows are induced from real email threads and spreadsheet version histories via LLM-assisted discovery + expert annotation (700+ expert hours). Frontier product agents (ChatGPT 5.1 Pro, Claude Sonnet 4.5) and 5 API models are evaluated; best system passes 38.4% of workflows (human eval).

## Tasks
- Task types (per Sec 2.2): Calculation (119 workflows), Structuring/Formatting (86), Data Entry/Import (44), Validation/Review (37; "checking consistency and reconciling calculations within a sheet or across sheets/files"), Cross-sheet/file Retrieval (36), Summary/Visualization (33), Financial Modeling (15; "extending or calibrating valuation and timing models, often via scenario and sensitivity analysis"), Web Search (11), Translation (3).
- Business types (Sec 2.2): reporting (48), trading and risk management (35), operational management (36), predictive modeling (33), planning and budgeting (26), pricing and budgeting [also stated as "pricing and valuation" in Sec 2.1] (15), accounts payable/receivable (10), procurement and sales (7), asset management (3).
- 78.5% of workflows are multi-task composites; examples include headcount-summary cross-check/correction, PDF-to-spreadsheet extraction, XNPV contract valuation under assumption scenarios, USD conversion of a trading-income report, French-to-English report translation, World Bank report summarization/visualization.

## Eval
- Human evaluation on ALL 172 workflows: binary pass/fail, gold standard ("marked as successful only if the model generates or revises the content and structure in accordance with the instruction and no critical errors, omissions, or unintended changes are introduced").
- Automated LLM-as-judge (GPT-5-mini) over modify/generate/QA task types with structured diffs (diff_ref vs diff_model), compact snapshots, and screenshots; rubric = completeness, numerical/logical correctness, over-edit avoidance, readability. Agreement with human labels: 82.1% (GPT 5.1 Pro) / 90.2% (Claude Sonnet 4.5) accuracy; recall 83.3%/88.4%; precision 73.6%/76.0% — "automated evaluation may overestimate accuracy by several percentage points" (Sec 3.2.1).

## Data realism
- In-the-wild enterprise sourcing: Enron corpus (~15,000 spreadsheet files, 500,000 emails from 150 executives/employees), EUSES (~450 financial spreadsheets), investment/securities firms, World Bank, Canadian and British governments. "preserving in-the-wild messiness across multimodal artifacts" (Abstract).
- 700+ hours of domain-expert annotation; inter-annotator validation on all workflows + LLM secondary checkers.
- Scale/messiness: median workflow 15K cells (mean 157K; max workbook 3.7M cells); mean 21.5K formulas per workflow (median 212); 92.4% of workflows multi-sheet (avg 8, max 91 sheets); 86.6% multi-file (up to 14 files).

## Agent scope
- Product-side web agents: ChatGPT (GPT 5.1, Pro mode) and Claude (Sonnet 4.5, thinking mode), web browsing enabled, history disabled; iterative multi-tool-call file manipulation returning downloadable spreadsheets.
- API-based: 5 frontier LLMs (GPT 5.1, Claude Sonnet 4.5, Grok 4, Qwen 3 Max, Gemini 3 Pro Preview) as SINGLE-CALL code-generation agents (SpreadsheetBench-derived harness; Python/openpyxl/pandas/matplotlib/scikit-learn executed in sandboxed Docker/Jupyter; strict one-shot, no retry; semantic-rich tuple spreadsheet encoding; multimodal/PDF handling; truncation for context limits).

## Key numbers (exact quotes)
- "GPT 5.1 Pro spends 48 hours in total yet passes only 38.4% of workflows, while Claude Sonnet 4.5 passes just 25.0%" (Abstract).
- "even the frontier agents pass only fewer than 40% of workflows (GPT 5.1 Pro spends 16.8 minutes per workflow on average)" (Sec 1).
- Table 3 (Sec 3.2.1): human eval GPT 5.1 Pro 66/172 (38.4%), Claude Sonnet 4.5 43/172 (25.0%); automated eval 72/172 (41.9%), 50/172 (29.1%).
- "GPT 5.1 Pro decreases from 44.3% (workflows with ≤2 tasks) to 23.5% (workflows with ≥2 tasks), and Claude Sonnet 4.5 decreases from 30.3% to 11.8%" (Sec 3.2) [note: paper text renders the second threshold as ">2" in context of "more than two tasks"].
- Error analysis (Claude Sonnet 4.5 web, Sec 3.3): 10% task misunderstanding, 25% data retrieval errors, 35% formula reasoning errors, 25% code generation errors, 5% data rendering errors.
- API single-call: "GPT 5.1 Pro achieves 41.9%, while GPT 5.1 with our API-based agent design reaches 32.0%" (automated eval, Sec 3.2).

## LEAF CELLS (justified)
- **1.2 reconciliation: P** — Validation/Review (37 workflows) = "checking consistency and reconciling calculations within a sheet or across sheets/files" (e.g., headcount summary cross-check, equity roll-forward difference test); figure/calc reconciliation, not bank/subledger reconciliation.
- **2.1 budgeting: P** — "planning and budgeting" business type (26 workflows); email-induced workflows like "revise the 2002 allocations"; budget-artifact updates, not a full budget cycle.
- **2.2 forecasting: P** — "predictive modeling" business type (33 workflows); Fig. 3 "end-to-end predictive modeling workflow commonly performed by financial analysts"; forecasting embedded in spreadsheet workflows, not an FP&A forecast process.
- **2.4 mgmt reporting: P** — reporting is largest business type (48 workflows); Summary/Visualization (33) "producing summaries or charts that surface key financial insights"; report generation from tabular data (Fig. 18), internal trading-income-by-trader summary (Fig. 17).
- **2.5 modeling/spreadsheets: F** — the benchmark's core: end-to-end spreadsheet manipulation/modeling workflows (Financial Modeling task type; XNPV contract valuation Example 4; 27M cells; formula reasoning central).
- **2.6 decision support: P** — Financial Modeling tasks run "scenario and sensitivity analysis" (e.g., XNPV under assumption combinations included/excluded); analysis subtask, no decision-recommendation output.
- **6.1 M&A valuation/modeling: P** — "a valuation model from an investment firm can be turned into a financial modeling task" (Sec 2.1.3); valuation/timing model calibration; valuation craft only, no deal/M&A context.
- **7.1 P2P: P** — business types "accounts payable/receivable (10)" and "procurement and sales (7)"; AP/procurement spreadsheet workflows exist but no transactional P2P process execution described.
- **7.2 O2C: P** — same tags cover receivable/sales-side spreadsheet workflows (AP/AR 10, procurement and sales 7); no invoice-to-cash process execution described.

Not scored (no evidence in text): 1.1, 1.3, 1.4, 1.5, 1.6, 1.7, 2.3, 3.1–3.4, 4.1–4.4, 5.1–5.3, 6.2, 6.3, 7.3, 9.1, 9.2.

## Matrix fields
- **Band:** core (explicitly finance & accounting enterprise workflows: budgeting, reporting, AP/AR, planning; plus trading/asset-management adjacents).
- **Verification:** fulltext.

## UNVERIFIED / caveats
- Figures 1–19 are images in the HTML; task-per-workflow distribution and pass-rate-by-task-type read only from surrounding text/tables, not the figure graphics.
- Business-type label inconsistency in paper: "pricing and valuation" (Sec 2.1) vs "pricing and budgeting (15)" (Sec 2.2) — likely typo; both quoted.
- The "48 hours in total" is aggregate GPT 5.1 Pro time across the benchmark (avg 16.8 min/workflow), not per-workflow.
- Trading and risk management (35 workflows) and asset management (3) fall outside the CFO leaf taxonomy (markets-side); noted here, not scored. USD-conversion example uses monthly-average FX rates (Fig. 17) but is report translation, not treasury FX management — 3.2 not scored.
