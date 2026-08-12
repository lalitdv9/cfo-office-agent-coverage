# BlueFin: Benchmarking LLM Agents on Financial Spreadsheets

- **ID:** arXiv:2605.30907v1 [cs.SE] 29 May 2026; CC BY-NC-SA 4.0. Dataset: huggingface.co/datasets/Longitude-Labs/bluefin-release; code: github.com/Longitude-Labs/bluefin
- **Authors:** Srivatsa Kundurthy*, Clara Na*, Colton Moraine, Anoushka Mohta, Case Winter, George Fang, John Ling, Emma Strubell, Zach Kirshner (Longitude Labs Inc.; Cornell; CMU). *Equal contribution; correspondence [email removed].
- **Status:** FULL TEXT fetched 2026-07-16 from https://arxiv.org/html/2605.30907v1 (main body + Appendices A–E.1 read; fetch truncated inside Appx E — see UNVERIFIED). This note supersedes the abstract-level screening entry (screening.csv / included_papers.csv, verification=abstract).

## Summary
Benchmark of 131 expert-authored professional-finance spreadsheet tasks (10 synthesis, 82 manipulation, 39 interrogation) with 3,225 binary rubric criteria in 6 categories (Formula Correctness, Model Integration, Output Validation, Perturbation, Presentation, Pitfalls). Agents operate a 20-tool spreadsheet harness (read/write/format primitives, recalc via LibreOffice-headless with iterative calc for circular debt/LBO references, sandboxed openpyxl execute_python) under a minimal 61-word system instruction. Generative tasks graded by an agentic LM judge (GPT-5.4, high reasoning) using the same tool environment; judge validated against expert consensus. Five frontier models evaluated on 120 held-out tasks; none exceeds 50% overall. Tasks mirror investment-banking/private-equity analyst spreadsheet work (45+ min to multiple hours per task).

## Tasks
- 131 tasks / 3,225 rubric criteria (Table 1): synthesis = spreadsheet creation from NL prompt (10; incl. "full debt builds and merger models... multiple hours"); manipulation = modify a seed workbook per NL brief (82; dominant category, "at least 45+ minutes of work for an analyst"); interrogation = comprehension/QA over a workbook, often requiring assumption updates + recalculation of multi-level dependencies (39).
- Manipulation held-out set (n=75) spans 5 financial-modeling categories (Fig. 2): "Planning & Forecasting at 39%, Valuation & Deal Analysis at 24%, Financial Statements at 19%, Supporting Schedules at 11%, Reporting & Monitoring at 8%" and 16 industries.
- Public release: 11 tasks / 305 criteria; 120 tasks held out.

## Eval method
Agentic LM-judge over expert-validated binary rubrics: judge (GPT-5.4, reasoning_effort=high, domain-opinionated SI) inspects static structure and dynamic behavior (mutate input → recalc_workbook → check output within tolerance); binary decision per criterion with mandatory cell-level evidence; score = weighted points ratio (0–100), non-completions = 0. Judge selection via inter-annotator alignment study over 384 criteria (Krippendorff's alpha 0.826; GPT-5.4 macro-F1 0.839 vs Gemini 3.1 Pro 0.803, Sonnet 4.6 0.805). Interrogation tasks have specified correct answers (no rubric). Plus a 2-reviewer human utility study (Appx C).

## Data realism
High for expert-authored (not naturally-occurring) data: 78 vetted finance-professional contributors across 7 countries (IB/PE/HF/consulting up to MD and fractional CFO), compensated above market; ~5 hours annotator labor per task; multi-stage review; PII/IP screening; seed workbooks hand-created by finance experts plus "pre-existing models collected from industry experts"; hidden set retained against leakage. Rubric candidates drafted by Claude Opus 4.6, then expert-validated/refined.

## Agent scope
Multi-step single-agent tool use: 20-tool harness in 6 categories + sandboxed execute_python (no file I/O/network); minimal-elicitation 61-word SI (HELM/GAIA philosophy); models decide their own workflows (mean turns 24 GPT-5.5 vs 38 Opus). No multi-agent, no external retrieval; single workbook as sole context.

## Key numbers (exact quotes + location)
- Abstract: "we curate a set of 131 challenging, complex tasks with real-world relevance in the domain, containing 3,225 granular rubric criteria".
- Abstract (HEADLINE): "Frontier LLMs demonstrate poor performance on the challenging benchmark, with the strongest LLMs achieving less than 50% average scores across tasks – models exhibit particular weaknesses in dynamic correctness."
- Table 2 (held-out, N=120): Overall — Opus 4.7 49.2, Sonnet 4.6 42.9, GPT-5.5 49.6, Gemini 3.1 Pro 45.9, Grok 4.20 31.3; caption: "No frontier model exceeds 50% performance."
- Abstract: "Our judge achieves parity with expert consensus (α=0.826) with a macro-F1 score of 0.839."
- §4.2: "we observe a roughly 30 point gap between performance on formula correctness criteria, which check surface forms of static cell logic, vs dynamic-behavior correctness criteria" (Formula Correctness 50-68% vs Output Validation 20-48%, Perturbation 15-37%).
- Fig. 4 caption: "The median task sits at 46.2%; only 44% of tasks clear 50% and not a single task clears 70%."
- §4.3: "GPT-5.5 achieves a similar overall score range at 5.6x lower cost ($8.85 vs $49.21 per task)" than Opus (Fig. 5 caption).
- §2 (vs FinSheet-Bench): "our closed frontier models... achieve only 34.7%-50.0% accuracy performance on interrogation tasks".

## LEAF CELLS
- **2.5:F** — building, modifying, auditing, and exercising driver-based financial workbooks is the benchmark's entire object (synthesis/manipulation/interrogation over professional finance models incl. 3-statement, DCF, LBO/debt schedules, waterfalls); end-to-end from NL brief to graded workbook.
- **2.2:P** — "Planning & Forecasting" is the largest manipulation category (39%, Fig. 2), but forecasting is exercised as workbook construction/modification, not an FP&A rolling-forecast workflow from actuals; ambiguity: category label (Opus-tagged), no task-level forecast-process evidence.
- **6.1:P** — "Valuation & Deal Analysis" 24% of manipulation tasks; DCF/merger-model/waterfall-IRR builds (rubric examples in Appx A reference DCF tab, WACC, GP/LP waterfall) — valuation as spreadsheet modeling, not target screening.
- **2.4:P** — AMBIGUOUS: "Reporting & Monitoring" category (8% of manipulation set, ~6 tasks) plausibly covers management-reporting workbooks, but no task example appears in the text; could equally be model-monitoring dashboards. Counted P with this stated ambiguity.
- (Considered, NOT tagged: 2.1 budgeting — "Planning & Forecasting" may include budget builds but no budgeting task evidenced; 3.3 — debt builds are modeling artifacts, not issuance/covenant management; 1.7 — "Financial Statements" category = 3-statement model construction, not statutory filing/tie-out.)
- Band note: tasks mirror IB/PE analyst work (§3.1) — persona is deal-side, but the measured medium (leaf 2.5, cross-cutting) is core; consistent with taxonomy cross-check treating BlueFin as core 2.5 evidence.

## UNVERIFIED
- Fetch truncated mid-Appendix E.1 (judge SI base64): Appx E.2–E.9 (tool catalog, sandbox, adapters, termination, truncation, logs, cloud, replay), Appx F (Table 6 benchmarking costs), and Appx G case-study prose not read (G scores visible in TOC/§4.4.1: CS1 Gemini 22.2%/Opus 30%; CS2 32%/64%/88%; CS3 27.7x cost gap also stated in §4.4).
- Figures 1–5 are images; category/industry splits taken from captions.
- Venue beyond arXiv not stated.
