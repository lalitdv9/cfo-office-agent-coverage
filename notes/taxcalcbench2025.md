# TaxCalcBench (near-miss cite-and-distinguish note)
- arXiv:2507.16126 (Column Tax). Verified via WebSearch + arXiv/GitHub 2026-07-16.
- Scope: PERSONAL income tax — "calculate personal income tax returns"; 51 pairs of taxpayer inputs (W-2s etc.) → correct Form 1040 in IRS XML. Finding: SOTA models correctly calculate "less than a third" of returns even on a simplified set.
- Distinction from our leaf 4.1 (tax provision): 4.1 = CORPORATE current/deferred income-tax provision (ASC 740/IAS 12) reconciling to the return AND the financial statements. TaxCalcBench = individual Form-1040 calculation (consumer/personal). It does NOT fill 4.1; it shows the tax *leaf* attracts benchmarks while the corporate-provision leaf stays empty, and its <1/3 result reinforces the reliability theme.
