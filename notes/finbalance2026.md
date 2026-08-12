# FinBalance: A Multi-Document Accounting Reconciliation Benchmark

- arXiv ID: 2606.15949
- Authors: Sasank Tumpati (1,*), Devansh Agarwal (1,*), Ayush Kedia (1), Arjun Neekhra (1), Murari Mandal (2), Krishna Garg (3), Yash Sinha (1), Suman Gupta (1), Dhruv Kumar (1). Affiliations: (1) BITS Pilani, (2) KIIT Bhubaneswar, (3) University of Oxford. (* equal contribution.)
- Status: full-text fetched: Y (https://arxiv.org/html/2606.15949v1, full HTML body incl. abstract, Sections 1-8, results, limitations headings)

## Summary
FinBalance evaluates whether LLMs can do the step that precedes financial statements: reconciling a bundle of OCR'd source documents (invoices, bank statements, contracts, schedules, distractors, plus an opening trial balance) into cited journal entries, a final balance sheet, and an inconsistency flag/code. The benchmark is synthetic by construction but its accounting knowledge is human-authored: experts define business scenarios, document schemas, chart of accounts, policies, tax/FX treatments, distractor and contradiction templates, and a deterministic double-entry ledger generator composes records with exact, replayable ground truth. Coverage spans eight industries, three period types, five difficulty levels, and a 23-code inconsistency taxonomy; the main evaluation split has 710 records (480 standard + 230 forced-inconsistency), with a 143-record compact split for ablations. Two complementary metrics separate self-reporting from entry quality: BSexact (model's own balance sheet vs ground truth) and BSrecon (balance sheet obtained by replaying the model's entries through the ledger). Six LLMs reach at most 46% BSexact; four of six show a 26-41pp aggregation gap between BSrecon and BSexact, and 52% of otherwise-correct entries cite the wrong documents. A one-turn ledger-feedback diagnostic raises BSexact by +30 to +33pp but degrades inconsistency detection by up to -52pp on smaller models. Design and labels were validated by practicing finance professionals at two major US investment banks and a certified accountant.

## Tasks covered
710-record main evaluation split: 480 standard reconciliation records (4 per industry-period-difficulty cell: 8 industries x 3 period types x 5 difficulty levels) + 230 forced-inconsistency records (10 per each of 23 codes). 143-record compact ablation split (120 standard + 23 forced-inconsistency). Output per record: cited journal entries (JSON), final balance sheet, inconsistency flag/code/justification. Concept flags: ASC 606 revenue recognition, leases, deferred tax, asset disposals, FX remeasurement, multi-jurisdictional sales tax, exemptions, rollforwards.

## Eval method
Deterministic exact-match / execution-based: BSexact (exact match at 0.01 tolerance), BSrecon (deterministic ledger replay of the model's own entries), strict/lenient posting-level entry matching (debit account, credit account, rounded amount, sorted doc_refs), inconsistency-code match rate over 230 negative controls, parse rate. No LLM judge. Human expert validation of the benchmark itself (75 records reviewed by IB professionals; 25 double-reviewed with 100% collapsed agreement on verdict; full 143-record compact split reviewed by a certified accountant, zero rejections). Bootstrap over 5000 resamples for uncertainty.

## Data realism
Synthetic/templated with human-authored accounting specifications ("FinBalance is synthetic by construction, but its accounting knowledge is human-authored rather than model-invented," Section 1). PDF-style rendered documents with OCR text; distractors are neutralized but visually plausible. Not real company documents. Generator is seed-deterministic and released for fresh stratified samples.

## Agent scope
Primarily single-turn long-context structured generation (document bundle -> JSON output). Ablations extend to light tool use: passive tools (calculators, search; rarely used by models), best-of-3 sampling, and a one-revision-turn ledger-feedback loop. Not multi-step workflow or multi-agent.

## Key numbers (exact quotes)
- Best score: "On a 710-record evaluation split, six contemporary LLMs reach at most 46% exact final-balance-sheet accuracy." (Abstract); "the highest BSexact score is 46%" (Section 5). Best model: "GPT-5 is comparatively self-consistent (46.5% BSexact, 46.3% BSrecon)" (Section 5).
- Aggregation gap: "Four models show a 26-41 pp gap between BSexact, the model's reported balance sheet, and BSrecon, the balance sheet obtained by replaying its entries through our ledger." (Abstract); per-model: "DeepSeek Chat reaches 0.473 BSrecon but only 0.067 BSexact, a 40.6 pp aggregation gap. Gemini 3 Flash (+31.3 pp), Qwen 3 235B (+29.0 pp), and Claude Haiku 4.5 (+26.3 pp) show the same pattern." (Section 5)
- Document linking: "on the anchor ablation split, 52% of journal entries with correct account and amount cite the wrong documents, a rate that barely moves under explicit citation-pressure prompting (-1.4 pp)" (Section 1)
- Ledger feedback: "BSexact rises by +30 to +33 pp across three model families; the same tool feedback also reveals a trade-off, degrading inconsistency-code detection by -13 to -52 pp on smaller models." (Abstract); "Gemini 3 Flash loses -13 pp (not significant), while Qwen 3 235B loses -17 pp and Claude Haiku 4.5 loses -52 pp." (Section 6/5, Figure 3 discussion)
- Split composition: "The main evaluation split used in this paper contains 710 records: four standard records for every industry-period-difficulty cell (480 total) and ten forced-inconsistency records for every negative-control code (230 total)." (Section 3, Coverage)
- Models evaluated: "We evaluate six contemporary LLMs: Gemini 3 Flash (anchor; full ablation matrix), GPT-5 (low reasoning effort), Claude Haiku 4.5, Grok-4.3, Qwen 3 235B, and DeepSeek Chat." (Section 4)

## Relevance to CFO-office taxonomy
Core controllership/accounting-close work: journal-entry preparation with document support, balance-sheet aggregation, reconciliation, and contradiction detection. Maps to the record-to-report and reconciliation branch of a CFO-office taxonomy; also a rare benchmark of "refuse to fabricate a balanced statement when documents contradict."

## UNVERIFIED items
- Analysis-section per-industry/error-taxonomy breakdowns (Section 6 details beyond quoted parts not fully read).
- Total dataset size beyond the 710/143 evaluation splits (generator can produce unlimited records; no fixed corpus size stated in fetched portions).
