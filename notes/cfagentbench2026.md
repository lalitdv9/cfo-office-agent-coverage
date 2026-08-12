# CFAgentBench: A Reproducible Environment and Benchmark for Autonomous Construction-Finance Agents

- arXiv ID: 2606.22000
- Authors: Rishi Srivastava (sole author; no affiliation listed in the fetched HTML; paper dated June 18, 2026)
- Status: full-text fetched: Y (https://arxiv.org/html/2606.22000v1, full HTML body incl. abstract, Sections 1-6, task table, metrics, experiments)

## IMPORTANT SCOPE NOTE
"CF" here means **construction finance**, not CFA/corporate finance generally. The target is "a CFO/controller-class agent that must operate across the real software stack a US construction finance team runs" (Abstract).

## Summary
CFAgentBench is a self-hostable, executable environment plus benchmark for autonomous construction-finance agents operating across a mock enterprise software stack: ERP, project management, email, documents, pay applications, payroll, certified payroll, lien waivers, and bank/treasury portals. It contains 1,014 machine-gradeable task specifications across 8 domains and 77 families, every family grounded in a real practitioner source (CFMA forum threads, NAHB threads, a construction-finance podcast, customer emails/calls, standards docs); of these, 40 tasks (54 with the project-management extension) are compiled into oracle-validated executable evaluators, which is what the paper actually reports on. The environment comprises 35 mock applications collapsing into 9 archetypes under a uniform app contract (seed/serve/snapshot/reset/state_diff/guarded_calls), and grading is functional correctness: deterministic state diff, forbidden-side-effect checks, and required-output regexes, with an LLM judge used only for narrative reply quality and never as reward. A signature design choice is the money-movement guard: 278 instances embed a payment/payroll/e-signature/e-filing step where the correct behavior is to stop and stage for human approval — executing even the correct transaction fails the task. A first sweep of three open-weight models (ReAct-style tool-use, k=5, temperature 0, total cost $5.14) shows the best single-shot agent, DeepSeek-V3.1, at pass1=0.67 collapsing to pass5=0.38, evidence that single-attempt accuracy overstates deployable reliability. An oracle policy scores 1.0 on all forty tasks and a no-op baseline scores 0.00, validating solvability and determinism.

## Tasks covered
1,014 task instances, 8 domains, 77 families. Domain distribution (Table 3, Section 4): AP & Procurement 243; Reporting & Compliance 159; Project Accounting 157; Cross-system 116; Payroll & HR 112; Billing 93; Cash & Treasury 70; GL & Close 64. Splits: public dev 142, public test 569 (public split n=711), private held-out 303 ("CFAgentBench-Pro"). Difficulty 1-4 by equivalent human time: 94/395/448/77 instances. Executable today: 40 oracle-validated tasks (54 with PM extension); the rest are released as gradeable specifications awaiting evaluator compilation. Example executable families: ETC-forecast updates, owner pay-application drafting, invoice coding and COI-driven payment holds, certified-payroll WH-347 validation, sub-contract accruals, positive-pay resolution, 1099-NEC preparation, ERP invoice sync.

## Eval method
Execution-based functional correctness: deterministic expected_state_diff plus forbidden_state_diffs checks (AppWorld pattern) plus required-output regexes; layered grader with rubric (primary + partial-credit weights). Money-movement guard is itself scored behavior. LLM judge only for narrative reply quality, never a reward signal. Metrics: pass^1 and pass^k (fraction succeeding on every one of k runs), k=5 headline; oracle replay validates each evaluator (admitted only if oracle scores 1.0); trivial no-op baseline floors the benchmark at 0.00.

## Data realism
Mock/synthetic executable environment (35 mock apps reconciled to one "Company-A" book), but task provenance is real: "The set is grounded, not synthetic trivia. Every family traces to a real source: 597 instances seed from real CFMA Connection Cafe threads ...; 218 from a construction-finance agentic-dataset plan document; 83 from Finance at the Jobsite podcast episodes; 81 from public standards and construction-software vendor documentation (AIA G702/G703, IRS 1099-NEC, ASC 842 ...); 28 from Beiing Human customer emails and NAHB builder-forum threads; 6 from Fathom call transcripts; and 1 from a CRM record." (Section 4.1)

## Agent scope
Multi-step, multi-application tool-use workflows (single agent, ReAct-style, native function-calling, fixed step budget); cross-system tasks span up to 4 apps (e.g., Procore, Sage Intacct, Box, Outlook); includes human-in-the-loop staging behavior (money guard). Not multi-agent; not long-horizon simulation.

## Key numbers (exact quotes; MathML spacing artifacts in source cleaned)
- Task counts: "CFAgentBench contains 1,014 machine-gradeable task specifications spanning 8 domains and 77 task families" (Abstract; body: "CFAgentBench v1 contains 1,014 task instances across 8 domains and 77 families." Section 4)
- Executable subset: "a self-validated subset of 40 tasks (54 with the project-management extension) is compiled into oracle-validated executable evaluators — the runnable suite this paper reports on" (Abstract)
- Money guard: "A distinguishing design principle is a money-movement guard: 278 instances embed a payment, payroll, e-signature, or e-filing step where the correct behavior is to stop and stage for human approval; executing even the correct transaction fails the task." (Abstract)
- Headline result: "In a first three-model open-weight sweep (k=5) on a forty-task oracle-validated subset, the strongest agent reaches pass1 = 0.67 but only pass5 = 0.38 — losing 43% of its successes when required to repeat them, under fixed (temperature-0) decoding" (Abstract)
- Per-model: "The best pass1 agent, DeepSeek-V3.1, drops from 0.67 to pass5 = 0.38 — losing 43% of its successes when required to repeat them five times — whereas the two Qwen agents lose less (Qwen2.5: 0.54 -> 0.40; Qwen3: 0.45 -> 0.30)." (Section 6.2, Findings)
- Validation: "the oracle scores pass1 = 1.0 and pass5 = 1.0 ... and 1.0 across all forty tasks"; "the trivial no-op policy ... scores 0.00 on all forty tasks" (Section 6.1)
- Cost: "The combined three-model, 600-run sweep cost $5.14." (Section 6.2)
- Power design: "the public test set (n=569) would give a model's overall accuracy a 95% Wilson half-width of +/-4.1%" (Section 5.4); at n=40 executable scale the half-width is about +/-0.15.

## Relevance to CFO-office taxonomy
Direct controller/CFO-office operational coverage in a vertical (construction): AP/procurement, billing (pay apps), payroll and certified payroll compliance, GL & close accruals, cash & treasury (positive pay), reporting & compliance (1099-NEC), and cross-system ERP sync. The money-movement staging guard is a concrete safety pattern for CFO-office agent taxonomies.

## UNVERIFIED items
- Author affiliation (not present in fetched HTML).
- Models evaluated are only 3 open-weight models on n=40; between-model rankings explicitly labeled within-noise by the authors.
- Full Tables 5/6 per-domain numbers (not read line-by-line beyond quoted findings).
- Quoted abstract/body sentences contain HTML-conversion spacing artifacts in the raw fetch (e.g., "spanning8 domains", "and77 families"); numbers verified, spacing normalized here.
