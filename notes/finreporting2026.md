# FinReporting: An Agentic Workflow for Localized Reporting of Cross-Jurisdiction Financial Disclosures

- arXiv ID: 2604.05966
- Authors: Fan Zhang (1,2), Mingzi Song (3), Rania Elbadry (1), Yankai Chen (1,4, corresponding), Shaobo Wang (2), Yixi Zhou (1), Xunwen Zheng (5), Yueru He (6), Yuyang Dai (7), Georgi Georgiev (8), Ayesha Gull (9), Muhammad Usman Safder (9), Fan Wu (1), Liyuan Meng (1), Fengxian Ji (1), Junning Zhao (2), Xueqing Peng (10), Jimin Huang (10), Yu Chen (2), Xue (Steve) Liu (1,4), Preslav Nakov (1), Zhuohan Xie (1). Affiliations: (1) MBZUAI, (2) University of Tokyo, (3) Meiji Gakuin University, (4) McGill University, (5) Kyoto University, (6) Columbia University, (7) UC Berkeley, (8) Sofia University, (9) Namal University, (10) The Fin AI.
- Status: full-text fetched: Y (https://arxiv.org/html/2604.05966v1, complete paper returned in a single fetch: abstract, Sections 1-6, Tables 1-2, limitations, ethics, references)

## Summary
FinReporting is a system/demo paper (not a benchmark): an agentic workflow that converts heterogeneous annual filings from the US, Japan, and China into localized financial statements under a unified canonical ontology spanning Income Statement, Balance Sheet, and Cash Flow. The pipeline decomposes reporting into auditable stages — filing acquisition, statement identification, extraction, canonical mapping, and outputting — with structured verification between stages. A three-layer design combines a deterministic rule-based processing layer (XBRL fact selection for US/JP; PDF table parsing for CN), an LLM guardrail layer in which the LLM acts as a bounded verifier restricted to KEEP/REPAIR/NEED_REVIEW decisions with evidence grounding, and a conditional human expert review layer. Evaluation covers 18 canonical statement fields per company over 90 non-financial firms (30 per market, split 20 baseline + 10 held-out challenge), with gold labels manually validated by financial domain experts. FinReporting outperforms a naive LLM reporting pipeline mainly on the PDF-centric Chinese market (ACC 82.11 vs 78.15) and matches or slightly improves elsewhere; a backbone comparison shows small cheap models match the strongest models on accuracy at a fraction of the cost. An interactive demo supports cross-market inspection and structured export.

## Tasks covered (task design)
Not a task benchmark; an extraction/localization workflow evaluated on: 18 canonical targets per firm (IS: 5, BS: 7, CF: 6); 90 firms total (30 per market x US/JP/CN; per market: 20-company baseline split for rule development/gold annotation + 10-company held-out challenge split); annual consolidated filings of non-financial firms. Sources: SEC EDGAR 10-K XBRL (US), EDINET annual securities reports XBRL (JP), cninfo annual-report PDFs (CN). Per-field status labels: OK, MISSING, PARSE_ERROR, NOT_APPLICABLE.

## Eval method
Deterministic metrics against human-expert gold labels (no LLM judge for scoring): Filled Rate (FR, fraction of non-null outputs), Conflict Rate (CR, fraction triggering human review from rule-vs-LLM-verifier disagreement or insufficient evidence), and Accuracy (ACC vs manual labels). "Gold annotations are manually validated by financial domain experts to ensure correctness of canonical mappings and numerical consistency." (Section 4.1)

## Data realism
Real regulatory documents: "Data are collected from public regulatory disclosures: US filings from SEC EDGAR (10-K XBRL), JP filings from EDINET annual securities reports (XBRL), and CN annual reports from publicly disclosed filing PDFs." (Section 4.1). Not synthetic.

## Agent scope
Multi-step agentic pipeline/workflow (rule-based stages + constrained LLM verification + conditional human review). LLM is a bounded verifier, not a free-form agent; no tool-exploration loop, not multi-agent, not long-horizon.

## Key numbers (exact quotes / table values)
- Main results (Table 1, Section 4, GPT-4o guardrail; values FR / CR / ACC, FinReporting column): US 95.56 / 15.56 / 90.23; JP 84.44 / 15.56 / 88.36; CN 63.33 / 40.56 / 82.11. Baseline LLM_Reporting: US 94.44 / 5.56 / 89.38; JP 84.44 / 15.56 / 88.36; CN 63.33 / 26.67 / 78.15.
- Field inventory: "For each company, the system produces reporting for a fixed inventory of 18 core items spanning IS/BS/CF, with an auditable trace and a review flag when evidence is insufficient." (Section 4.1)
- Data split: "For each market, we construct a 20-company baseline split used for rule development and gold annotation, and an additional 10-company challenge split used as a held-out evaluation set, yielding 30 firms per market (90 firms total)." (Section 4.1)
- Canonical targets: "Main cross-market metrics are reported on a shared subset of 18 canonical targets (IS: 5, BS: 7, CF: 6), while market-specific extra line items are retained for UI display and qualitative analysis." (Section 4.1)
- Backbone comparison (Table 2, US filings; FR / CR / ACC / Cost $): GPT-5.2 95.56 / 8.89 / 90.23 / 36.96; GPT-5 mini 95.56 / 15.00 / 90.23 / 17.77; GPT-4o 95.56 / 15.56 / 90.00 / 34.04; Gemini-2.5-Flash 95.56 / 12.78 / 90.23 / 7.27; Gemini-2.5-Flash-Lite 95.56 / 8.89 / 90.00 / 1.47; DeepSeek-Chat 95.56 / 100.00 / 90.23 / 2.41. "smaller/efficient backbones can match the strongest models on accuracy while being dramatically cheaper" (Section 4.2).

## Relevance to CFO-office taxonomy
External-reporting/consolidation-adjacent work: statement extraction, taxonomy mapping (XBRL vs PDF), cross-jurisdiction canonicalization, anomaly logging, and audit trails. Maps to the financial reporting and disclosure-analysis branch of a CFO-office taxonomy; its constrained-verifier + audit-trail architecture is a design pattern for trustworthy CFO-office agents. Note it is a demo-track system paper with small-scale evaluation, not an agent-capability benchmark.

## UNVERIFIED items
- Publication venue/track (formatting suggests an ACL-style demo paper; not stated in fetched HTML).
- No mismatch checks were requested for this paper; all reported numbers above come directly from Tables 1-2 and Section 4 of the fetched text.
