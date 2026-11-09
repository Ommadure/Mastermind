# Epistemic & Asymmetric Risk Framework

This reference governs **Stage 3 (Epistemic & Asymmetric Risk Engine)** of the `mastermind` skill. Use it to audit known data, uncover missing/shadow data, stress-test noisy predictions, and evaluate asymmetric consequences.

## 1. Known Data Forensics & Outside-View Base Rates

Standard reasoning falls into the **Inside View** (judging a plan by personal optimism or vendor promises). Mastermind enforces Philip Tetlock's **Outside View**:

1. **Reference Class Forecasting**: Define the statistical reference class for the user's goal (e.g., "self-taught learners attempting full-stack Rust competency in 6 months while working full-time" or "B2B SaaS products migrating to microservice architectures").
2. **Historical Attrition & Failure Base Rate**: State the empirical base rate of completion or success (typically 5% to 15% for unguided MOOCs/self-study; 25% to 40% for project-driven cohorts).
3. **Evidence Quality Weighting**:
   - **High Weight (0.8 - 1.0)**: Audited production post-mortems, peer-reviewed empirical studies, reproducible benchmarks on open datasets, direct market hiring/compensation ledgers.
   - **Medium Weight (0.4 - 0.7)**: Practitioner survey aggregates (e.g., Stack Overflow Developer Survey, CNCF Survey), longitudinal GitHub commit/issue velocity.
   - **Low Weight (0.0 - 0.3)**: Vendor whitepapers, influencer tutorials, cherry-picked micro-benchmarks, bootcamp placement claims.

## 2. The Shadow Data Protocol (Abraham Wald Survivorship Filter)

During WWII, statistician Abraham Wald showed that armoring bombers where returning planes had bullet holes was a fatal error—the missing data (planes shot in the engines that never returned) held the real signal.

For every decision or skill audit, explicitly construct the **Shadow Data Table**:

| Shadow Data Category | Diagnostic Question to Answer | Impact on Decision |
| :--- | :--- | :--- |
| **1. The Unobserved Graveyard** | Who attempted this skill, tool, or strategy and failed silently? Why are they absent from the dataset? | Adjusts naive success probabilities downward toward the true base rate. |
| **2. Confounder & Selection Bias** | Did visible winners succeed *because* of this tool/skill, or because they already had elite distribution, capital, or 10 years of systems experience? | Prevents attributing background advantages to the tool or curriculum itself. |
| **3. Hidden Prerequisite Debt** | What unstated foundational skills (e.g., linear algebra, memory management, probability, regulatory compliance) cause 80% of beginners to stall out at week 4? | Inserts mandatory prerequisite modules before the main learning track. |
| **4. Unmeasured Switching / Lock-In Cost** | What happens in 24 months if the vendor changes licensing, deprecates the API, or the niche shrinks? | Penalizes proprietary, non-transferable skills in the consequence matrix. |

## 3. Expected Value of Perfect Information (EVPI) & Micro-Experiments

Before committing hundreds of hours or significant capital under uncertainty, quantify how much the **missing data** is actually worth:

$$\text{EVPI} = \text{EV}_{\text{with perfect foresight}} - \text{EV}_{\text{under current uncertainty}}$$

Where:
- $\text{EV}_{\text{with perfect foresight}} = \sum_{s \in S} P(s) \cdot \max_{a \in A} V(a, s)$
- $\text{EV}_{\text{under current uncertainty}} = \max_{a \in A} \sum_{s \in S} P(s) \cdot V(a, s)$

### Operational EVPI Rules
- **Low EVPI ($\text{EVPI} < 5$ utility points)**: The best option dominates across almost all scenarios even with missing data. **Do not waste time over-researching—execute the top convex option immediately.**
- **High EVPI ($\text{EVPI} \ge 5$ utility points)**: Missing information can easily flip the optimal choice. **Halt full commitment and prescribe a 24-to-72-hour Micro-Experiment** to measure the unknown variable directly (e.g., build a 1-day prototype, run 5 cold market outreach tests, or complete 1 hardcore problem set to test personal aptitude).

## 4. Prediction Error Tolerance & Consequence Asymmetry (Convexity vs. Concavity)

Forecasts of technology and market trends 3 to 5 years out carry wide error bars. Mastermind separates **Forecast Probability** from **Payoff Convexity**:

### The 4-Regime Stress Test
Never evaluate a decision on a single expected future. Score every option on a $-100$ to $+100$ utility scale across four regimes:
1. **Bull Regime**: The trend accelerates faster than expected ($+30\%$ to $+50\%$ adoption/demand).
2. **Base Regime**: The trend follows current consensus trajectory.
3. **Bear Regime (Forecast Wrong by 40%+)**: The technology stalls, hits the Trough of Disillusionment, or takes 3x longer to mature.
4. **Tail-Shock Regime**: AI automation, regulatory shifts, or a superior paradigm renders the specific tool obsolete overnight.

### Payoff Asymmetry & Reversibility Matrix

| Payoff Function | Door Type (Bezos) | Convexity Ratio ($\frac{\text{Max Upside}}{|\text{Max Downside}|}$) | Consequence Profile | Mastermind Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Convex (Antifragile)** | **Type 2 (Reversible Two-Way Door)** | $\ge 3.0$ | Capped, minor downside (e.g., 15 hours spent learning transferable concepts); massive uncapped career or capability upside. | **GREENLIGHT**: Proceed even if forecast confidence is only 25% to 35%. |
| **Linear (Symmetric)** | **Type 2 (Reversible Two-Way Door)** | $1.0 - 2.9$ | Proportional return on hours invested; moderate opportunity cost if forecast is wrong. | **TIME-BOXED PROBE**: Commit a strict 2-to-4-week sprint with a hard review gate. |
| **Concave (Fragile)** | **Type 1 (Irreversible One-Way Door)** | $< 1.0$ or Tail $\le \text{Ruin}$ | Modest upside if right, but catastrophic loss of time, capital, or career positioning if the forecast is off by 30%. | **VETO / HEDGE**: Reject full commitment even if forecast probability appears 75%+ favorable. |

## 5. First-, Second-, and Third-Order Consequence Tracing

For every recommended action, explicitly map three horizons of consequence:
- **1st-Order Consequence (0 - 3 Months)**: Immediate time cost, cognitive friction, and initial skill output.
- **2nd-Order Consequence (3 - 12 Months)**: Opportunity cost (what you *did not* learn or build during those hours) and portfolio positioning.
- **3rd-Order Consequence (1 - 5 Years)**: Compounding network/career leverage, Lindy durability of the acquired mental models, and resilience against automation.
