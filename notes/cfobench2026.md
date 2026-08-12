# Can LLM Agents Be CFOs? A Benchmark for Resource Allocation in Dynamic Enterprise Environments

- arXiv ID: 2603.23638
- Authors: Yi Han (Georgia Institute of Technology), Lingfei Qian (The Fin AI), Yan Wang (The Fin AI), Yueru He (Columbia University), Xueqing Peng (The Fin AI), Dongji Feng (California State University), Yankai Chen (McGill / MBZUAI), Haohang Li (Stevens Institute of Technology), Yupeng Cao (Stevens Institute of Technology), Jimin Huang (The Fin AI / University of Manchester), Xue Liu (McGill / MBZUAI), Jian-Yun Nie (Universite de Montreal), Sophia Ananiadou (University of Manchester).
- Status: full-text fetched: Y (https://arxiv.org/html/2603.23638v1, full HTML body incl. abstract, Sections 1-5, Table 2 results, limitations)

## NAMING VERIFICATION (requested check)
The benchmark name **EnterpriseArena IS used**: Section 3 is titled "3 EnterpriseArena" and the abstract states: "We introduce EnterpriseArena, the first benchmark for evaluating agents on long-horizon enterprise resource allocation."

## Summary
EnterpriseArena tests whether LLM agents can perform CFO-style resource allocation under uncertainty in a long-horizon, partially observable enterprise simulator. The simulated firm is a consumer lending company; each episode spans 132 monthly timesteps (11 years) covering multiple economic cycles, built from anonymized firm-level financials, business documents, macro/industry signals, and expert-validated GAAP-guided operating rules. The agent (ReAct framework with memory) must acquire state information through budgeted organizational tools and choose among book_closing, fund_raising_request, and pass actions, under a hard non-negative-cash survival constraint. Evaluation is fully execution-based: binary survival plus a terminal valuation score (revenue multiple + remaining cash - tool-use penalty). Across eleven LLMs (5 runs each) only 16% of runs survive the full horizon; scale does not predict success, with the small Qwen3.5-9B (80% survival, $78.8M score) beating all larger and closed models. Two senior finance professionals serve as a human baseline (100% survival, $152.2M), roughly double the best LLM agent.

## Tasks covered
One simulated enterprise environment (consumer lending firm; init $15M cash, 5,000 borrowers, $10K avg loan, 10.5M shares at $10). 132 monthly decision steps per episode; 16 types of data/documents across economic, industry, and company levels; 11 models x 5 trials; actions: book_closing, fund_raising_request, pass; budgeted information tools.

## Eval method
Execution-based simulation metrics (no LLM judge): (1) Survival — episode terminates with score 0 if cash < 0 at any timestep; (2) Terminal valuation score Score_T = Rev_T x m + Cash_T - lambda * N_tools with m=5, lambda=5,000 (Section 3.5, Eq. 2). Environment validated by two experts (8+ and 14+ years enterprise finance experience).

## Data realism
Semi-synthetic simulator grounded in real data: "transformed firm-level financial data, anonymized business documents, decade-scale macroeconomic and industry signals, and expert-validated operating rules" (Section 1). Anonymization: firms labeled "Company XYZ", dates like "Jan 2xx0"; stochastic noise added per timestep (Section 3.4).

## Agent scope
Long-horizon (132 steps), single agent, tool-use (budgeted org tools), partially observable, dynamic/state-dependent/stochastic environment. Not multi-agent.

## Key numbers (exact quotes)
- 132-month CONFIRMED: "It instantiates CFO-style decision-making in a 132-month enterprise simulator combining firm-level financial data, anonymized business documents, macroeconomic and industry signals, and expert-validated operating rules." (Abstract)
- Survival is 16%, NOT 15%: "Experiments on eleven advanced LLMs show that this setting remains highly challenging: only 16% of runs survive the full horizon, and larger models do not reliably outperform smaller ones." (Abstract)
- "Only 16% of LLM trials survive the entire long-horizon, and 5 out of 11 models fail to survive in any trial. Qwen3.5-9B is the only model to achieve a majority survival rate (80%)." (Section 4.2, RQ1)
- Human vs best agent: "The human baseline achieves 100% survival with a score of $152.2M, nearly double that of the best LLM agent, Qwen3.5-9B ($78.8M, 80% survival)." (Section 4.2, RQ2)
- Horizon config: "Each episode spans T=132 timesteps, corresponding to an 11-year horizon with monthly updates." (Section 4.1)
- Per-model survival (Table 2, 5-round average): Gemini-3.1-Pro 50%; Claude-Haiku-4.5 20%; GPT-5.4 0%; GLM-5 20%; Qwen3.5-397B 20%; DeepSeek-V3.1 0%; Llama-3.3-70B 0%; Mistral-Small-24B 0%; Mixtral-8x7B 0%; Qwen3.5-9B 80%; Llama-3-8B 20%; Average 26% (model-level average; run-level aggregate is 16%).

## Relevance to CFO-office taxonomy
The most direct "CFO agent" benchmark in the corpus: treasury/liquidity management, capital raising (equity/debt), book closing cadence, long-horizon capital allocation under macro cycles. Maps to treasury + corporate finance strategy branches of a CFO-office taxonomy rather than accounting-close mechanics.

## UNVERIFIED items
- The claim "best survival ~15%" is a MISMATCH: the paper says 16% of all runs survive (aggregate), and the best single model survives 80% of its trials. No 15% figure found anywhere (grep for "15%" matched nothing relevant).
- Case study details (Section 4.3) not read in full.
