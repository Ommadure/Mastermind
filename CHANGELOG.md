# Changelog

All notable changes to the **Mastermind (`mastermind`)** skill package are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.1] - 2026-11-09

### Added
- **Interactive HTML Visualization (`scripts/visualization.py`)**: New standalone module generating clean, accessible HTML reports with Chart.js visualizations designed for universal readability.
  - Clear verdict badge (GREEN/AMBER/RED) with plain-language meaning
  - Key metrics cards: Expected Value, EVPI, Skill Half-Life, Durability Score
  - Three intuitive charts: Payoffs by Scenario (bar), Risk vs Reward (scatter), Forecast Uncertainty (range bars)
  - Options comparison table with plain-language recommendations
  - Monte Carlo simulation results table
  - Key insights boxes: Missing Data Impact, Survivorship Bias, Hidden Factors
  - 3-phase learning roadmap with time estimates and concrete checkpoints
  - Crucible Gate: First-principles test + hands-on drill
  - Auto dark/light theme (follows system preference), responsive, print-friendly
- **CLI Integration**: Added `--html` argument to `risk_and_trend_analyzer.py` for generating HTML reports alongside JSON output and Matplotlib charts.
- **Zero-Dependency Architecture**: HTML reports use Chart.js via CDN — no additional Python packages required.

### Changed
- Updated `scripts/risk_and_trend_analyzer.py` version to 2.0.1
- Enhanced main() to accept `--html` flag and integrate with visualization module
- Maintained full backward compatibility — all existing JSON output and Matplotlib charts work unchanged

## [2.0.0] - 2026-11-09

### Added
- **MIT License (`LICENSE`)**: Added standard permissive MIT license so the skill can be freely shared, forked, and installed by any user.
- **Comprehensive User & Contributor Documentation (`README.md`)**: Documented the 5-stage pipeline, theoretical foundations, CLI usage, installation instructions for other users, and trigger prompts.
- **Modular Reference Library (`references/`)**:
  - `references/epistemic-risk-framework.md`: Full mathematical and qualitative rubrics for Abraham Wald's Survivorship Filter, Expected Value of Perfect Information (EVPI), 4-Regime Prediction Error stress-testing, Nassim Taleb's Convexity Ratio, and Jeff Bezos's Type 1 / Type 2 Door reversibility.
  - `references/trend-forensics-and-chart-reading.md`: Structured checklist for decomposing uploaded analytic charts, scoring Gartner Hype Cycle and Wardley Evolution positions, computing the Lindy Durability Score, and issuing `GREEN` / `AMBER` / `RED` obsolescence warnings.
  - `references/zero-cost-tier1-sources.md`: Curated, verified directory of 100% free Tier-1 primary sources across Software/CS, AI/Math, Engineering, Finance/Economics, Natural Sciences, and Design/Writing.
  - `references/deliberate-practice-pedagogy.md`: Ultralearning 80/20 deconstruction (Concepts, Facts, Procedures) and K. Anders Ericsson's Deliberate Practice Crucible testing loop.
- **Standardized Report Blueprint (`assets/decision-and-mastery-report-template.md`)**: Reusable Markdown template for consistent, high-clarity audits and roadmaps.
- **Worked Case Studies (`examples/sample-mastermind-walkthroughs.md`)**: Three complete end-to-end examples covering GREEN, AMBER, and RED trend verdicts.
- **Upgraded Quantitative Risk & Trend Engine (`scripts/risk_and_trend_analyzer.py`)**: Added Monte Carlo prediction-error perturbation (1,000-trial simulation), automated Trend Warning Badge computation (`GREEN` / `AMBER` / `RED`), 3-panel Matplotlib diagnostic chart generation, and a built-in `--selftest` suite.

## [1.0.0] - 2026-11-09

### Added
- Initial release of `mastermind` with core 5-step workflow, basic epistemic risk rubric, and EV/EVPI analyzer script.
