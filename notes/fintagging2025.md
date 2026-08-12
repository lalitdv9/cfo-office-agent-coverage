# FinTagging: Benchmarking LLMs for Extracting and Structuring Financial Information
- arXiv: 2505.20650 (v1 title on arXiv header: "...Benchmarking LLMs for Extracting and Structuring Financial Information"; corpus CSV earlier title said "An LLM-ready Benchmark..." — v1 header form used here; flagged minor title-variant)
- Status: full text fetched (arxiv.org/html/2505.20650v1); abstract + contributions read by main assistant; results tables NOT parsed.
## Summary (from abstract, exact)
"the first full-scope, table-aware XBRL benchmark designed to evaluate the structured information extraction and semantic alignment capabilities of large language models (LLMs) in the context of XBRL-based financial reporting... decomposes the XBRL tagging problem into two subtasks: FinNI for financial entity extraction and FinCL for taxonomy-driven concept alignment. It requires models to jointly extract facts and align them with the full 10k+ US-GAAP taxonomy across both unstructured text and structured tables".
## Eval: zero-shot LLM evaluation over extraction + alignment subtasks (deterministic metrics). Data realism: real XBRL/US-GAAP reporting content (text + tables). Agent scope: single-turn structured extraction (non-agentic).
## LEAF CELLS
- 1.7 P — XBRL fact extraction + US-GAAP concept alignment = tagging subtask of statutory reporting (not statement preparation/filing).
## UNVERIFIED: headline result numbers (results section not parsed); exact dataset counts.
