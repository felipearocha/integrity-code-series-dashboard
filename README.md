# Integrity Code Series — Dashboard

Live status of all repositories in the Integrity Code Series.
Auto-refreshed monthly by a GitHub Actions cron job; can also be triggered manually.

_Last refresh: **2026-05-13 05:02 UTC**_

| # | Repo | Domain | Lang | CI | Latest release | Stars | Last push |
|---|---|---|---|---|---|---|---|
| Week 3 | [`Integrity-code-series-3`](https://github.com/felipearocha/Integrity-code-series-3) | F1 lap simulation (six coupled ODEs) | Python | ![CI](https://github.com/felipearocha/Integrity-code-series-3/actions/workflows/ci.yml/badge.svg) | [v.0.0.1](https://github.com/felipearocha/Integrity-code-series-3/releases/tag/v.0.0.1) | 1 | 0d |
| Week 6 | [`Integrity-code-series-week6-smartphone-galvanic`](https://github.com/felipearocha/Integrity-code-series-week6-smartphone-galvanic) | Smartphone galvanic corrosion (Laplace + BV) | Python | ![CI](https://github.com/felipearocha/Integrity-code-series-week6-smartphone-galvanic/actions/workflows/ci.yml/badge.svg) | [v1.0.0](https://github.com/felipearocha/Integrity-code-series-week6-smartphone-galvanic/releases/tag/v1.0.0) | 1 | 0d |
| Week 7 | [`integrity_code_series_week7_h2_lferw`](https://github.com/felipearocha/integrity_code_series_week7_h2_lferw) | LF-ERW H2 conversion (B31.12 + NACE TM0316) | Python | ![CI](https://github.com/felipearocha/integrity_code_series_week7_h2_lferw/actions/workflows/ci.yml/badge.svg) | [v1.0.0](https://github.com/felipearocha/integrity_code_series_week7_h2_lferw/releases/tag/v1.0.0) | 0 | 0d |
| Week 8 | [`integrity-code-series-week8-creep-fatigue-heater`](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater) | Creep-fatigue 9Cr-1Mo (Norton/Omega + Coffin-Manson) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater/actions/workflows/ci.yml/badge.svg) | [v1.0.0](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater/releases/tag/v1.0.0) | 0 | 0d |
| Week 9 | [`integrity-code-series-week9-cui`](https://github.com/felipearocha/integrity-code-series-week9-cui) | CUI thermohygro-electrochemical (3 PDEs, Strang) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week9-cui/actions/workflows/ci.yml/badge.svg) | [v1.1.0](https://github.com/felipearocha/integrity-code-series-week9-cui/releases/tag/v1.1.0) | 1 | 0d |
| Week 10 | [`integrity-code-series-week-10_nnph_scc`](https://github.com/felipearocha/integrity-code-series-week-10_nnph_scc) | NNpHSCC full-physics (Chen-Sutherby-Xing + BS 7910) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week-10_nnph_scc/actions/workflows/ci.yml/badge.svg) | [v1.0.0](https://github.com/felipearocha/integrity-code-series-week-10_nnph_scc/releases/tag/v1.0.0) | 1 | 0d |
| Bonus | [`Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation`](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation) | Vibration-accelerated corrosion (SDOF + BV + Archard) | Python | ![CI](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation/actions/workflows/ci.yml/badge.svg) | [v0.1.0](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation/releases/tag/v0.1.0) | 1 | 0d |
| Bonus | [`synthetic-integrity-digital-twin-piml`](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml) | Physics-informed neural-network surrogate | Python | ![CI](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml/actions/workflows/ci.yml/badge.svg) | [v1.0.0](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml/releases/tag/v1.0.0) | 1 | 0d |
| Bonus | [`integrity-data-foundation`](https://github.com/felipearocha/integrity-data-foundation) | Engineering data validation baseline | Python | ![CI](https://github.com/felipearocha/integrity-data-foundation/actions/workflows/ci.yml/badge.svg) | [v0.1.0](https://github.com/felipearocha/integrity-data-foundation/releases/tag/v0.1.0) | 1 | 0d |

## About

The Integrity Code Series is a set of physics-first integrity simulators by Felipe Rocha.
Each entry is a self-contained Python package with:

- governing PDEs/ODEs documented in code with `[SOURCE: Author Year]` tags
- analytical benchmarks against textbook constants
- a Monte Carlo or sensitivity layer over the deterministic model
- a `run_all.py` entry point that reproduces every figure

## Refresh manually

```bash
python scripts/refresh.py
```

Or trigger the workflow:

```bash
gh workflow run refresh.yml -R felipearocha/integrity-code-series-dashboard
```

## License

MIT - Felipe Rocha
