# Deliberate Practice & Ultralearning Pedagogy Protocol

This reference governs **Stage 4 (80/20 Deconstruction)** and **Stage 5 (Deliberate Practice & Crucible Gatekeeping)** of the `mastermind` skill. It ensures the user achieves real, durable mastery rather than the "illusion of competence" that comes from passive video watching or re-reading notes.

## 1. Scott Young's Ultralearning Metalearning Map (80/20 Deconstruction)

Before assigning any reading or exercise, deconstruct the target skill into three distinct buckets and prune the 70% of curriculum filler that does not drive real-world performance:

| Bucket | Definition | How Mastermind Teaches & Tests It |
| :--- | :--- | :--- |
| **1. Concepts (What to Understand)** | First-principles mental models, invariants, trade-offs, and causal mechanisms. | Tested via **Feynman Inversion Drills**: Ask the user to explain *why* a mechanism works and *when* it breaks without using buzzwords. |
| **2. Facts (What to Memorize or Index)** | Core terminology, orders of magnitude (latency/cost numbers), syntax primitives, or reference lookup paths. | Tested via **Spaced Active Retrieval**: Rapid-fire closed-book diagnostic questions; never waste hours memorizing what takes 5 seconds to look up in official docs. |
| **3. Procedures (What to Practice)** | Muscle-memory workflows, debugging sequences, proof techniques, or production builds. | Tested via **Directness Projects**: Build, debug, or analyze a real artifact in the actual target environment from Day 1. |

## 2. K. Anders Ericsson's Deliberate Practice Rules

Ordinary repetition plateaus quickly. To force continuous growth across the user's learning sessions, enforce these four Deliberate Practice conditions:

1. **Operate at the Edge of Current Ability (+15% Difficulty Zone)**:
   - Never assign trivial "Hello World" copy-paste tutorials if the user already knows basic programming or domain logic.
   - Design tasks where the user will initially fail or struggle on 20% to 30% of the edge cases.
2. **Isolate Micro-Bottlenecks (The Drill Principle)**:
   - When a user struggles with a complex task (e.g., building a distributed consensus node or writing a persuasive strategic memo), isolate the single weakest sub-skill (e.g., async state transitions or counterfactual thesis framing) and drill that component repeatedly until fluent.
3. **Immediate, High-Clarity Diagnostic Feedback**:
   - When reviewing user code, math, writing, or decisions, never respond with vague praise like *"Good job!"* or *"Nice start!"*
   - State specifically:
     - **What passed**: The exact logic or structure that is solid.
     - **What failed or is fragile**: Exact line/argument flaws, hidden assumptions, race conditions, or unhandled tail risks.
     - **The Remediation Drill**: The exact fix or revision required right now.
4. **Prevent Premature Automation / AI Crutches During Learning**:
   - Warn the user when using auto-complete or LLM code/text generation during the learning phase will short-circuit neural myelination. Require them to write core implementations and proofs by hand first.

## 3. The 3-Tier Mastery Crucible Gatekeeper

Structure every learning roadmap into sequential phases separated by **Crucible Gates**. Do not let the user claim mastery of a phase until they can pass its gate:

- **Gate 1: Foundational Literacy & First-Principles Defense (Hours 1 - 15)**
  - *Requirement*: Explain the core architecture, trade-offs, and failure modes of the skill from memory, and build a minimal working end-to-end artifact using only official documentation.
- **Gate 2: Adversarial Debugging & Edge-Case Stress Test (Hours 15 - 50)**
  - *Requirement*: Diagnose and fix broken implementations, handle malformed inputs or adversarial conditions, and benchmark performance against a baseline.
- **Gate 3: Production-Grade Capstone & Pre-Mortem Audit (Hours 50+)**
  - *Requirement*: Design, ship, and document an original, non-trivial project or strategic analysis from scratch, complete with a Pre-Mortem risk register and empirical verification.
