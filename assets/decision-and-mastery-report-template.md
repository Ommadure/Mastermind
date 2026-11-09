# Mastermind Strategic Audit & Zero-Cost Mastery Blueprint (Template)

Use this structure when delivering a comprehensive Mastermind evaluation and learning roadmap. Adapt the depth to match the complexity of the user's request.

## 0. Interactive HTML Visualization (v2.0.1+)

For enhanced understanding and stakeholder communication, generate an interactive HTML report:
```bash
python3 scripts/risk_and_trend_analyzer.py --json '<payload>' --html report.html
```

The HTML report includes:
- **Executive Dashboard**: Animated trend badge, key metrics cards
- **Interactive Charts**: Regime payoffs (bar), Asymmetry map (scatter), Monte Carlo ranges (P10/P50/P90)
- **Risk Matrix**: Sortable table with color-coded posture badges
- **Learning Roadmap**: Timeline with phase markers
- **Dark/Light Theme**: Persisted preference, auto-detects system theme
- **Print-Friendly**: Clean PDF output via browser print

---

## 1. Executive Verdict & Trend Warning Badge

* **Target Skill / Decision**: `<Name of Skill, Technology, or Strategic Decision>`
* **Trend Warning Badge**: `[GREEN: MASTER DEEPLY]` | `[AMBER: TACTICAL 80/20 ONLY]` | `[RED: OBSOLESCENCE / HYPE TRAP - PIVOT]`
* **Lifecycle & Lindy Position**: `<Gartner Hype Stage>` | `<Wardley Stage>` | `<Estimated Skill Half-Life in Years>`
* **Bottom-Line Verdict**: `<1-2 crisp sentences stating the exact rational decision, realistic hours to competency, and primary caveat without sugarcoating>`

## 2. Epistemic & Asymmetric Risk Matrix

| Strategic Option | Bull Payoff | Base Payoff | Bear (Forecast Wrong 40%+) | Tail Shock | Expected Value (EV) | Convexity Ratio | Reversibility (Door Type) | Posture |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Option A (Full Mastery)** | `<val>` | `<val>` | `<val>` | `<val>` | `<EV>` | `<Ratio>` | `Type 1 / Type 2` | `<GO / PROBE / REJECT>` |
| **Option B (Tactical 80/20)** | `<val>` | `<val>` | `<val>` | `<val>` | `<EV>` | `<Ratio>` | `Type 2` | `<GO / PROBE / REJECT>` |
| **Option C (Pivot / Baseline)** | `<val>` | `<val>` | `<val>` | `<val>` | `<EV>` | `<Ratio>` | `Type 2` | `<GO / PROBE / REJECT>` |

### Shadow Data Audit (What the Visible Data Hides)
* **Unobserved Graveyard (Survivorship Bias)**: `<Historical attrition rate and who fails silently>`
* **Omitted Confounders**: `<Prerequisites or advantages hidden behind survivor stories>`
* **Missing Data Value (EVPI) & 48-Hour Micro-Experiment**: `<State what critical data is missing and the exact 24-72h test to measure it before full commitment>`

### Consequence Horizon & Pre-Mortem (Assuming Failure in 6 Months)
* **Top 2 Pre-Mortem Failure Modes & Lock-In Mitigations**: `<Why this plan is most likely to fail and the structural rule to prevent it>`
* **1st / 2nd / 3rd-Order Consequences**: `<Immediate cost -> Opportunity cost -> 3-5 year compounding effect>`

## 3. Zero-Cost 80/20 Deconstruction & Tier-1 Primary Sources

| Module & Time Allocation | Core Concepts & Procedures (80/20 Focus) | Verified 100% Free Tier-1 Primary Sources | What to Skip (Fluff Filter) |
| :--- | :--- | :--- | :--- |
| **Phase 1: Foundations (`<X>` hrs)** | `<Concepts & mental models>` | `[Exact Title](https://...)` (`<Tier 1A/1B/1C - why trusted>`) | `<Specific chapters/topics to ignore>` |
| **Phase 2: Core Execution (`<Y>` hrs)** | `<Applied procedures & edge cases>` | `[Exact Title](https://...)` (`<Tier 1A/1B/1C - why trusted>`) | `<Specific chapters/topics to ignore>` |
| **Phase 3: Production Mastery (`<Z>` hrs)** | `<System integration & stress testing>` | `[Exact Title](https://...)` (`<Tier 1A/1B/1C - why trusted>`) | `<Specific chapters/topics to ignore>` |

## 4. Crucible Gate #1 (Immediate Deliberate Practice Challenge)

* **First-Principles Defense Question**: `<Question testing causal understanding without buzzwords>`
* **Hands-On Build / Diagnostic Drill**: `<Concrete mini-build or problem the user must complete before advancing to Phase 2>`
