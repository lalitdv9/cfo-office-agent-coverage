# BigFinanceBench: A Workflow-Grounded Benchmark for Financial-Research Agents

- arXiv ID: 2606.03829
- Authors: Alex Wang (1,*), Georg Meinhardt (1,*), Jacob Katz (1), Joseph H. Kim (2,+), Pratyush K. Chaudhary (1), Chase Blagden (2,+), Eric Xu (1). Affiliations: (1) Rogo, (2) OpenAI. (* equal contribution; + work done while at Rogo.)
- Status: full-text fetched: Y (https://arxiv.org/html/2606.03829v1, full HTML body incl. abstract, Sections 1-5, setup/results, appendix headings and Table 3 leaderboard excerpt)

## Summary
BigFinanceBench is a 928-item, expert-authored benchmark of open-ended financial-research tasks graded at the resolution of the analyst derivation, not just the final answer. Questions were written by 52 practicing financial-research subject-matter experts (mostly current/former investment bankers and PE investors) and independently audited by a 12-person reviewer panel between September 2025 and March 2026. Each item pairs a ground-truth reference answer with a binary, atomic, point-weighted rubric (15,656 criteria; 36,241 total points) covering entity identification, source selection, line-item retrieval, accounting adjustment, formula construction, and synthesis. Agents run in a common open-book ReAct harness (50-step budget) with a minimal public-source tool set (web_search, edgar_search, fetch_url, python_exec), and two independent LLM judges (Gemini 3.1 Pro Preview and Claude Opus 4.7) grade each visible trajectory against the rubric, with three trials per question and very high inter-judge agreement (Cohen's kappa 0.952-0.973). Across ten frontier and open-weight agents the best system reaches only 58.8% rubric score (GPT-5.5 per Appendix Table 3), with the top three closed models within 0.3pp of each other but specializing in different workflows. Rubric scores systematically exceed final-answer accuracy (mean gap 15.95pp), showing partial workflow progress that final-answer grading discards.

## Tasks covered
928 open-ended, multi-source, assumption-dependent financial-research questions ("workflow-grounded"); requires chaining retrieval, normalization, accounting judgment, and calculation over public evidence (SEC filings and other public sources). 15,656 rubric criteria, 36,241 total rubric points. 3 trials/question -> 2,784 expected (question, trial) records per model.

## Eval method
Rubric + LLM-judge: point-weighted per-item rubrics graded by two independent LLM judges over the full visible agent trajectory (tool calls, outputs, calculations, final answer). Primary metric: rubric score (earned/total points, macro-averaged); secondary: final-answer accuracy and unweighted criterion pass rate. Human experts author/audit items but do not grade runs.

## Data realism
Real public documents: agents must find and use primary sources themselves (SEC filings via edgar_search, public web). Questions authored from real analyst practice; deliberately difficult (authors pre-tested against frontier agents and recorded failure modes). 81% of items (748/928) carry substantive reviewer feedback/edits in preserved review logs.

## Agent scope
Single-agent, multi-step tool-use research workflow (open-book ReAct, 50-step budget, python sandbox). Not multi-agent, not long-horizon simulation.

## Key numbers (exact quotes)
- 928 items CONFIRMED: "We introduce BigFinanceBench, a 928-item expert-authored benchmark of open-ended financial-research tasks in which each item pairs a ground-truth reference answer with a point-weighted rubric that decomposes the derivation into independently checkable steps." (Abstract)
- 36,241 points CONFIRMED: "Across 36,241 rubric points, the benchmark supports partial-credit evaluation and localization of failures across the analyst workflow." (Abstract); also "yielding 15,656 criteria and 36,241 total points for partial-credit evaluation of analyst derivations." (Section 1, Contributions)
- 58.8% best CONFIRMED: "Evaluating ten current frontier and open-weight agents, we find substantial headroom: the best system reaches only 58.8% rubric score, final-answer accuracy is a useful but lossy proxy for derivation quality, and model capability varies non-uniformly across financial workflows." (Abstract). Best system identified as GPT-5.5 at 58.8% in Appendix C, Table 3.
- Authors/reviewers: "The dataset contains 928 items authored by 52 financial-research subject-matter experts ... A separate panel of 12 reviewers audited the items before inclusion." (Section 3.1)
- Ceiling: "the best systems remain below 60% rubric score and below 45% final-answer accuracy." (Section 4.2)
- Process-vs-outcome gap: "Every model sits above the equality line, with a mean rubric-minus-final-answer gap of 15.95 pp, Pearson r=0.94 across models, and 41 of 45 pairwise rankings concordant." (Section 4.2)
- Judges: "two independent judges (Gemini 3.1 Pro Preview and Claude Opus 4.7) receive the question, visible agent trace, reference answer, and full point-weighted rubric" (Section 4.1); "Inter-judge agreement is high (Cohen's kappa in [0.952, 0.973] ...)." (Section 4.1)
- Routing: "a simple router using observable (workflow, source) features improves over the best single model by 7.6% relative rubric gain and 10.7% relative answer-accuracy gain." (Section 4.2)

## Relevance to CFO-office taxonomy
Financial research / analysis workflows (sell-side/buy-side analyst work: sourcing filings, accounting adjustments, metric derivation). Maps to the financial analysis and reporting-interpretation branch of a CFO-office taxonomy rather than transaction processing or close; its rubric-over-derivation methodology is a template for auditable evaluation of CFO-office agents.

## UNVERIFIED items
- Full 10-model leaderboard values (Appendix Table 3 only partially visible in fetched text; only GPT-5.5 = 58.8% rubric / 44.3% next cell confirmed).
- Workflow-family breakdown counts (Appendix F statistics not read).
