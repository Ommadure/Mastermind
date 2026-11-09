# Mastermind (`mastermind`) — v2.0.1

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Spec: Agent Skill](https://img.shields.io/badge/Skill_Format-Multi--File_v2.0-emerald.svg)](./SKILL.md)
[![Cost: 100% Free Resources](https://img.shields.io/badge/Pedagogy-100%25_Free_Tier--1_Sources-teal.svg)](./references/zero-cost-tier1-sources.md)
[![Visualization: Interactive HTML](https://img.shields.io/badge/Visualization-Interactive_HTML_Report-orange.svg)](./scripts/visualization.py)

**Mastermind** is an open-source, MIT-licensed AI Agent Skill designed for **rational decision-making under deep uncertainty**, **quantitative trend and chart forensics**, and **universal zero-cost skill acquisition**.

Most AI assistants fail at strategic mentorship for three reasons:
1. **Sycophancy & False Hope**: They validate whatever skill, tool, or plan a user proposes, ignoring opportunity cost and realistic failure rates.
2. **WYSIATI Bias (*What You See Is All There Is*)**: They treat visible data and survivor stories as the entire truth while ignoring missing data, silent dropouts, and unobserved confounders.
3. **Conflating Forecast Probability with Consequence Asymmetry**: They rely on fragile point-estimate predictions about the future instead of evaluating how badly a 40% forecast error hurts the user.

**Mastermind** replaces passive agreement with a rigorous, 5-stage epistemic and pedagogical engine.

**New in v2.0.1**: Interactive HTML visualization reports with Chart.js — executive dashboard, animated trend badges, risk matrices, Monte Carlo charts, and learning roadmaps. Dark/light theme, mobile-responsive, print-friendly.

## Table of Contents

1. [Core Capabilities](#core-capabilities)
2. [Repository & Directory Structure](#repository--directory-structure)
3. [Theoretical Foundations](#theoretical-foundations)
4. [The 5-Stage Mastermind Execution Pipeline](#the-5-stage-mastermind-execution-pipeline)
5. [Quantitative Risk & Trend Analyzer CLI (`scripts/risk_and_trend_analyzer.py`)](#quantitative-risk--trend-analyzer-cli-scriptsrisk_and_trend_analyzerpy)
6. [Installation & Sharing Guide for Other Users](#installation--sharing-guide-for-other-users)
7. [Trigger Examples & Usage Prompts](#trigger-examples--usage-prompts)
8. [Contributing & Extending](#contributing--extending)
9. [License](#license)

## Core Capabilities

* **Trend & Obsolescence Warning Radar (`GREEN` / `AMBER` / `RED`)**: Audits uploaded analytic charts and live market signals to classify any technology or skill across the Gartner Hype Cycle, Wardley Evolution Axis, and Lindy Durability scale—warning you *before* you invest ratusan of hours into a dying or commoditized wrapper.
* **Shadow Data & EVPI Audit**: Uses Abraham Wald's survivorship-bias framework and Expected Value of Perfect Information (EVPI) math to identify what data is *missing* and convert critical unknowns into 24-to-72-hour micro-experiments.
* **Prediction-Error & Consequence Asymmetry Engine**: Stress-tests decisions across four regimes (**Bull**, **Base**, **Bear / Forecast Wrong by 40%+**, and **Tail Shock**) and evaluates payoffs using Nassim Taleb's Convexity ratio and Jeff Bezos's Type 1 / Type 2 Door reversibility test.
* **100% Free, Tier-1 Primary Source Routing**: Strictly bans paywalled courses, paid bootcamps, and affiliate fluff. Routes learners exclusively to verified, zero-cost primary documentation, open university courseware (MIT OCW, Harvard CS50, Stanford, CMU), peer-reviewed papers, and open-source textbooks.
* **Ultralearning + Deliberate Practice Crucible**: Deconstructs any skill into its 80/20 Concepts, Facts, and Procedures, enforcing mastery through unassisted recall, edge-case debugging, and verification gates.

## Repository & Directory Structure

```text
mastermind/
├── SKILL.md                                     # Core agent instructions, triggers, and 5-stage workflow
├── LICENSE                                      # Permissive MIT License for open sharing and modification
├── README.md                                    # Comprehensive human & contributor documentation
├── CHANGELOG.md                                 # Version history and architectural release notes
├── references/
│   ├── epistemic-risk-framework.md              # Shadow Data, EVPI math, Convexity, and Reversibility rubrics
│   ├── trend-forensics-and-chart-reading.md     # Analytic chart forensics, Hype Cycle, Wardley, and Lindy scoring
│   ├── zero-cost-tier1-sources.md               # Verified directory of 100% free Tier-1 learning repositories
│   └── deliberate-practice-pedagogy.md          # Ultralearning 80/20 deconstruction and Crucible testing rules
├── assets/
│   └── decision-and-mastery-report-template.md  # Standardized Markdown template for audits and roadmaps
├── examples/
│   └── sample-mastermind-walkthroughs.md        # 3 complete reference walkthroughs (GREEN, AMBER, RED verdicts)
└── scripts/
    └── risk_and_trend_analyzer.py               # Deterministic Python CLI + Monte Carlo + Matplotlib chart generator
```

## Theoretical Foundations

Mastermind synthesizes eight peer-reviewed and field-tested frameworks into a single operational protocol:

| Domain | Framework | Pioneers / Origin | Operational Role in Mastermind |
| :--- | :--- | :--- | :--- |
| **Missing Data Forensics** | Survivorship & Silent Evidence Filter | Abraham Wald (Statistical Research Group) | Identifies unobserved failures, dropout base rates, and selection bias in visible charts. |
| **Value of Information** | Expected Value of Perfect Information (EVPI) | Howard Raiffa & Decision Analysis | Quantifies the maximum value of resolving a missing variable before committing resources. |
| **Probabilistic Forecasting** | Superforecasting & Outside-View Base Rates | Philip E. Tetlock & Dan Gardner | Anchors predictions in historical base rates rather than inside-view wishful thinking. |
| **Failure Pre-Emption** | Prospective Hindsight (Pre-Mortem Analysis) | Gary Klein | Assumes the learning plan or project has failed 6 months from now and works backward to lock in mitigations. |
| **Asymmetric Payoffs** | Antifragility, Convexity & Lindy Effect | Nassim Nicholas Taleb | Prioritizes capped-downside / uncapped-upside options and separates durable fundamentals from fragile fads. |
| **Decision Velocity** | Type 1 (One-Way) vs. Type 2 (Two-Way) Doors | Jeff Bezos | Matches analytical rigor to the cost of reversing the decision. |
| **Strategic Evolution** | Wardley Mapping & Hype Cycle Forensics | Simon Wardley & Gartner | Maps where a skill sits on the evolution curve from Genesis to Commodity/Utility. |
| **Expertise Acquisition** | Ultralearning & Deliberate Practice | Scott H. Young & K. Anders Ericsson | Replaces passive reading with 80/20 metalearning maps and high-friction diagnostic drills. |

## The 5-Stage Mastermind Execution Pipeline

```text
[User Prompt / Uploaded Chart]
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ STAGE 1: Operational Constraint & Baseline Audit         │
│ • Weekly hours, skill floor, deadline, ruin threshold    │
└──────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ STAGE 2: Trend Forensics & Obsolescence Warning Radar    │
│ • Chart decomposition, Hype vs. Reality, Lindy Score     │
│ • Issues Badge: [GREEN: Master] [AMBER: 80/20] [RED: Cut]│
└──────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ STAGE 3: Epistemic & Asymmetric Risk Engine              │
│ • Known Base Rates + Shadow Data Audit + EVPI            │
│ • 4-Regime Stress Test (Bull / Base / Bear / Tail Shock) │
│ • Convexity Ratio & 1st/2nd/3rd-Order Consequences       │
└──────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ STAGE 4: Zero-Cost Tier-1 Curriculum Architecture        │
│ • 80/20 Deconstruction (Concepts, Facts, Procedures)     │
│ • Strictly Free Tier-1 Sources (Specs, OCW, Open Books)  │
└──────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│ STAGE 5: Deliberate Practice & Crucible Gatekeeping      │
│ • Unassisted build/recall drills & diagnostic critique   │
└──────────────────────────────────────────────────────────┘
```

## Quantitative Risk & Trend Analyzer CLI (`scripts/risk_and_trend_analyzer.py`)

The bundled Python tool eliminates hand-wavy risk assessments by computing deterministic decision metrics, Monte Carlo forecast-error simulations, a 3-panel visual diagnostic chart, and **interactive HTML visualization reports** (v2.0.1+).

### Command-Line Usage

```bash
python3 scripts/risk_and_trend_analyzer.py --json '{
  "title": "Mastering Rust for Systems & AI Infrastructure (12-Month Horizon)",
  "options": {
    "Master Deeply (Full Commitment)": [0.35, 90, 0.40, 55, 0.15, 10, 0.10, -20],
    "Tactical 80/20 Probe (4-Week Cap)": [0.35, 65, 0.40, 45, 0.15, 20, 0.10, -5],
    "Stay on Current Stack (Baseline)": [0.35, 10, 0.40, 10, 0.15, 5, 0.10, -15]
  },
  "skill_metrics": {
    "lindy_years": 11,
    "hype_inflation_index": 35,
    "production_adoption_score": 82,
    "automation_vulnerability": 20
  },
  "ruin_threshold": -30,
  "output_chart": "rust_mastermind_audit.png",
  "output_html": "rust_mastermind_report.html"
}'
```

### Generate Interactive HTML Report (v2.0.1+)

```bash
# Via CLI flag (recommended)
python3 scripts/risk_and_trend_analyzer.py --json '<payload>' --html report.html

# Or via JSON payload
python3 scripts/risk_and_trend_analyzer.py --json '{
  "options": {...},
  "skill_metrics": {...},
  "output_html": "report.html"
}'
```

The HTML report includes:
- **Clear Verdict Badge**: GREEN (Master Deeply) / AMBER (Tactical 80/20) / RED (Pivot Away) — instantly understandable
- **Key Metrics Cards**: Expected Value, Value of Missing Data (EVPI), Skill Half-Life, Durability Score
- **Three Intuitive Charts**: 
  - Payoffs by Scenario (bar) — how each option does in best/expected/worst/extreme cases
  - Risk vs Reward (scatter) — right = safer, higher = better
  - Forecast Uncertainty (range bars) — likely outcome ranges from 1,000 simulations
- **Options Table**: Plain-language comparison with clear recommendations
- **Simulation Results**: Win rates, ruin risk, pessimistic/median/optimistic ranges
- **Key Insights**: Missing data impact, survivorship bias warning, hidden factors
- **3-Phase Learning Path**: Foundations → Core Skills → Production Mastery with time estimates
- **Crucible Gate**: First-principles test + hands-on verification drill
- **Auto Dark/Light Theme** (follows system), responsive, print-to-PDF friendly

### Run Built-In Self-Tests

```bash
python3 scripts/risk_and_trend_analyzer.py --selftest
```

## Installation & Sharing Guide for Other Users

Because this skill is packaged under the standard multi-file `SKILL.md` specification and licensed under MIT, other users can install it in three ways:

1. **Direct Archive Upload (Skills Manager UI)**:
   - Share the packaged `mastermind-skill-v2.0.0-mit.zip` archive.
   - Any user can upload the `.zip` archive or folder directly through their Skills Manager interface.
2. **Workspace Directory Installation**:
   - Place the `mastermind/` folder inside `skills/mastermind/` in the agent workspace and invoke `skills:save_skill(skill_dir="skills/mastermind")`.
3. **Git Repository / CLI Distribution**:
   - Host this folder in a public GitHub repository; users can import it by pointing their skill installer to the repository path.

## Trigger Examples & Usage Prompts

* **Skill Mastery + Trend Audit**:
  > *"Use mastermind to evaluate whether I should master Kubernetes and eBPF in 2026. I have 8 hours a week and strong Linux basics. Warn me about trend/abstraction risks, audit what data is missing, and build a 100% free Tier-1 curriculum."*
* **Analytic Chart + Strategic Decision**:
  > *"Here is a benchmark and market adoption chart for three vector database architectures. Use mastermind to analyze the chart, identify survivorship bias and missing production metrics, stress-test what happens if our query volume forecast is off by 50%, and recommend a decision."*
* **Pure Zero-Cost Deep Learning**:
  > *"Act as mastermind and teach me Linear Algebra and Convex Optimization for Machine Learning from scratch free of cost. Give me the 80/20 concept map, link only verified free Tier-1 university/textbook sources, and test me on Module 1 before letting me advance."*

## Contributing & Extending

Contributions are welcome under the MIT License:
1. Add new domain-specific free primary sources to `references/zero-cost-tier1-sources.md` (ensure every link is 100% free without registration paywalls).
2. Add worked industry case studies to `examples/sample-mastermind-walkthroughs.md`.
3. Run `python3 scripts/risk_and_trend_analyzer.py --selftest` and verify zero em-dashes in `SKILL.md` before submitting updates.

## License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for full terms.
