# Trend Forensics & Analytic Chart Reading Protocol

This reference governs **Stage 2 (Trend Forensics & Obsolescence Warning Radar)** of the `mastermind` skill. Use it to inspect uploaded charts, evaluate live market trajectories, and issue an explicit `GREEN`, `AMBER`, or `RED` trend warning before the user invests time in mastering a skill.

## 1. Analytic Chart Forensics Checklist

Whenever the user uploads an analytic chart (adoption curve, benchmark comparison, revenue/job trend, or performance graph) or when inspecting quantitative market series, audit these six structural dimensions:

1. **Axis & Scale Integrity**:
   - Check whether the Y-axis is truncated (exaggerating minor deltas) or uses a linear vs. logarithmic scale.
   - Check whether dual Y-axes are scaled to manufacture a spurious correlation.
2. **Timeframe & Regime Selection (Cherry-Picked Windows)**:
   - Identify the start and end dates. Does the chart start right at a cyclical trough or omit a recent plateau?
   - Compare short-term momentum (3-6 months) against the multi-year structural trend (3-5 years).
3. **Metric Definition & Proxy Validity**:
   - **Vanity Metrics (Low Signal)**: Social media mentions, GitHub stars alone, press release counts, waitlist signups, synthetic vendor micro-benchmarks.
   - **Structural Metrics (High Signal)**: Production deployments, active contributor retention, job postings requiring production experience, enterprise renewal/expansion rates, real-world latency/cost-per-unit curves.
4. **Variance, Confidence Intervals & Outliers**:
   - Check whether the chart plots only a mean (hiding massive variance or bimodal distributions) vs. median and interquartile ranges (P25/P50/P75/P99).
5. **First & Second Derivatives (Velocity vs. Acceleration)**:
   - Is growth accelerating ($f''(t) > 0$), growing linearly ($f''(t) \approx 0$), or decelerating toward an S-curve inflection point ($f''(t) < 0$)?
6. **Silent Denominator Check**:
   - If a skill or tool shows "+200% growth", check the absolute base. Growing from 50 job listings to 150 is noise compared to a core skill with 50,000 listings growing at 12%.

## 2. Lifecycle & Evolution Classification Matrix

Cross-reference every technology or skill across **Gartner's Hype Cycle** and **Simon Wardley's Evolution Axis**:

| Lifecycle Stage | Market & Chart Signatures | Skill Investment Strategy |
| :--- | :--- | :--- |
| **1. Genesis / Innovation Trigger** | High academic/R&D velocity, rapid breaking changes, tiny job market, zero standardized tooling. | **Explore Conceptually**: Read foundational papers and build weekend prototypes; do not memorize unstable APIs. |
| **2. Peak of Inflated Expectations** | Viral hype, "X will replace everything" claims, flood of paid beginner courses, low production retention. | **AMBER/RED Warning**: High risk of trough crash. Strip away the hype and study only the underlying computer science or domain primitive. |
| **3. Trough of Disillusionment** | Media backlash, weak startups folding, surviving teams solving hard production bottlenecks quietly. | **Contrarian Buyer's Market**: If core fundamentals are sound, mastering production failure modes here yields high differentiation. |
| **4. Slope of Enlightenment (Product)** | Standardized best practices, growing production hiring demand, clear ROI metrics, strong ecosystem tooling. | **GREEN (Peak Mastery Window)**: Highest return on deep deliberate practice and portfolio execution. |
| **5. Plateau of Productivity (Commodity / Utility)** | Ubiquitous adoption, stable interfaces, increasingly abstracted by cloud services or AI code generation. | **Architectural Literacy**: Understand how it works under the hood for debugging, but avoid spending months memorizing boilerplate syntax. |

## 3. The Lindy Durability & Skill Half-Life Formula

Per World Economic Forum workforce research, the average half-life of a professional skill is roughly 5 years, and narrow technical skills decay in ~2.5 years. Use Nassim Taleb's **Lindy Effect** to decompose any skill into three layers:

1. **Layer A - Lindy Core (Half-Life: 15 to 50+ Years) -> Allocate 50% of Learning Time**:
   - Mathematical foundations, algorithms, distributed systems theory, operating systems internals, information theory, microeconomics, statistical inference, cognitive psychology, persuasive writing, negotiation.
2. **Layer B - Ecosystem & Architecture (Half-Life: 4 to 8 Years) -> Allocate 35% of Learning Time**:
   - Major programming languages (Python, Rust, C++, SQL, TypeScript), Linux kernel/networking tools, relational/vector storage engines, container orchestration concepts, financial modeling standards.
3. **Layer C - Ephemeral Wrappers & Syntax (Half-Life: 6 to 24 Months) -> Allocate 15% Just-In-Time**:
   - Specific UI libraries, wrapper SDKs, prompt templates, vendor-specific configuration GUI workflows.

## 4. Trend Warning Badge Criteria (`GREEN` / `AMBER` / `RED`)

Every Mastermind skill evaluation must output one of these three explicit warnings:

- **`[GREEN: MASTER DEEPLY]`**
  - **Criteria**: Strong production adoption (or high-Lindy foundation), positive hiring/utility trajectory over a 3-to-5-year horizon, low vulnerability to trivial AI replacement, and high skill transferability.
  - **Action**: Build a full 80/20 Ultralearning + Deliberate Practice curriculum.
- **`[AMBER: TACTICAL 80/20 ONLY - ABSTRACTION RISK]`**
  - **Criteria**: Useful for shipping today, but high hype inflation, rapid API churn, or >50% likelihood of being abstracted away by AI/commoditization within 18 to 36 months.
  - **Action**: Cap learning time to a strict tactical sprint (e.g., 10 to 20 hours to learn the 20% needed to ship), and redirect the remaining 80% of study time to the Layer A/B fundamentals underneath it.
- **`[RED: OBSOLESCENCE / HYPE TRAP WARNING - PIVOT]`**
  - **Criteria**: Secular decline in production usage, severe vendor lock-in with shrinking market share, or pure hype wrapper with zero durable moat.
  - **Action**: Explicitly advise the user **not** to master this skill. State the exact reasons backed by trend data and provide a direct pivot roadmap to the superior alternative.
