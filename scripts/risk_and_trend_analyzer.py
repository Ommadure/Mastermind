#!/usr/bin/env python3
"""
Mastermind Quantitative Epistemic Risk, EVPI, Monte Carlo & Trend Forensics Engine
Version: 2.0.0
License: MIT

Capabilities:
1. Expected Value (EV) across 4 forecast regimes: Bull, Base, Bear (Forecast Wrong 40%+), and Tail Shock.
2. Expected Value of Perfect Information (EVPI) to quantify the cost of missing/shadow data.
3. Monte Carlo Forecast Error Perturbation (1,000 trials with Dirichlet/Gaussian probability noise)
   to calculate Win Probability and Ruin Probability when predictions are inaccurate.
4. Automated Trend & Obsolescence Warning Radar (`GREEN`, `AMBER`, `RED`) from Lindy age,
   hype inflation, production adoption, and automation vulnerability metrics.
5. 3-Panel Publication-Grade Matplotlib Diagnostic Chart generation.
6. Built-in `--selftest` unit test suite for deterministic verification.
"""

import argparse
import json
import math
import random
import sys
import unittest
from typing import Any, Dict, List, Optional

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


SCENARIO_NAMES = [
    "Bull Regime",
    "Base Regime",
    "Bear (Forecast Off 40%+)",
    "Tail Shock",
]


def evaluate_trend_warning(skill_metrics: Optional[Dict[str, float]]) -> Dict[str, Any]:
    """
    Computes an objective Trend & Obsolescence Warning Badge from 4 structural metrics:
      - lindy_years: Age of the core technology/discipline in years (0 to 50+)
      - hype_inflation_index: 0 to 100 (higher = more social/vendor hype vs. reality)
      - production_adoption_score: 0 to 100 (higher = stronger real production usage & hiring)
      - automation_vulnerability: 0 to 100 (higher = easier to replace with trivial automation/AI)
    """
    if not skill_metrics:
        return {
            "badge": "UNSPECIFIED (Provide skill_metrics to compute badge)",
            "composite_durability_score": None,
            "estimated_half_life_years": None,
            "strategic_directive": "Evaluate Gartner Hype Cycle, Wardley stage, and Lindy age qualitatively.",
        }

    lindy = float(skill_metrics.get("lindy_years", 5.0))
    hype = float(skill_metrics.get("hype_inflation_index", 50.0))
    prod = float(skill_metrics.get("production_adoption_score", 50.0))
    auto_vuln = float(skill_metrics.get("automation_vulnerability", 50.0))

    # Normalize Lindy score (caps around 20 years -> 100 points)
    lindy_score = min(100.0, (lindy / 15.0) * 100.0)
    hype_penalty = max(0.0, hype - prod) * 0.6

    composite = (
        0.35 * prod
        + 0.30 * lindy_score
        + 0.35 * (100.0 - auto_vuln)
        - hype_penalty
    )
    composite = round(max(0.0, min(100.0, composite)), 1)

    # Estimate practical skill half-life in years
    half_life = round(max(0.8, (lindy * 0.45) + ((100.0 - auto_vuln) / 20.0)), 1)

    if composite >= 65.0 and auto_vuln < 55.0:
        badge = "GREEN: MASTER DEEPLY"
        directive = (
            "High structural durability and asymmetric career leverage. "
            "Invest in deep 80/20 Ultralearning and Deliberate Practice."
        )
    elif composite >= 40.0:
        badge = "AMBER: TACTICAL 80/20 ONLY (ABSTRACTION RISK)"
        directive = (
            "Useful right now, but elevated risk of commoditization or API churn within 18-36 months. "
            "Cap study to the 20% needed to ship and invest saved hours into Layer-A Lindy fundamentals."
        )
    else:
        badge = "RED: OBSOLESCENCE / HYPE TRAP WARNING (PIVOT)"
        directive = (
            "Severe hype-to-production divergence or high automation replacement risk. "
            "Do not invest deep mastery hours; pivot to the durable foundational primitive."
        )

    return {
        "badge": badge,
        "composite_durability_score": composite,
        "estimated_half_life_years": half_life,
        "metrics_input": {
            "lindy_years": lindy,
            "hype_inflation_index": hype,
            "production_adoption_score": prod,
            "automation_vulnerability": auto_vuln,
        },
        "strategic_directive": directive,
    }


def run_monte_carlo_sensitivity(
    options: Dict[str, List[float]],
    ruin_threshold: float = -35.0,
    trials: int = 1000,
    seed: int = 42,
) -> Dict[str, Dict[str, float]]:
    """
    Stress-tests how options perform when predicted probabilities and payoffs are noisy/wrong.
    Perturbs regime probabilities by +/- 40% relative noise and payoffs by Gaussian noise.
    """
    rng = random.Random(seed)
    win_counts = {name: 0 for name in options}
    ruin_Drawdowns = {name: 0 for name in options}
    ev_samples: Dict[str, List[float]] = {name: [] for name in options}

    base_Names = list(options.keys())
    base_probs = [
        options[base_Names[0]][0],
        options[base_Names[0]][2],
        options[base_Names[0]][4],
        options[base_Names[0]][6],
    ]

    for _ in range(trials):
        # Perturb scenario probabilities to simulate inaccurate trend forecasts
        noisy_p = [max(0.01, p * rng.uniform(0.55, 1.45)) for p in base_probs]
        norm_p = sum(noisy_p)
        noisy_p = [p / norm_p for p in noisy_p]

        trial_evs = {}
        for name, vals in options.items():
            v = [vals[1], vals[3], vals[5], vals[7]]
            # Add +/- 15% payoff noise + shock realization check
            noisy_v = [vi + rng.gauss(0, max(2.0, abs(vi) * 0.12)) for vi in v]
            ev = sum(pi * vi for pi, vi in zip(noisy_p, noisy_v))
            trial_evs[name] = ev
            ev_samples[name].append(ev)

            # Check if tail/bear weighted shock breaches ruin threshold
            worst_realized = min(noisy_v[2], noisy_v[3])
            if worst_realized <= ruin_threshold and (noisy_p[2] + noisy_p[3]) > 0.22:
                ruin_Drawdowns[name] += 1

        best_opt = max(trial_evs, key=trial_evs.get)
        win_counts[best_opt] += 1

    mc_summary = {}
    for name in options:
        samples = sorted(ev_samples[name])
        p10 = samples[int(0.10 * trials)]
        p50 = samples[int(0.50 * trials)]
        p90 = samples[int(0.90 * trials)]
        mc_summary[name] = {
            "optimal_win_rate_pct": round((win_counts[name] / trials) * 100.0, 1),
            "tail_ruin_exposure_pct": round((ruin_Drawdowns[name] / trials) * 100.0, 1),
            "ev_p10_pessimistic": round(p10, 2),
            "ev_p50_median": round(p50, 2),
            "ev_p90_optimistic": round(p90, 2),
        }

    return mc_summary


def analyze_options(
    options: Dict[str, List[float]],
    ruin_threshold: float = -35.0,
    skill_metrics: Optional[Dict[str, float]] = None,
) -> Dict[str, Any]:
    """
    Each option maps to an 8-element list:
    [p_bull, val_bull, p_base, val_base, p_bear, val_bear, p_tail, val_tail]
    """
    if not options:
        raise ValueError("At least one decision option must be provided in 'options'.")

    results = {}
    probs = None

    for name, vals in options.items():
        if len(vals) != 8:
            raise ValueError(
                f"Option '{name}' must have 8 numbers: [p1, v1, p2, v2, p3, v3, p4, v4]"
            )
        p = [float(vals[0]), float(vals[2]), float(vals[4]), float(vals[6])]
        v = [float(vals[1]), float(vals[3]), float(vals[5]), float(vals[7])]
        total_p = sum(p)
        if total_p <= 0:
            raise ValueError(f"Probabilities for option '{name}' must sum to a positive value.")
        if not math.isclose(total_p, 1.0, rel_tol=1e-2):
            p = [x / total_p for x in p]
        probs = p

        ev = sum(pi * vi for pi, vi in zip(p, v))
        max_upside = max(v)
        max_downside = min(v)
        downside_mag = abs(min(0.0, max_downside))
        convexity_ratio = (
            max_upside / downside_mag if downside_mag > 0 else float("inf")
        )
        ruin_flag = max_downside <= ruin_threshold

        if ruin_flag:
            posture = "REJECT / HEDGE (Concave Ruin Risk)"
            door_type = "Type 1 (High Irreversibility Risk)"
        elif convexity_ratio >= 2.5 and ev > 0:
            posture = "GO - HIGH CONVEXITY (Asymmetric Upside)"
            door_type = "Type 2 (Reversible / Capped Downside)"
        elif ev > 0:
            posture = "TIME-BOXED PROBE (Positive EV, Moderate Risk)"
            door_type = "Type 2 (Time-Boxed Two-Way Door)"
        else:
            posture = "AVOID (Negative or Zero Expected Value)"
            door_type = "N/A"

        results[name] = {
            "probabilities": [round(x, 4) for x in p],
            "payoffs": v,
            "expected_value": round(ev, 2),
            "max_upside": max_upside,
            "max_downside": max_downside,
            "convexity_ratio": (
                round(convexity_ratio, 2)
                if not math.isinf(convexity_ratio)
                else "Infinite (No Downside)"
            ),
            "ruin_risk": ruin_flag,
            "door_classification": door_type,
            "recommended_posture": posture,
        }

    # Expected Value of Perfect Information (EVPI)
    best_ev_under_uncertainty = max(r["expected_value"] for r in results.values())
    ev_with_perfect_info = 0.0
    if probs:
        for s_idx in range(4):
            best_in_state = max(r["payoffs"][s_idx] for r in results.values())
            ev_with_perfect_info += probs[s_idx] * best_in_state

    evpi = round(max(0.0, ev_with_perfect_info - best_ev_under_uncertainty), 2)
    mc_results = run_monte_carlo_sensitivity(options, ruin_threshold=ruin_threshold)
    for name in results:
        results[name]["monte_carlo_stress_test"] = mc_results[name]

    trend_audit = evaluate_trend_warning(skill_metrics)

    return {
        "scenarios": SCENARIO_NAMES,
        "trend_warning_radar": trend_audit,
        "options_analysis": results,
        "best_ev_under_uncertainty": round(best_ev_under_uncertainty, 2),
        "ev_with_perfect_information": round(ev_with_perfect_info, 2),
        "evpi_missing_data_value": evpi,
        "missing_data_directive": (
            "HIGH EVPI: Missing data can flip this decision. Run a 24-72h micro-experiment before full commitment."
            if evpi >= 5.0
            else "LOW EVPI: Existing asymmetry dominates missing data. Proceed with top convex option."
        ),
    }


def plot_decision_chart(
    summary: Dict[str, Any],
    output_path: str,
    title: str = "Mastermind Epistemic Risk & Trend Forensics Audit",
) -> None:
    if not HAS_MPL:
        return

    options_data = summary["options_analysis"]
    option_names = list(options_data.keys())
    scenarios = summary["scenarios"]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2), dpi=150)
    fig.patch.set_facecolor("#F8FAFC")
    fig.suptitle(title, fontsize=12, fontweight="bold", y=0.98, color="#0F172A")

    colors = ["#1E3A8A", "#0D9488", "#D97706", "#DC2626"]

    # Panel 1: Payoffs across Forecast Regimes
    ax1 = axes[0]
    x = range(len(scenarios))
    width = 0.78 / max(1, len(option_names))
    for idx, name in enumerate(option_names):
        payoffs = options_data[name]["payoffs"]
        offsets = [pos + (idx - (len(option_names) - 1) / 2) * width for pos in x]
        ax1.bar(
            offsets,
            payoffs,
            width=width * 0.9,
            label=f"{name} (EV: {options_data[name]['expected_value']})",
            color=colors[idx % len(colors)],
            alpha=0.9,
        )
    ax1.axhline(0, color="#334155", linewidth=1, linestyle="--")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(["Bull", "Base", "Bear (-40%)", "Tail Shock"], fontsize=8.5)
    ax1.set_ylabel("Utility / ROI Score (-100 to +100)", fontsize=9)
    ax1.set_title("1. Regime Payoffs (Forecast Error Stress Test)", fontsize=9.5, fontweight="bold")
    ax1.legend(fontsize=7.5, loc="best")
    ax1.grid(axis="y", linestyle=":", alpha=0.6)

    # Panel 2: Expected Value vs Worst-Case Tail Consequence
    ax2 = axes[1]
    evs = [options_data[n]["expected_value"] for n in option_names]
    tails = [options_data[n]["max_downside"] for n in option_names]
    for idx, name in enumerate(option_names):
        ax2.scatter(
            tails[idx],
            evs[idx],
            s=150,
            color=colors[idx % len(colors)],
            edgecolors="#0F172A",
            zorder=5,
        )
        ax2.annotate(
            name,
            (tails[idx], evs[idx]),
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=8,
            fontweight="bold",
        )
    ax2.axvline(0, color="#64748B", linestyle=":", linewidth=1)
    ax2.axhline(0, color="#64748B", linestyle=":", linewidth=1)
    ax2.set_xlabel("Worst-Case Tail Consequence (Right = Safer)", fontsize=9)
    ax2.set_ylabel("Expected Value (EV)", fontsize=9)
    ax2.set_title(
        f"2. Asymmetry Map | Missing Data EVPI: {summary['evpi_missing_data_value']}",
        fontsize=9.5,
        fontweight="bold",
    )
    ax2.grid(True, linestyle=":", alpha=0.6)

    # Panel 3: Monte Carlo Forecast Noise Range (P10 / P50 / P90)
    ax3 = axes[2]
    y_pos = range(len(option_names))
    for idx, name in enumerate(option_names):
        mc = options_data[name]["monte_carlo_stress_test"]
        p10, p50, p90 = mc["ev_p10_pessimistic"], mc["ev_p50_median"], mc["ev_p90_optimistic"]
        ax3.errorbar(
            p50,
            idx,
            xerr=[[p50 - p10], [p90 - p50]],
            fmt="o",
            color=colors[idx % len(colors)],
            ecolor=colors[idx % len(colors)],
            elinewidth=3,
            capsize=5,
            markersize=7,
        )
        ax3.annotate(
            f"Win: {mc['optimal_win_rate_pct']}%",
            (p50, idx),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=8,
            fontweight="bold",
        )
    ax3.axvline(0, color="#334155", linestyle="--", linewidth=1)
    ax3.set_yticks(list(y_pos))
    ax3.set_yticklabels(option_names, fontsize=8.5)
    ax3.set_xlabel("Simulated EV Range (P10 - P50 - P90)", fontsize=9)
    ax3.set_title("3. Forecast Noise Robustness (1,000 Trials)", fontsize=9.5, fontweight="bold")
    ax3.grid(axis="x", linestyle=":", alpha=0.6)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(output_path, dpi=150)
    plt.close(fig)


class MastermindAnalyzerTests(unittest.TestCase):
    def test_ev_and_evpi_calculation(self) -> None:
        options = {
            "Full Commit": [0.4, 80, 0.3, 40, 0.2, -20, 0.1, -50],
            "Tactical Probe": [0.4, 55, 0.3, 35, 0.2, 10, 0.1, -5],
            "Baseline": [0.4, 0, 0.3, 0, 0.2, 0, 0.1, 0],
        }
        res = analyze_options(
            options,
            ruin_threshold=-35,
            skill_metrics={
                "lindy_years": 12,
                "hype_inflation_index": 30,
                "production_adoption_score": 85,
                "automation_vulnerability": 20,
            },
        )
        self.assertTrue(res["options_analysis"]["Full Commit"]["ruin_risk"])
        self.assertFalse(res["options_analysis"]["Tactical Probe"]["ruin_risk"])
        self.assertGreater(res["evpi_missing_data_value"], 0.0)
        self.assertIn("GREEN", res["trend_warning_radar"]["badge"])

    def test_red_hype_trap_warning(self) -> None:
        badge_info = evaluate_trend_warning(
            {
                "lindy_years": 1.0,
                "hype_inflation_index": 95.0,
                "production_adoption_score": 20.0,
                "automation_vulnerability": 85.0,
            }
        )
        self.assertIn("RED", badge_info["badge"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Mastermind Epistemic Risk & Trend Analyzer")
    parser.add_argument("--json", type=str, help="JSON payload with options, skill_metrics, and parameters")
    parser.add_argument("--selftest", action="store_true", help="Run built-in unit tests")
    args = parser.parse_args()

    if args.selftest:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(MastermindAnalyzerTests)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)

    if not args.json:
        parser.error("Provide --json '<payload>' or --selftest.")

    payload = json.loads(args.json)
    options = payload.get("options", {})
    ruin_threshold = float(payload.get("ruin_threshold", -35.0))
    skill_metrics = payload.get("skill_metrics")
    output_chart = payload.get("output_chart")
    title = payload.get("title", "Mastermind Epistemic Risk & Trend Forensics Audit")

    summary = analyze_options(options, ruin_threshold=ruin_threshold, skill_metrics=skill_metrics)
    if output_chart:
        plot_decision_chart(summary, output_chart, title=title)
        summary["chart_saved_to"] = output_chart

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
