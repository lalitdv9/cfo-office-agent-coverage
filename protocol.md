# PRISMA Search Protocol — AI Agents for the Office of the CFO

**Version:** 1.0 — registered 2026-07-16, BEFORE any search execution.
**Author of record:** Anonymous research team.
**Standard:** PRISMA 2020 (Page et al., BMJ 2021) adapted for a rapid CS/NLP survey.

## 1. Research questions

- **RQ1:** What LLM-based / agentic AI systems and benchmarks target corporate finance *function* tasks (Office of the CFO), as opposed to financial-markets tasks?
- **RQ2:** Which CFO-office functions (per the taxonomy in `cfo_task_tree.md`) are covered by existing benchmarks/systems, and which are unmeasured?
- **RQ3:** What evaluation methodologies do these works use (exact-match, rubric/LLM-judge, human expert, execution-based), and on what data realism level?

## 2. Databases and search interfaces

| # | Database | Access method in this environment | Notes |
|---|----------|-----------------------------------|-------|
| D1 | arXiv (cs.AI, cs.CL, cs.MA, cs.SE, q-fin) | arXiv export API (`export.arxiv.org/api/query`), fetched directly | Primary database; field moves on preprints |
| D2 | Semantic Scholar | Graph API (`api.semanticscholar.org/graph/v1/paper/search`) | Also used for snowballing (citations/references) |
| D3 | General web search | Search engine queries | Proxy for Google Scholar; also surfaces SSRN, publisher pages, workshop proceedings |
| D4 | Accounting journals (JETA, IJAIS, Accounting Horizons, J. Accounting Literature, ISAFM) | Targeted web search with venue names; publisher pages fetched to verify | No institutional API access in this environment — approximated via D3 and direct page fetches. **Protocol limitation, documented.** |
| D5 | ACM DL / IEEE Xplore | Targeted web search (site-scoped) + DOI resolution | Same limitation as D4 |

**Honest constraint statement:** this search is executed in a sandboxed environment without
institutional database subscriptions. arXiv and Semantic Scholar are searched natively via
their public APIs; Google Scholar, ACM DL, IEEE Xplore, SSRN, and paywalled accounting
journals are approximated through general web search plus direct verification fetches of
every candidate's landing page. Given that the LLM-agent literature is overwhelmingly
preprint-first, arXiv+S2 coverage is expected to capture the large majority of relevant
work; the residual risk (missed paywalled accounting-venue papers) is mitigated by D4
venue-name queries and snowballing, and is disclosed in the paper's Limitations section.

## 3. Time window

**January 2023 – July 16, 2026.**
Justification: the LLM-agent era begins for practical purposes with the post-ChatGPT wave
(instruction-tuned LLMs + tool use). Agentic frameworks (ReAct, AutoGPT-style loops,
function calling) appear at scale from early 2023. Pre-2023 work in this space is
overwhelmingly RPA/classical-ML (excluded by E3). Earlier foundational items may be cited
in the paper for context but are not corpus members.

## 4. Inclusion criteria

- **I1:** The work uses or evaluates an LLM-based or agentic AI system, or introduces a benchmark for such systems.
- **I2:** The task is a corporate finance FUNCTION task: financial close / reconciliation / consolidation, FP&A (budget, forecast, variance analysis, management reporting), treasury, corporate tax, investor relations, P2P/O2C, financial reporting/disclosure, spreadsheet financial modeling, controllership.
- **I3:** Peer-reviewed venue OR arXiv/SSRN preprint. Preprints tagged `preprint=yes` in `included_papers.csv`.
- **I4 (window):** first public appearance within Jan 2023 – Jul 16, 2026.

## 5. Exclusion criteria

- **E1:** Pure financial-markets tasks: trading, portfolio management, asset pricing, market prediction.
- **E2:** Markets-facing risk tasks: fraud detection, credit scoring, robo-advisory, AML/KYC (unless the paper ALSO covers an I2 task, in which case include and note scope).
- **E3:** Pre-LLM automation only (RPA, classical ML, OCR-only pipelines without LLM/agent component).
- **E4:** Vendor whitepapers / consulting reports (PwC, Deloitte, BCG, L.E.K., Gartner, vendor blogs). Logged separately as grey literature in `screening.csv` with `category=grey`; usable ONLY for adoption-motivation sentences in the introduction, never as capability evidence.
- **E5:** Personal finance / consumer fintech assistants.
- **E6:** General-purpose agent benchmarks with no finance-function component (e.g., generic web/OS agents) — unless they contain a distinct, non-trivial finance-function task subset, in which case include with a note restricting analysis to that subset.

**Boundary rule (audit):** agentic-audit / AI-in-auditing papers ARE included in the corpus
but tagged `category=audit`. They feed exactly one de-scoping paragraph in Related Work
(existing reviews cover them) and are excluded from the coverage-matrix analysis.

**Boundary rule (general financial QA):** financial-document QA benchmarks (e.g., XBRL/
filings QA) are included only if the tasks map to a CFO-office workflow (e.g., disclosure
drafting, filing analysis for reporting); pure retail-investor QA is E1/E5.

## 6. Search query families

Logged individually in `search_log.csv` (date, database, exact query string, n_results,
n_screened_in). Families (expanded during execution as terms emerge):

- F1: "LLM agent" × {financial close, reconciliation, FP&A, variance analysis, month-end, treasury, corporate tax, financial reporting, accounting, CFO, spreadsheet}
- F2: "agentic AI" × {accounting, corporate finance, financial planning and analysis, controllership}
- F3: "benchmark" × {financial analyst, finance agent, accounting agent, spreadsheet finance, financial modeling}
- F4: venue-scoped: {JETA, IJAIS, Accounting Horizons, Journal of Accounting Literature, ISAFM} × {LLM, generative AI, agent}
- F5: snowballing — for every included paper, inspect its reference list and its citers (Semantic Scholar API `citations`/`references` endpoints); one hop minimum for benchmark papers.
- F6: novelty falsification — explicit searches for any existing survey/position paper on agents for CFO-office/corporate-finance-function/accounting/FP&A/close (see §8).

## 7. Screening procedure

1. **Identification:** all query hits recorded; duplicates removed by arXiv ID/DOI/title match.
2. **Title/abstract screen:** each candidate → `screening.csv` with `include_ta` ∈ {yes,no,maybe} + one-line reason keyed to I/E criteria.
3. **Full-text screen:** candidates passing (2) get their landing page + full text fetched; final `include` decision with reason. Every included paper's ID verified to resolve (title on landing page matches title in corpus CSV).
4. **Corpus entry:** included papers → `included_papers.csv` (bibkey, title, authors, year, venue, arxiv_id/doi, url, category, preprint flag).
5. **Flow accounting:** PRISMA 2020 numbers (identified / deduplicated / screened / full-text assessed / included, with exclusion reasons at each stage) were tracked in the internal `prisma_flow.md` working file (not part of this release); the released `screening.csv` (with its `resolution` column) and `recount.py` reproduce and check these numbers directly.

Single-screener design (one AI screener, human review at Checkpoint 1) — disclosed in the
paper's methodology section. No dual-screener kappa is claimable; the mitigations are the
public search log and the human checkpoint.

## 8. Novelty falsification plan (RQ0, run before corpus finalization)

Search explicitly for surveys/position papers covering agents + {CFO, corporate finance
function, accounting, FP&A, financial close, controllership} in 2025–2026. If any is found
that organizes the CFO-office space (not markets, not audit-only): STOP per the project brief
§2.4, document in the internal progress log (PROGRESS.md, not part of this release), and hand
the pivot decision to the human.

## 9. Expected corpus size

30–80 included papers. If <15 after full-text screening, broaden I2 to include enterprise
document-workflow agents applied to finance documents, and document the amendment here as
protocol v1.1 with date.

## 10. Deviations log

| Date | Deviation | Reason |
|------|-----------|--------|
| 2026-07-16 | D1 (arXiv native search UI and export API) unusable: arxiv.org robots.txt disallows /search and /api for our fetch tool; egress proxy also blocks direct API access. Replaced with domain-restricted web search over arxiv.org. Consequence: `n_results` in search_log.csv = number of search-engine results returned, NOT arXiv's total-hits count. /abs/ and /html/ pages remain directly fetchable, so verification fetches are unaffected. | Technical environment constraint; logged per-query in search_log.csv rows 2-3. |
| 2026-07-16 | Single-session parallel execution: seed verification, sweep, novelty check, and venue-sweep were executed by four parallel AI sub-agents; all extraction traceable to fetched pages. Per-query logs: `search_log.csv` (released) and `notes/audit_overlap.md` (released); the novelty-check and grey-literature per-query logs (`novelty_check.md`, `grey_literature.md`) were internal working files, not part of this release. | Time-boxing within Phase 1 window. |
| 2026-07-21 | D7: targeted post-hoc search on process standardization x agent deployment (user direction), outside the PRISMA screening window; results used as background citations only, no matrix rows added; logged in the internal `standardization_research.md` (not part of this release). | User checkpoint: ground a proposed §7 paragraph before adding it |
