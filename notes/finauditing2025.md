# FINAUDITING: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs
- arXiv: 2510.08886 (v1). Authors: Yan Wang (The Fin AI), Keyi Wang (Columbia), Shanshan Yang (Stevens), Jaisal Patel (RPI), Jeff Zhao (UT Austin), Fengran Mo (U Montreal), Xueqing Peng, Lingfei Qian, Jimin Huang* (The Fin AI), Guojun Xiong (Harvard), Xiao-Yang Liu (Columbia), Jian-Yun Nie (U Montreal). Same Fin AI group as EnterpriseArena.
- Status: full text fetched (arxiv.org/html/2510.08886v1); abstract + header read by main assistant.
## Summary (abstract, exact quotes)
"the first taxonomy-aligned, structure-aware, multi-document benchmark for evaluating LLMs on financial auditing tasks. Built from real US-GAAP-compliant XBRL filings... three complementary subtasks, FinSM for semantic consistency, FinRE for relational consistency, and FinMR for numerical consistency... Extensive zero-shot experiments on 13 state-of-the-art LLMs reveal that current models perform inconsistently... with accuracy drops of up to 60-90% when reasoning over hierarchical multi-document structures."
## Eval: unified retrieval/classification/reasoning metrics, zero-shot (deterministic). Data: REAL US-GAAP XBRL filings. Scope: single-turn multi-document reasoning (non-agentic).
## LEAF CELLS
- 1.7 P — XBRL filing consistency checking (semantic/relational/numerical) = verification subtask of statutory reporting. AMBIGUITY: "auditing" name suggests 8.0, but tasks are filing-consistency checks usable in reporting tie-out; scored 1.7 P with this note. NOT 1.3 (hierarchical XBRL structure ≠ intercompany consolidation).
## UNVERIFIED: per-subtask dataset sizes; venue (ACM template, conference placeholder text).
