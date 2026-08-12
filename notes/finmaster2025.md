# FinMaster: A Holistic Benchmark for Mastering Full-Pipeline Financial Workflows with LLMs

- arXiv ID: 2505.13533 (v1)
- Authors: Junzhe Jiang, Chang Yang (PolyU, equal contrib.); Aixin Cui (CUHK); Sihan Jin (HKUST); Ruiyu Wang (KTH); Bo Li, Xiao Huang (PolyU); Dongning Sun (Peng Cheng Lab); Xinrun Wang (SMU, corresponding)
- Status: full-text fetched Y (arxiv.org/html/2505.13533v1; abstract, §1-3 structure, preliminaries, FinSim/FinSuite sections, results excerpts read; scored by main assistant directly)

## Summary
FinMaster assesses LLMs on "financial literacy, accounting, auditing, and consulting" via three
modules: FinSim (simulators generating synthetic, privacy-compliant company financial data,
with controllable error injection for audit tasks), FinSuite (183 tasks across types and
difficulty levels), and FinEval (unified evaluation interface). Statements are generated from
simulated transaction flows (income statement from revenue/expense transactions; balance sheet
from asset/liability/equity data; cash-flow statement from cash transactions). Headline finding:
accuracy collapses from >90% on basic tasks to ~40% on complex multi-step scenarios, with
computational error propagation (58% single-metric → 37% multi-metric).

## Tasks covered
183 tasks (FinSuite) spanning accounting (transaction→statement generation), auditing
(error-injected anomaly detection), consulting (analysis/advisory), and financial-literacy QA.

## Eval method
Deterministic accuracy over task outputs via FinEval unified interface; multi-dimensional
complexity framework for error attribution. No LLM judge mentioned in read portions.

## Data realism
Synthetic simulator data (FinSim), deliberately privacy-compliant, "replicate real-world market
dynamics"; error injection "impractical to replicate with real data" (Appendix A/D).

## Agent scope
Single-turn structured tasks over provided data (LLM evaluation, non-agentic in read portions).
UNVERIFIED whether any tool-use loop exists.

## Key numbers (exact quotes)
- "accuracy dropping from over 90% on basic tasks to merely 40% on complex scenarios requiring
  multi-step reasoning" (Abstract)
- "single-metric calculations initially demonstrating 58% accuracy decreased to 37% in
  multimetric scenarios" (Abstract)
- "advanced LLMs, including Claude-3.7-Sonnet, DeepSeek-V3, and o3-mini, achieve impressive
  accuracy of 96% on fundamental financial literacy tasks, their performance drops sharply to
  40% on complex tasks" (Conclusion region, line 268 of fetch)
- 183 tasks (Abstract: "spanning 183 tasks of various types and difficulty levels")

## LEAF CELLS
- 1.7 P — generation of income statement / balance sheet / cash-flow statement from simulated books = statement-preparation subtask (not filing/tie-out/XBRL).
- 1.1 P — transaction recording → statement pipeline exercises bookkeeping-level structure; transactions are simulator-provided, not agent-recorded (ambiguity noted).
- 2.6 P — consulting/analysis tasks (financial-indicator reasoning) = decision-support subtask.
- 8.0 (de-scoped column) — auditing tasks with injected errors; recorded here for the audit paragraph, not a matrix column.

## UNVERIFIED
- Full FinSuite task-type inventory (Appendix E tables not parsed line-by-line).
- Whether any agentic/tool-use configuration is evaluated.
- Venue status (arXiv v1, May 2025; acceptance unknown).
