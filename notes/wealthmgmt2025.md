# wealthmgmt2025

## Title
- arXiv metadata / registered title (VERIFIED via DataCite DOI record 10.48550/arXiv.2512.02230 and arXiv abs listing): "Benchmarking LLM Agents for Wealth-Management Workflows"
- Title as printed inside the document (fetched HTML v1 of the dissertation): "Benchmarking LLM Agents in Wealth-Management Workflows"
- NOTE the for/in discrepancy between the arXiv metadata and the in-document title page. Cite the arXiv metadata form ("for").

## IDs
- arXiv: 2512.02230 (v1), cs.AI, submitted 2025-12-01 (v1 updated 2025-12-03)
- DOI: 10.48550/arXiv.2512.02230
- 56 pages, 8 figures (arXiv comment field via DataCite)
- License: CC BY 4.0

## Authors (VERIFIED)
Rory Milsom — sole author. MSc dissertation, Master of Science, School of Informatics, University of Edinburgh, 2025. (DataCite creators: "Milsom, Rory"; confirmed on the fetched HTML title page.) Acknowledgements thank Dr Alexandra Birch-Mayne and Barry Haddow for guidance (supervisors; not co-authors).

## Status
FETCHED 2026-07-16: (1) https://arxiv.org/abs/2512.02230 (abstract); (2) full HTML https://arxiv.org/html/2512.02230v1 — Phase 3 FULL READ of Ch. 3 Methodology (task suite 3.5, checkpoints, evaluators, autonomy 3.6, data 3.7-3.9), Ch. 4 Results (Experiments 1-2, quantitative + qualitative), Ch. 5 Conclusion, Appendix task catalogue headings; (3) DataCite record. VERIFIED, verification=fulltext.

## Abstract (verbatim, from abs page / DataCite)
"Modern work relies on an assortment of digital collaboration tools, yet routine processes continue to suffer from human error and delay. To address this gap, this dissertation extends TheAgentCompany with a finance-focused environment and investigates whether a general purpose LLM agent can complete representative wealth-management tasks both accurately and economically. This study introduces synthetic domain data, enriches colleague simulations, and prototypes an automatic task-generation pipeline. The study aims to create and assess an evaluation set that can meaningfully measure an agent's fitness for assistant-level wealth management work. We construct a benchmark of 12 task-pairs for wealth management assistants spanning retrieval, analysis, and synthesis/communication, with explicit acceptance criteria and deterministic graders. We seeded a set of new finance-specific data and introduced a high vs. low-autonomy variant of every task. The paper concluded that agents are limited less by mathematical reasoning and more so by end-to-end workflow reliability, and meaningfully affected by autonomy level, and that incorrect evaluation of models have hindered benchmarking."

## Summary
Edinburgh MSc dissertation extending TheAgentCompany (TAC, arXiv 2412.14161) with a wealth-management environment: EspoCRM + OwnCloud + Rocket.Chat (Sotopia NPCs) + Plane in docker-compose; 28 synthetic finance artifacts over 5 client profiles + 1 colleague; 12 task-pairs in 3 difficulty tiers, each in high-autonomy (brief) vs low-autonomy (schema/path-constrained) variants (24 task images); 3-5 checkpoint deterministic Python evaluators graded post-hoc from service state. Single agent config (OpenHands + GPT-4o). Key result: new suite 49.0% checkpoints (HA) vs legacy TAC finance tasks 14.8%; low autonomy lifts to 69.4% and 4/12 resolved; failures cluster in access/auth and delivery (WebDAV, chat), not arithmetic.

## Tasks (Table 3.1; Appendix 6.1-6.2)
- Level 1 (retrieval/summarisation): Net Worth Snapshot.
- Level 2 (analytical/computational): Asset Aggregation; Year-End Tax Summary ("Compile taxable income components for tax reporting"); Trusts & Beneficiaries ("Reconcile trust records with beneficiaries to find discrepancies"); Tax Threshold Calculation ("Compute estate-level tax due using bands and rates"); Pension Projection; Expense Categorisation; Capital Gains Computation (FIFO lot matching); Portfolio Asset Allocation.
- Level 3 (synthesis/communication/decision support): Emergency Fund (savings >= 6 months expenses, pass/fail DM); Meeting Scheduling Coordination (calendars -> confirmation + invite); Quarterly Metrics Analysis ("Analyse quarterly business metrics and inform stakeholders" -> Rocket.Chat updates + Plane task closed).
- Design grounded in a 1-hour semi-structured interview with a senior product manager at Aveni Ltd (29/05/25) + literature review; deliberately assistant-level ("artefacts such as summaries, checklists, draft communications, data pulls, and simple analytics, rather than discretionary investment decisions").

## Eval method
Checkpoint-based deterministic grading following/refining TAC: 3-5 checkpoints per task (vs TAC's coarser <3), post-hoc over final service state via APIs/WebDAV; numeric tolerance "max 10^-6 absolute or 1% relative"; CSV grading schema/key-based, order-insensitive, values recomputed ("never byte-for-byte"); strict regex/path checks for text deliverables; LLM-as-judge ONLY for yes/no predicates over Rocket.Chat transcripts; "make-good" upstream credit when final artefact fully correct. Metrics: resolved (all checkpoints), % checkpoints passed, mean step-count, API cost.

## Data realism
Synthetic, closed-world: artifacts drafted via "ChatGPT o4-mini-high" from NL briefs, normalized to UTF-8/LF, seeded at fixed paths (/Finance_Documents/Clients/<Client>/); cross-service dependencies (CRM tables vs deed in document store); minimal irrelevant filler + TAC legacy distractors; NPC colleagues via Sotopia streaming OpenAI completions. Realism grounded in one industry interview + desk research; author flags "closed-world setup with synthetic, but carefully normalised, data, a small number of clients and tasks" as limitation.

## Agent scope
Multi-step, multi-application single agent: stock OpenHands runner with GPT-4o (rendered "GPT-40" in HTML), host networking to EspoCRM/OwnCloud/Rocket.Chat/Plane; simulated-colleague dialogue; mean 10.8-12.3 steps/run. Not multi-agent (future work); single model configuration is an author-acknowledged limitation.

## Key numbers (exact quotes + location)
- Table 4.1: "Original TAC (12 tasks): Resolved 0/12; % Checkpoints Passed 8/54 = 14.8%; Mean Step-Count 11.3; Cost $0.1033" vs "New WM (HA, 12 tasks): 2/12; 24/49 = 49.0%; 10.8; $0.1373".
- Table 4.2: "High Autonomy (HA): 2/12; 24/49 = 49.0%; 10.8; $0.1373" vs "Low Autonomy (LA): 4/12; 34/49 = 69.4%; 12.3; $0.1237".
- §4.2.1: Level-2 pass-rate "rises from ≈56.9% (high autonomy) to ≈82.4% (low autonomy)"; "Level 3 tasks remain flat at ≈35.5% under both styles".
- §4.2.1 task-level: "Pension Growth, Trusts & Beneficiaries, Client Net Worth, and Asset Aggregation jump from 25% to 75%, 25% to 75%, 50% to 100%, and 20% to 100% respectively when schemas/paths are provided".
- §5.1 (HEADLINE): "agent competence on finance tasks is limited less by mathematical reasoning than by end-to-end workflow reliability (finding the right files, following naming/location rules, and delivering outputs)."

## LEAF CELLS (adjacent band, ADJ-2 adjacent finance-workflow; cells flag task-shape overlap only)
- **1.2:P** — Trusts & Beneficiaries is a cross-system reconciliation workflow (CRM percentages vs deed, discrepancy report with Difference column); AMBIGUITY: reconciles client/trust records, not GL/subledger/bank balances — reconciliation-shaped, wrong domain object.
- **4.2:P** — Year-End Tax Summary (taxable income components), Tax Threshold Calculation (banded estate tax due), Capital Gains Computation (FIFO) exercise tax-computation/compliance-support; AMBIGUITY: individual/estate-level client tax work, not corporate return preparation/filing.
- **2.4:P** — AMBIGUOUS: Quarterly Metrics Analysis ("analyse quarterly business metrics and inform stakeholders") is a lightweight management-reporting/stakeholder-update task via chat + issue tracker; not a recurring management/board pack.
- (Function-level scope note retained from screening: wealth-management assistant workflows are client/CRM-centric, not corporate finance; no coverage of close, consolidation, FP&A cycle proper, treasury, IR, P2P, O2C.)

## UNVERIFIED items
- Figures 4.1-4.6 are images (distributions read from captions/prose only).
- Appendix 6.3+ (data schemas, task-generation pipeline prototype details) skimmed at heading level only.
- Exact grade/award status of the dissertation not public; supervisor roles inferred from acknowledgements.
- "GPT-40" in HTML assumed to be GPT-4o (OCR/render artifact).
