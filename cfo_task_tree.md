# The CFO-Office Task Taxonomy — v1.2 (2026-07-16; v1.1 ratified at Checkpoint 3; v1.2 completeness-audit amendments pending human ratification)

> Refined from the project brief seed taxonomy. Two levels: pillar → leaf. Each leaf carries a
> one-line OPERATIONAL DEFINITION used for matrix-scoring consistency (Phase 3): a benchmark
> "covers" a leaf only if its tasks fall within the definition.
> v1.0 will follow the corpus cross-check (leaf additions/changes documented in §Changelog).

**Standing scope ruling (Checkpoint 1, human-approved 2026-07-16):** investor-side
analyst-research benchmarks (Finance Agent Benchmark, FinanceQA, FinanceBench,
BigFinanceBench) are NOT scored against this tree as core rows; they form a visually
separated "adjacent benchmarks" band in the coverage matrix (code ADJ below).

## 1. Controllership / Record-to-Report (R2R)
- **1.1 Transaction capture & journal entries** — Record and classify transactions, accruals, and adjusting journal entries in the general ledger under applicable GAAP/IFRS.
- **1.2 Account reconciliation** — Match balances and transactions across GL, subledgers, bank statements, and supporting documents; identify, explain, and resolve breaks.
- **1.3 Intercompany & consolidation** — Eliminate intercompany balances, translate foreign-currency results, and consolidate entity trial balances into group financial statements.
- **1.4 Close orchestration** — Plan, sequence, execute, and track the period-end close checklist (tasks, owners, dependencies, sign-offs) across systems to a certified close.
- **1.5 Technical accounting & policy** — Research and apply accounting standards to complex transactions; draft accounting position memos and policy documentation.
- **1.6 Internal controls & SOX execution** — Design, operate, document, and evidence internal controls over financial reporting, including segregation-of-duties enforcement.
- **1.7 Statutory & external reporting (incl. XBRL)** — Produce external filings and statutory statements: drafting, tie-out, XBRL tagging, and jurisdiction-specific localization. *(Scoping note v1.2: sustainability/ESG disclosure prepared by controllership falls within this leaf.)*
- **1.8 Asset & project accounting** — Account for fixed assets (additions, transfers, depreciation, disposals, register maintenance) and capital projects (project transactions, capitalization, close-out). *(Added v1.2 — APQC 8.3.3/8.4; see Changelog.)*

## 2. Financial Planning & Analysis (FP&A)
- **2.1 Budgeting & long-range planning** — Build annual budgets and multi-year plans from driver assumptions, targets, and cross-functional inputs, including capital-expenditure planning and project approval. *(def. extended v1.2 — APQC 8.4.1)*
- **2.2 Forecasting** — Produce and update rolling forecasts of P&L/cash/balance-sheet lines from actuals and drivers.
- **2.3 Variance analysis** — End-to-end: pull data from source systems → reconcile → compute variances → flag by materiality → root-cause → draft commentary → escalate. (The paper's fully-worked example workflow.)
- **2.4 Management & board reporting** — Assemble recurring management/board packs: KPIs, financial summaries, narrative commentary.
- **2.5 Financial modeling & spreadsheet operations** — Build, modify, audit, and exercise driver-based financial models and workbooks (cross-cutting medium; scored here).
- **2.6 Business partnering & decision support** — Ad-hoc decision analysis: pricing, make-vs-buy, scenario and sensitivity analysis for operating partners.
- **2.7 Cost & profitability accounting** — Allocate operating/overhead costs across products and services: product costing, inventory accounting, cost-of-sales analysis, profitability reporting. *(Added v1.2 — APQC 8.1.2; see Changelog.)*

## 3. Treasury
- **3.1 Cash & liquidity management** — Daily cash positioning, pooling/sweeping, short-horizon liquidity forecasting (e.g., 13-week cash forecast), and in-house banking / intercompany netting. *(def. extended v1.2 — APQC 8.7.3)*
- **3.2 FX & interest-rate risk** — Identify exposures, propose/execute hedges, and support hedge accounting.
- **3.3 Debt, investments & capital markets** — Manage debt issuance/repayment, short-term investments, covenant compliance monitoring, and rating-agency/banking relationships; funding decisions. *(def. extended v1.2 — APQC 8.7.4)*
- **3.4 Working capital management** — Analyze and optimize DSO/DPO/DIO and cash conversion cycle.

## 4. Tax
- **4.1 Tax provision** — Compute current/deferred income-tax provision for financial statements (ASC 740 / IAS 12), including rate reconciliation.
- **4.2 Compliance & filings** — Prepare and file direct/indirect tax returns across jurisdictions from financial and transactional data.
- **4.3 Transfer pricing** — Set and document intercompany pricing policies; prepare TP documentation and analyses.
- **4.4 Planning & controversy** — Tax structuring/planning and management of audits and disputes.

## 5. Investor Relations (IR)
- **5.1 Earnings release & call preparation** — Draft earnings releases, scripts, and anticipated Q&A from internal results (company-side, pre-publication).
- **5.2 Guidance & consensus management** — Formulate external guidance and track/analyze analyst consensus against internal outlook.
- **5.3 Shareholder engagement** — Investor targeting, meeting preparation, and perception analysis.

## 6. Strategic Finance / M&A
- **6.1 Screening & valuation** — Identify/screen targets and build valuation analyses (DCF, comparables, accretion/dilution).
- **6.2 Due diligence** — Analyze target data-room financials; quality-of-earnings style analysis.
- **6.3 Synergies & post-merger integration** — Estimate/track synergies; integrate finance operations post-close.

## 7. Operational Finance
- **7.1 Procure-to-pay (P2P)** — Vendor onboarding, purchase orders, invoice capture/coding, 2/3-way matching, approval routing, payment execution, and employee expense (T&E) reimbursements. *(def. extended v1.2 — APQC 8.6.2)*
- **7.2 Order-to-cash (O2C)** — Customer credit, billing/invoicing, collections, dispute handling, and cash application.
- **7.3 Payroll & workforce compliance** — Payroll processing and payroll-adjacent statutory compliance (e.g., certified payroll reporting). *(Added v1.1 — see Changelog.)*

## 8. Internal Audit / Risk — DE-SCOPED LEAF
- **8.0 Audit & financial-risk assurance** — Journal-entry testing, misstatement/fraud detection, continuous auditing. Covered by existing reviews (JETA/MAJ/JAL/IJAIS items in corpus, category=audit); receives one de-scoping paragraph in Related Work and is EXCLUDED from matrix columns.

## 9. Finance Systems & Data
- **9.1 ERP/EPM administration & close automation** — Configure and operate finance systems, close-automation tooling, and integrations.
- **9.2 Finance data governance** — Master data (chart of accounts, entities, cost centers), data quality, and lineage for financial data.

## ADJ. Adjacent band (not tree leaves)
- **ADJ-1 Analyst/financial-research tasks** — Investor-side research over public filings/market data (per Checkpoint-1 ruling).
- **ADJ-2 Adjacent finance-workflow benchmarks** — Wealth-management ops (2512.02230) and general business-simulation economies (e.g., CoffeeBench) pending final classification.

## Corpus cross-check (v1.0, from full-text-verified papers as of 2026-07-16)

Evidence per leaf from the 22 full-text-verified corpus items (leaf tags in
`search/ft_decisions_*.csv` and `corpus/notes/`). ● = full-workflow coverage claimed by
at least one paper; ◐ = partial/subtask only; — = no verified coverage found yet.
27 records remain in full-text screening; tags may still be added, but every pending
record's title/abstract was checked — none plausibly fills the empty pillars below.

| Leaf | Evidence so far |
|---|---|
| 1.1 JEs | ◐ close-orchestration system (2606.20058, simulated agents); FinMaster pending |
| 1.2 Reconciliation | ● FinBalance (dedicated benchmark); ◐ 2606.20058 |
| 1.3 Consolidation | ◐ 2606.20058 only; FinAuditing (XBRL multi-doc consistency) pending |
| 1.4 Close orchestration | ◐ 2606.20058 — a production SYSTEM report; no public benchmark exists |
| 1.5 Technical accounting | ◐ FinanceQA (ADJ band, accounting conventions); FinRule-Bench pending |
| 1.6 SOX/controls | — (CFAgentBench's money-movement guards are a candidate ◐; decide in Phase 3) |
| 1.7 Statutory reporting/XBRL | ● FinReporting (localization); ◐ 2603.22651; XBRL cluster pending (FinTagging, XBRLTagRec, FinAuditing, LAVA, XBRL-Agent) |
| 2.1–2.4 FP&A cycle | ◐ 2606.20058 only; NO dedicated budget/forecast/variance/mgmt-reporting benchmark |
| 2.5 Modeling/spreadsheets | ● WorkstreamBench, BlueFin; Finch/FinSheet-Bench/SpreadsheetArena pending |
| 2.6 Decision support | ◐ 2606.20058 |
| 3.1/3.2/3.4 Treasury | — empty |
| 3.3 Debt/capital markets | ◐ EnterpriseArena (funding decisions within simulation) |
| 4.1 Provision, 4.3 TP | — empty |
| 4.2/4.4 Tax compliance/planning | ◐ Tax Attorneys 2023 (non-agentic legal reasoning only) |
| 5.1–5.3 IR (company-side) | — empty (earnings-call ANALYSIS work is investor-side, excluded/ADJ) |
| 6.1/6.3 M&A | — empty |
| 6.2 Due diligence | ◐ IPO Finance Agent (ADJ band, S-1 diligence questions) |
| 7.1 P2P | ● invoice cluster (2509.04469, 2510.15727, 2511.05547), CFAgentBench, ◐ Better Bill GPT; org-memory P2P pending |
| 7.2 O2C | ◐ CFAgentBench; CoffeeBench pending |
| 8.0 Audit (de-scoped) | corpus category=audit (4 journal items + arXiv audit benchmarks pending) |
| 9.1 ERP/close automation | ● 2606.20058; ◐ 2510.15727 |
| 9.2 Data governance | — empty |

**Structural conclusion:** the corpus forced NO new leaves and NO removals; v0.9 structure
stands as v1.0. Emerging empty/near-empty cells (research-agenda payload, to be confirmed
in Phase 3): treasury ops (3.1/3.2/3.4), tax provision & transfer pricing (4.1/4.3),
company-side IR (5.x), SOX/controls (1.6), consolidation (1.3), close orchestration as a
BENCHMARK (1.4), end-to-end variance analysis (2.3), finance data governance (9.2). This
matches the project brief expectations — now verified against fetched texts rather than assumed.

**Figure:** `paper/figures/cfo_taxonomy.tex` (TikZ, compiles standalone; preview
`cfo_taxonomy.pdf`, single-column sized, verified overlap-free).

## Completeness audit v1.2 (2026-07-16) — one-by-one check against APQC PCF 8.0 "Manage Financial Resources"

External checklist: APQC Process Classification Framework, category "Manage Financial
Resources", official definitions document (v2.0.0/PCF 6.0.0, fetched from apqc.org
2026-07-16). Every APQC process group/process mapped to a leaf:

| APQC process | Our leaf | Verdict |
|---|---|---|
| 8.1.1 Planning/budgeting/forecasting | 2.1, 2.2 | covered (2.1 def. extended: capital planning, 8.4.1) |
| 8.1.2 Cost accounting & control (product costing, inventory acct, profitability) | — | **MISS → new leaf 2.7** |
| 8.1.3 Cost management | 2.7 + 2.6 | covered after fix |
| 8.1.4 Evaluate/manage financial performance | 2.4 + 2.6 | covered |
| 8.2.1–8.2.5 Revenue accounting (credit, invoicing, AR, collections, adjustments) | 7.2 | covered (dispute handling = adjustments/deductions) |
| revenue recognition decisions | 1.5 | covered (ASC 606 in def.) |
| 8.3.1 Policies & procedures | 1.5/1.6 | covered |
| 8.3.2 General accounting (GL, JEs, allocations, intercompany, recon, trial balance) | 1.1, 1.2, 1.3; CoA → 9.2 | covered |
| 8.3.3 Fixed-asset accounting | — | **MISS → new leaf 1.8** |
| 8.3.4 Financial reporting | 1.7 (external) + 2.4 (management) | covered |
| 8.4.1 Capital planning & project approval | 2.1 (def. extended) | covered after fix |
| 8.4.2 Capital project accounting | 1.8 | covered after fix |
| 8.5.1–8.5.3 Payroll (time, pay, payroll taxes) | 7.3 | covered (added v1.1) |
| 8.6.1 Accounts payable | 7.1 | covered |
| 8.6.2 Expense reimbursements (T&E) | 7.1 (def. extended) | covered after fix |
| 8.7.1 Treasury policies | 3.x umbrella | covered |
| 8.7.2 Manage cash (positions, forecasts, bank relationships) | 3.1 | covered |
| 8.7.3 In-house bank / intercompany netting | 3.1 (def. extended) | covered after fix |
| 8.7.4 Debt & investment | 3.3 (def. extended: investments) | covered after fix |
| 8.7.5 Risk & hedging | 3.2 | covered |
| 8.8.1–8.8.3 Internal controls (establish, operate, report) | 1.6 | covered |
| 8.9.1 Tax strategy & plan | 4.4 | covered |
| 8.9.2 Process taxes (provision + filings) | 4.1, 4.2 | covered |
| 8.10.1–8.10.4 International funds/consolidation (rates, FX transactions, exposure, reporting) | 3.2, 3.1, 1.3, 1.1 | covered |

Functions in our tree beyond APQC-8 (role-scoped, deliberate): 1.7 statutory/XBRL detail,
5.x investor relations, 6.x strategic finance/M&A, 8.0 audit (de-scoped), 9.x finance
systems, 4.3 transfer pricing. APQC places these in other categories or omits them; the
Office-of-the-CFO role owns them, so they stay.

Corpus evidence for the new leaves: 1.8 — CFAgentBench "Project Accounting" domain
(157 task specs, previously mapped to NO leaf: a taxonomy miss caught by this audit) and
FinBalance asset-disposal/rollforward concept flags → both ◐. 2.7 — no benchmark found
→ new EMPTY column (added to the research-agenda payload).

## Changelog
- v0.9 (2026-07-16): initial refinement of INSTRUCTIONS §3 seed. Changes from seed:
  (a) split seed pillar-1 "reporting" into 1.4 close orchestration vs 1.7 statutory/external
  reporting (corpus items separate cleanly: close-orchestration systems vs XBRL/disclosure
  benchmarks); (b) "spreadsheet financial modeling" placed as leaf 2.5 with cross-cutting
  note; (c) Internal Audit/Risk collapsed to single de-scoped leaf 8.0 per boundary rule;
  (d) Finance Systems split into 9.1/9.2; (e) ADJ band codified per Checkpoint-1 ruling.
  Payroll and T&E deliberately NOT added (absent from seed and from corpus measurements;
  candidate addition if snowballing surfaces evidence).
- v1.2 (2026-07-16, completeness audit vs APQC PCF 8.0): leaves **1.8 Asset & project
  accounting** and **2.7 Cost & profitability accounting** ADDED (APQC 8.3.3/8.4 and 8.1.2;
  1.8 additionally evidenced by CFAgentBench's unmapped Project Accounting domain);
  definitions of 2.1, 3.1, 3.3, 7.1 extended (capital planning, in-house banking/netting,
  investments, T&E); 1.7 scoping note (ESG disclosure). Figure, matrix columns, and paper
  updated. PENDING human ratification.
- v1.1 (2026-07-16, Phase 3): leaf **7.3 Payroll & workforce compliance ADDED** per Phase-2
  rule "add missing leaves if a benchmark tests something not in the tree": CFAgentBench's
  Payroll & HR domain (112 task specs; certified-payroll WH-347 validation among the 40
  executable oracle-validated tasks) is direct corpus evidence. **RATIFIED by human at
  Checkpoint 3 (2026-07-16); figure regenerated with 7.3.**
- v1.0 (2026-07-16): corpus cross-check completed against 22 full-text-verified papers
  (+ snowball hop); no structural changes required; evidence table added; figure produced
  (TikZ + PDF, overlap-checked). Snowballing surfaced no payroll/T&E measurement — leaves
  stay out. Awaiting Checkpoint-2 approval.
