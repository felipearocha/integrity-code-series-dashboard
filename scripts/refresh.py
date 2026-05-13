"""Refresh the Integrity Code Series live dashboard README.

Queries the GitHub API via `gh` CLI, builds a status table for each repo
in the series, and writes the result to README.md. Designed to run unattended
under a GitHub Actions monthly cron.

Author: Felipe Rocha
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

OWNER = "felipearocha"
REPO_DIR = Path(__file__).resolve().parents[1]

SERIES = [
    ("Week 3",  "Integrity-code-series-3",                                                "F1 lap simulation (six coupled ODEs)"),
    ("Week 6",  "Integrity-code-series-week6-smartphone-galvanic",                        "Smartphone galvanic corrosion (Laplace + BV)"),
    ("Week 7",  "integrity_code_series_week7_h2_lferw",                                   "LF-ERW H2 conversion (B31.12 + NACE TM0316)"),
    ("Week 8",  "integrity-code-series-week8-creep-fatigue-heater",                       "Creep-fatigue 9Cr-1Mo (Norton/Omega + Coffin-Manson)"),
    ("Week 9",  "integrity-code-series-week9-cui",                                        "CUI thermohygro-electrochemical (3 PDEs, Strang)"),
    ("Week 10", "integrity-code-series-week-10_nnph_scc",                                 "NNpHSCC full-physics (Chen-Sutherby-Xing + BS 7910)"),
    ("Bonus",   "Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation", "Vibration-accelerated corrosion (SDOF + BV + Archard)"),
    ("Bonus",   "synthetic-integrity-digital-twin-piml",                                  "Physics-informed neural-network surrogate"),
    ("Bonus",   "integrity-data-foundation",                                              "Engineering data validation baseline"),
]


def gh_json(args: list[str]):
    r = subprocess.run(["gh"] + args, capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return {}
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {}


def fetch_repo(slug: str) -> dict:
    data = gh_json(["api", f"repos/{OWNER}/{slug}"])
    if not data:
        return {"missing": True, "slug": slug}
    latest = gh_json(["api", f"repos/{OWNER}/{slug}/releases/latest"])
    return {
        "slug": slug,
        "url": data.get("html_url", f"https://github.com/{OWNER}/{slug}"),
        "stars": data.get("stargazers_count", 0),
        "issues": data.get("open_issues_count", 0),
        "pushed_at": data.get("pushed_at", ""),
        "default_branch": data.get("default_branch", "main"),
        "language": (data.get("language") or "-"),
        "license": (data.get("license") or {}).get("spdx_id", "-"),
        "latest_release": latest.get("tag_name", "-") if isinstance(latest, dict) else "-",
        "release_url": latest.get("html_url", "") if isinstance(latest, dict) else "",
    }


def days_since(iso_ts: str) -> str:
    if not iso_ts:
        return "-"
    try:
        ts = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
    except ValueError:
        return "-"
    return f"{(datetime.now(timezone.utc) - ts).days}d"


def build_row(label: str, info: dict, desc: str) -> str:
    if info.get("missing"):
        return f"| {label} | `{info['slug']}` | (private/unreachable) | - | - | - | - | - |"
    slug = info["slug"]
    ci_badge = f"![CI](https://github.com/{OWNER}/{slug}/actions/workflows/ci.yml/badge.svg)"
    release_cell = (
        f"[{info['latest_release']}]({info['release_url']})"
        if info["latest_release"] != "-" and info["release_url"]
        else info["latest_release"]
    )
    return (
        f"| {label} | [`{slug}`]({info['url']}) | {desc} | "
        f"{info['language']} | {ci_badge} | {release_cell} | "
        f"{info['stars']} | {days_since(info['pushed_at'])} |"
    )


def build_readme() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = [build_row(label, fetch_repo(slug), desc) for label, slug, desc in SERIES]

    lines = [
        "# Integrity Code Series — Dashboard",
        "",
        "Live status of all repositories in the Integrity Code Series.",
        "Auto-refreshed monthly by a GitHub Actions cron job; can also be triggered manually.",
        "",
        f"_Last refresh: **{now}**_",
        "",
        "| # | Repo | Domain | Lang | CI | Latest release | Stars | Last push |",
        "|---|---|---|---|---|---|---|---|",
        *rows,
        "",
        "## About",
        "",
        "The Integrity Code Series is a set of physics-first integrity simulators by Felipe Rocha.",
        "Each entry is a self-contained Python package with:",
        "",
        "- governing PDEs/ODEs documented in code with `[SOURCE: Author Year]` tags",
        "- analytical benchmarks against textbook constants",
        "- a Monte Carlo or sensitivity layer over the deterministic model",
        "- a `run_all.py` entry point that reproduces every figure",
        "",
        "## Refresh manually",
        "",
        "```bash",
        "python scripts/refresh.py",
        "```",
        "",
        "Or trigger the workflow:",
        "",
        "```bash",
        "gh workflow run refresh.yml -R felipearocha/integrity-code-series-dashboard",
        "```",
        "",
        "## License",
        "",
        "MIT - Felipe Rocha",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    readme = REPO_DIR / "README.md"
    readme.write_text(build_readme(), encoding="utf-8")
    print(f"Wrote {readme} ({readme.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
