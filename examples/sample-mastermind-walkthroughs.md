# Sample Mastermind Walkthroughs (Reference Case Studies)

These three end-to-end case studies illustrate how `mastermind` evaluates different skill and decision requests across the `GREEN`, `AMBER`, and `RED` warning spectrum.

## Case Study 1: `[GREEN: MASTER DEEPLY]` — Distributed Systems & Consensus Fundamentals

* **User Prompt**: *"Should I spend 6 months mastering Distributed Systems and Consensus (Raft/Paxos, replication, partitioning), and how do I learn it free of cost?"*
* **Trend Warning Badge**: **`[GREEN: MASTER DEEPLY]`**
  - **Lifecycle & Lindy Analysis**: Plateau of Productivity / Core Infrastructure; Lindy age of 40+ years (since Lamport's 1978 time/clocks paper). Half-life exceeds 20 years. AI coding assistants can generate CRUD boilerplate, but they frequently introduce subtle data-corruption and split-brain bugs in distributed state machines—making human architectural mastery *more* valuable as AI code generation scales.
* **Shadow Data & EVPI Audit**:
  - **Unobserved Graveyard**: ~85% of self-learners who only *read* distributed systems papers without implementing network partition tests fail system-design and production debugging interviews.
  - **Missing Data (EVPI = 3.2 - Low)**: High certainty on long-term ROI. The only personal unknown is concurrency fluency in Go or Rust.
* **Zero-Cost Tier-1 Curriculum (Top Sources)**:
  1. **MIT 6.5840 (formerly 6.824) Distributed Systems** ([MIT 6.5840 Schedule & Labs](https://pdos.csail.mit.edu/6.824/schedule.html)) — Tier 1B Open University Courseware: Complete the Raft consensus and fault-tolerant Key-Value service labs in Go.
  2. **In Search of an Understandable Consensus Algorithm (Raft Extended Paper)** ([Ongaro & Ousterhout Raft Paper PDF](https://raft.github.io/raft.pdf)) — Tier 1A/1B Primary Spec: Implement Figure 2 state transitions verbatim.
  3. **Jepsen Distributed Systems Safety Analyses** ([Jepsen Analyses Archive](https://jepsen.io/analyses)) — Tier 1A Production Forensics: Study how real production databases fail under network partitions and clock skew.
* **Crucible Gate #1**: Explain why a Raft leader cannot safely commit a log entry from a *previous* term solely by counting replicas, and implement leader election passing all partition test cases in MIT Lab 3A.

## Case Study 2: `[AMBER: TACTICAL 80/20 ONLY]` — Niche High-Level Prompt-Orchestration Wrappers

* **User Prompt**: *"I want to spend the next 4 months mastering a specific multi-agent wrapper framework to build my career."*
* **Trend Warning Badge**: **`[AMBER: TACTICAL 80/20 ONLY - ABSTRACTION RISK]`**
  - **Lifecycle & Lindy Analysis**: Peak of Inflated Expectations transitioning into Trough of Disillusionment; Lindy age under 2 years; estimated API half-life of 6 to 12 months. Major foundation model providers natively absorb wrapper orchestration features every release cycle.
* **Epistemic & Consequence Audit**:
  - **Concave Trap on Full Mastery**: Spending 200 hours memorizing a high-level wrapper's abstractions is a fragile bet—if the framework breaks backward compatibility or gets superseded by native SDK tool-use, 80% of that memorized syntax becomes worthless.
  - **Convex Pivot**: Cap learning the wrapper to a **12-hour weekend sprint** (the 20% needed to ship prototypes), and invest the remaining **180+ hours** in **Lindy Core AI Systems Engineering**: structured outputs, evaluation harnesses (evals), retrieval information theory (BM25 + vector hybrid search), latency/token economics, and direct state-machine orchestration in standard Python/TypeScript.
* **Zero-Cost Tier-1 Curriculum (Top Sources)**:
  1. **Stanford CS324: Large Language Models** ([Stanford CS324 Course Notes](https://stanford-cs324.github.io/winter2022/)) — Tier 1B Open University Courseware.
  2. **Introduction to Information Retrieval (Manning, Raghavan, Schütze)** ([Stanford NLP IIR Free Book](https://nlp.stanford.edu/IR-book/)) — Tier 1C Open Textbook for true search/retrieval math.
  3. **Anthropic & OpenAI Official Prompt & Evaluation Engineering Guides** ([OpenAI Platform Docs](https://platform.openai.com/docs/)) — Tier 1A Primary Maintainer Documentation.

## Case Study 3: `[RED: OBSOLESCENCE / HYPE TRAP WARNING]` — Manual Boilerplate PSD-to-HTML Slice Coding

* **User Prompt**: *"Should I spend 6 months mastering manual PSD-to-static-HTML/CSS slicing to freelance full-time?"*
* **Trend Warning Badge**: **`[RED: OBSOLESCENCE / HYPE TRAP WARNING - PIVOT]`**
  - **Lifecycle & Chart Forensics**: Secular commodity decline. Automated design-to-code compilers, component libraries, and multimodal vision-to-UI models have compressed the market rate for pure static template slicing by >75%.
* **Shadow Data Audit**:
  - **Survivorship Bias**: Freelancers displaying high earnings on marketplaces in this category built their client rosters 7 to 10 years ago and actually sell full-stack conversion optimization or custom interactive WebGL/accessibility engineering, not static slicing.
* **Rational Pivot Recommendation**:
  - Abandon pure static slicing. Pivot immediately to **Web Performance Forensics, W3C Accessibility Auditing (WCAG 2.2), and Full-Stack Reactive State Architecture** using [MDN Web Docs](https://developer.mozilla.org/), [High Performance Browser Networking](https://hpbn.co/), and [W3C Web Accessibility Initiative](https://www.w3.org/WAI/).
