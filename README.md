# Integrity Code Series — Dashboard

Live status of all repositories in the Integrity Code Series.
Auto-refreshed monthly by a GitHub Actions cron job; can also be triggered manually.

_Last refresh: **2026-11-10 01:18 UTC**_

| # | Repo | Domain | Lang | CI | Latest release | Stars | Last push |
|---|---|---|---|---|---|---|---|
| Week 3 | [`integrity-code-series-week3-f1-lap-simulation`](https://github.com/felipearocha/integrity-code-series-week3-f1-lap-simulation) | F1 lap simulation (six-state model) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week3-f1-lap-simulation/actions/workflows/ci.yml/badge.svg) | [v.0.0.1](https://github.com/felipearocha/integrity-code-series-week3-f1-lap-simulation/releases/tag/v.0.0.1) | 2 | 0d |
| Week 6 | [`integrity-code-series-week6-smartphone-galvanic`](https://github.com/felipearocha/integrity-code-series-week6-smartphone-galvanic) | Smartphone galvanic corrosion (Laplace + BV) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week6-smartphone-galvanic/actions/workflows/ci.yml/badge.svg) | [v1.0.1](https://github.com/felipearocha/integrity-code-series-week6-smartphone-galvanic/releases/tag/v1.0.1) | 1 | 0d |
| Week 7 | [`integrity-code-series-week7-h2-lferw`](https://github.com/felipearocha/integrity-code-series-week7-h2-lferw) | LF-ERW H2 conversion (H diffusion + HA-FCG + B31.12-form MAOP) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week7-h2-lferw/actions/workflows/ci.yml/badge.svg) | [v1.0.1](https://github.com/felipearocha/integrity-code-series-week7-h2-lferw/releases/tag/v1.0.1) | 0 | 0d |
| Week 8 | [`integrity-code-series-week8-creep-fatigue-heater`](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater) | Creep-fatigue 9Cr-1Mo (Norton/Omega + Coffin-Manson) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater/actions/workflows/ci.yml/badge.svg) | [v1.0.1](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater/releases/tag/v1.0.1) | 1 | 0d |
| Week 9 | [`integrity-code-series-week9-cui`](https://github.com/felipearocha/integrity-code-series-week9-cui) | CUI thermohygro-electrochemical (2 PDEs + Butler-Volmer, Strang) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week9-cui/actions/workflows/ci.yml/badge.svg) | [v1.1.1](https://github.com/felipearocha/integrity-code-series-week9-cui/releases/tag/v1.1.1) | 1 | 0d |
| Week 10 | [`integrity-code-series-week10-nnph-scc`](https://github.com/felipearocha/integrity-code-series-week10-nnph-scc) | NNpHSCC full-physics (Chen-Sutherby-Xing + BS 7910) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week10-nnph-scc/actions/workflows/ci.yml/badge.svg) | [v1.0.1](https://github.com/felipearocha/integrity-code-series-week10-nnph-scc/releases/tag/v1.0.1) | 1 | 0d |
| Week 11 | [`integrity-code-series-week11-erosion-corrosion-multiphase`](https://github.com/felipearocha/integrity-code-series-week11-erosion-corrosion-multiphase) | Erosion-corrosion multiphase (NORSOK M-506 + DNV + G119 + API 579) | Python | ![CI](https://github.com/felipearocha/integrity-code-series-week11-erosion-corrosion-multiphase/actions/workflows/ci.yml/badge.svg) | [v1.0.0](https://github.com/felipearocha/integrity-code-series-week11-erosion-corrosion-multiphase/releases/tag/v1.0.0) | 0 | 0d |
| Bonus | [`Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation`](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation) | Vibration-accelerated corrosion (SDOF + BV + Archard) | Python | ![CI](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation/actions/workflows/ci.yml/badge.svg) | [v0.1.1](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation/releases/tag/v0.1.1) | 1 | 0d |
| Bonus | [`synthetic-integrity-digital-twin-piml`](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml) | Physics-informed neural-network surrogate | Python | ![CI](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml/actions/workflows/ci.yml/badge.svg) | [v1.0.1](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml/releases/tag/v1.0.1) | 2 | 0d |
| Bonus | [`integrity-data-foundation`](https://github.com/felipearocha/integrity-data-foundation) | Engineering data validation baseline | Python | ![CI](https://github.com/felipearocha/integrity-data-foundation/actions/workflows/ci.yml/badge.svg) | [v0.1.0](https://github.com/felipearocha/integrity-data-foundation/releases/tag/v0.1.0) | 1 | 0d |

## About

The Integrity Code Series is a set of physics-first integrity simulators by Felipe Rocha.
Each entry is a self-contained Python package. Across the series you will find:

- governing equations documented in code, with sources or `[ASSUMED]` flags
- hand-calculation benchmarks wherever a closed form exists
- Monte Carlo or sensitivity layers over the deterministic models
- a `run_all.py` entry point in every simulator that reproduces its figures

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
