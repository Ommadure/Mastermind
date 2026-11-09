#!/usr/bin/env python3
"""
Mastermind HTML Visualization Generator - Simplified v2.0.1
Version: 2.0.1
License: MIT

Generates clean, accessible HTML reports from Mastermind analysis results.
Focus on clarity, simplicity, and universal readability.
"""

import json
import html
from typing import Dict, Any, List, Optional
from datetime import datetime
from string import Template


# Simplified HTML Template - Clean, Accessible, User-Friendly
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
        :root {
            --bg: #fafafa;
            --card: #ffffff;
            --text: #1a1a2e;
            --text-muted: #555;
            --border: #e0e0e0;
            --primary: #2563eb;
            --success: #16a34a;
            --warning: #d97706;
            --danger: #dc2626;
            --shadow: 0 2px 8px rgba(0,0,0,0.06);
            --radius: 10px;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --bg: #141423;
                --card: #1e1e30;
                --text: #f0f0f5;
                --text-muted: #aaa;
                --border: #333;
                --shadow: 0 2px 8px rgba(0,0,0,0.3);
            }
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 20px;
            max-width: 900px;
            margin: 0 auto;
        }

        h1 { font-size: 1.8rem; font-weight: 700; margin-bottom: 4px; }
        h2 { font-size: 1.3rem; font-weight: 600; margin: 24px 0 12px; padding-bottom: 6px; border-bottom: 2px solid var(--border); }
        h3 { font-size: 1.1rem; font-weight: 600; margin: 16px 0 8px; }

        p { color: var(--text-muted); margin-bottom: 12px; }

        .meta { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 24px; }

        /* Badge */
        .verdict-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 14px 20px;
            border-radius: var(--radius);
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 24px;
            border: 2px solid;
        }
        .verdict-badge.green { background: #f0fdf4; color: #166534; border-color: #16a34a; }
        .verdict-badge.amber { background: #fffbeb; color: #92400e; border-color: #d97706; }
        .verdict-badge.red { background: #fef2f2; color: #991b1b; border-color: #dc2626; }
        @media (prefers-color-scheme: dark) {
            .verdict-badge.green { background: #14532d; color: #86efac; border-color: #22c55e; }
            .verdict-badge.amber { background: #78350f; color: #fde047; border-color: #f59e0b; }
            .verdict-badge.red { background: #7f1d1d; color: #fca5a5; border-color: #ef4444; }
        }
        .badge-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }

        /* Card Grid */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }
        .card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
            box-shadow: var(--shadow);
        }

        .metric { text-align: center; }
        .metric-value { font-size: 2rem; font-weight: 700; font-family: monospace; line-height: 1.2; }
        .metric-label { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
        .metric.good .metric-value { color: var(--success); }
        .metric.warning .metric-value { color: var(--warning); }
        .metric.bad .metric-value { color: var(--danger); }

        /* Charts */
        .chart-card { grid-column: 1 / -1; }
        .chart-wrap { position: relative; height: 280px; }

        /* Table */
        .table-wrap { overflow-x: auto; margin-top: 12px; }
        table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid var(--border); }
        th { background: var(--bg); font-weight: 600; color: var(--text-muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; }
        tr:hover td { background: var(--bg); }

        .posture {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }
        .posture-go { background: #dcfce7; color: #166534; }
        .posture-probe { background: #fef3c7; color: #92400e; }
        .posture-avoid { background: #fee2e2; color: #991b1b; }
        @media (prefers-color-scheme: dark) {
            .posture-go { background: #14532d; color: #86efac; }
            .posture-probe { background: #78350f; color: #fde047; }
            .posture-avoid { background: #7f1d1d; color: #fca5a5; }
        }

        /* Insight Boxes */
        .insight {
            background: var(--card);
            border: 1px solid var(--border);
            border-left: 4px solid var(--primary);
            border-radius: var(--radius);
            padding: 16px;
            margin: 12px 0;
        }
        .insight-title { font-weight: 600; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }
        .insight.warning { border-left-color: var(--warning); }
        .insight.danger { border-left-color: var(--danger); }
        .insight.success { border-left-color: var(--success); }

        /* Roadmap */
        .phase {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 16px;
            margin: 12px 0;
            position: relative;
            padding-left: 48px;
        }
        .phase::before {
            content: "";
            position: absolute;
            left: 16px;
            top: 16px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            border: 3px solid var(--card);
        }
        .phase.phase1::before { background: var(--success); }
        .phase.phase2::before { background: var(--warning); }
        .phase.phase3::before { background: var(--danger); }

        .phase-title { font-weight: 600; margin-bottom: 4px; }
        .phase-time { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 8px; }
        .phase-focus { color: var(--text-muted); font-size: 0.9rem; }

        /* Simple List */
        .simple-list { margin-left: 20px; margin-top: 8px; }
        .simple-list li { margin: 6px 0; color: var(--text-muted); }

        /* Footer */
        footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border); text-align: center; color: var(--text-muted); font-size: 0.85rem; }

        /* Print */
        @media print {
            body { background: white; color: black; padding: 0; }
            .card { box-shadow: none; border: 1px solid #ccc; }
            .verdict-badge { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        }

        @media (max-width: 600px) {
            body { padding: 16px; }
            h1 { font-size: 1.5rem; }
            .grid { grid-template-columns: 1fr; }
            .chart-wrap { height: 240px; }
            .phase { padding-left: 36px; }
        }
    </style>
</head>
<body>
    <header>
        <h1>${title}</h1>
        <p class="meta">Generated ${timestamp} • Mastermind v2.0.1</p>
    </header>

    <!-- Main Verdict -->
    <div class="verdict-badge ${badge_class}">
        <span class="badge-dot" style="background: ${badge_color};"></span>
        <span>${badge_text}</span>
    </div>

    <p>${directive}</p>

    <!-- Key Metrics -->
    <div class="grid">
        <div class="card metric ${ev_class}">
            <div class="metric-value">${best_ev}</div>
            <div class="metric-label">Best Expected Value</div>
        </div>
        <div class="card metric">
            <div class="metric-value">${evpi}</div>
            <div class="metric-label">Value of Perfect Info (EVPI)</div>
        </div>
        <div class="card metric">
            <div class="metric-value">${half_life}</div>
            <div class="metric-label">Skill Half-Life (years)</div>
        </div>
        <div class="card metric ${durability_class}">
            <div class="metric-value">${durability}</div>
            <div class="metric-label">Durability Score</div>
        </div>
    </div>

    <!-- Trend Context -->
    <div class="grid">
        <div class="card">
            <h3>Trend Context</h3>
            <p><strong>Lindy Age:</strong> ${lindy_years} years</p>
            <p><strong>Hype Level:</strong> ${hype_index}/100</p>
            <p><strong>Production Adoption:</strong> ${prod_adoption}/100</p>
            <p><strong>Automation Risk:</strong> ${auto_vuln}/100</p>
        </div>
    </div>

    <!-- Charts -->
    <div class="grid">
        <div class="card chart-card">
            <h2>Payoffs by Scenario</h2>
            <div class="chart-wrap"><canvas id="payoffChart"></canvas></div>
            <p style="margin-top: 8px; font-size: 0.85rem;">Shows how each option performs under four scenarios: Best case (Bull), Expected (Base), 40% forecast error (Bear), and Extreme shock (Tail).</p>
        </div>

        <div class="card chart-card">
            <h2>Risk vs Reward</h2>
            <div class="chart-wrap"><canvas id="asymmetryChart"></canvas></div>
            <p style="margin-top: 8px; font-size: 0.85rem;">Each dot is an option. Right = safer (less downside). Higher = better expected value. Ideal options are top-right.</p>
        </div>

        <div class="card chart-card">
            <h2>Forecast Uncertainty</h2>
            <div class="chart-wrap"><canvas id="monteCarloChart"></canvas></div>
            <p style="margin-top: 8px; font-size: 0.85rem;">After 1,000 simulations with noisy forecasts. Bars show likely range (P10-P90). Dot = median.</p>
        </div>
    </div>

    <!-- Options Comparison -->
    <h2>Options at a Glance</h2>
    <div class="table-wrap">
        <table>
            <thead>
                <tr>
                    <th>Option</th>
                    <th>Bull</th>
                    <th>Base</th>
                    <th>Bear</th>
                    <th>Tail</th>
                    <th>EV</th>
                    <th>Convexity</th>
                    <th>Reversibility</th>
                    <th>Recommendation</th>
                </tr>
            </thead>
            <tbody>
                ${risk_table_rows}
            </tbody>
        </table>
    </div>

    <!-- Monte Carlo Details -->
    <h2>Simulation Results</h2>
    <div class="table-wrap">
        <table>
            <thead>
                <tr>
                    <th>Option</th>
                    <th>Win Rate</th>
                    <th>Ruin Risk</th>
                    <th>Pessimistic (P10)</th>
                    <th>Median (P50)</th>
                    <th>Optimistic (P90)</th>
                </tr>
            </thead>
            <tbody>
                ${mc_table_rows}
            </tbody>
        </table>
    </div>

    <!-- Key Insights -->
    <h2>What You Should Know</h2>

    <div class="insight ${evpi_class}">
        <div class="insight-title">📊 Missing Data Impact: ${evpi_label}</div>
        <p>${evpi_directive}</p>
    </div>

    <div class="insight warning">
        <div class="insight-title">⚠️ Survivorship Bias</div>
        <p>${survivorship_bias}</p>
    </div>

    <div class="insight warning">
        <div class="insight-title">🔍 Hidden Factors</div>
        <p>${omitted_confounders}</p>
    </div>

    <!-- Learning Roadmap -->
    <h2>Suggested Learning Path</h2>

    <div class="phase phase1">
        <div class="phase-title">Phase 1: Foundations</div>
        <div class="phase-time">~20-40 hours</div>
        <div class="phase-focus">Core concepts & mental models</div>
        <ul class="simple-list">
            <li>Read official specifications & documentation (Tier 1A)</li>
            <li>Build mental models before writing code</li>
            <li>Complete: Explain the core idea in plain language</li>
        </ul>
    </div>

    <div class="phase phase2">
        <div class="phase-title">Phase 2: Core Skills</div>
        <div class="phase-time">~40-80 hours</div>
        <div class="phase-focus">Applied procedures & edge cases</div>
        <ul class="simple-list">
            <li>Follow open university courses & peer-reviewed papers (Tier 1B)</li>
            <li>Practice the 20% of skills used 80% of the time</li>
            <li>Complete: Build a working mini-project</li>
        </ul>
    </div>

    <div class="phase phase3">
        <div class="phase-title">Phase 3: Production Mastery</div>
        <div class="phase-time">~80-160 hours</div>
        <div class="phase-focus">Integration, stress testing, real-world constraints</div>
        <ul class="simple-list">
            <li>Use open-source textbooks & interactive sandboxes (Tier 1C)</li>
            <li>Handle failures, scale, and maintenance</li>
            <li>Complete: Ship something real or pass verification gate</li>
        </ul>
    </div>

    <!-- Crucible Gate -->
    <h2>Your First Checkpoint</h2>

    <div class="insight">
        <div class="insight-title">🧠 First-Principles Test</div>
        <p>${defense_question}</p>
    </div>

    <div class="insight success">
        <div class="insight-title">🛠️ Hands-On Drill</div>
        <p>${diagnostic_drill}</p>
    </div>

    <footer>
        <p>Generated by <strong>Mastermind v2.0.1</strong> — Rational Decision Engine</p>
        <p>MIT Licensed • <a href="#" onclick="window.print()">Print / Save as PDF</a></p>
    </footer>

    <script>
        // Chart Data
        const chartData = ${chart_data_json};

        // Theme-aware colors
        function getColors() {
            const dark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            return {
                grid: dark ? '#333' : '#e0e0e0',
                text: dark ? '#aaa' : '#555',
                primary: '#2563eb',
                success: '#16a34a',
                warning: '#d97706',
                danger: '#dc2626',
                bg: dark ? '#1e1e30' : '#ffffff'
            };
        }

        let charts = {};

        function renderCharts() {
            const c = getColors();

            // Destroy old
            Object.values(charts).forEach(ch => ch.destroy());

            // 1. Payoffs Bar Chart
            charts.payoff = new Chart(document.getElementById('payoffChart'), {
                type: 'bar',
                data: {
                    labels: ['Bull', 'Base', 'Bear (-40%)', 'Tail Shock'],
                    datasets: chartData.payoffs.map((p, i) => ({
                        label: '$${p.name} (EV: $${p.ev})',
                        data: p.values,
                        backgroundColor: [c.primary, c.success, c.warning, c.danger][i % 4] + 'CC',
                        borderColor: [c.primary, c.success, c.warning, c.danger][i % 4],
                        borderWidth: 1
                    }))
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { color: c.text, font: { size: 10 } } } },
                    scales: {
                        y: { beginAtZero: true, grid: { color: c.grid }, ticks: { color: c.text } },
                        x: { grid: { color: c.grid }, ticks: { color: c.text } }
                    }
                }
            });

            // 2. Risk vs Reward Scatter
            charts.asymmetry = new Chart(document.getElementById('asymmetryChart'), {
                type: 'scatter',
                data: {
                    datasets: [{
                        label: 'Options',
                        data: chartData.asymmetry.map(a => ({ x: a.tail, y: a.ev, option: a.name })),
                        backgroundColor: chartData.asymmetry.map((_, i) => [c.primary, c.success, c.warning, c.danger][i % 4]),
                        borderColor: '#1a1a2e', borderWidth: 2,
                        pointRadius: 8, pointHoverRadius: 10
                    }]
                },
                options: {
                    responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { display: false }, tooltip: { callbacks: { label: ctx => '$${ctx.raw.option}: EV $${ctx.raw.y}, Risk $${ctx.raw.x}' } } },
                    scales: {
                        x: { title: { display: true, text: 'Worst-Case Downside (Right = Safer)', color: c.text }, grid: { color: c.grid }, ticks: { color: c.text } },
                        y: { title: { display: true, text: 'Expected Value (Higher = Better)', color: c.text }, grid: { color: c.grid }, ticks: { color: c.text } }
                    }
                }
            });

            // 3. Monte Carlo Horizontal Bar
            charts.monte = new Chart(document.getElementById('monteCarloChart'), {
                type: 'bar',
                data: {
                    labels: chartData.monteCarlo.map(m => m.name),
                    datasets: [
                        { label: 'P10 (Pessimistic)', data: chartData.monteCarlo.map(m => m.p10), backgroundColor: c.danger + '80', borderColor: c.danger, borderWidth: 1 },
                        { label: 'P50 (Median)', data: chartData.monteCarlo.map(m => m.p50), backgroundColor: c.primary + '80', borderColor: c.primary, borderWidth: 1 },
                        { label: 'P90 (Optimistic)', data: chartData.monteCarlo.map(m => m.p90), backgroundColor: c.success + '80', borderColor: c.success, borderWidth: 1 }
                    ]
                },
                options: {
                    responsive: true, maintainAspectRatio: false, indexAxis: 'y',
                    plugins: { legend: { position: 'bottom', labels: { color: c.text, font: { size: 10 } } } },
                    scales: { x: { grid: { color: c.grid }, ticks: { color: c.text } }, y: { grid: { color: c.grid }, ticks: { color: c.text } } }
                }
            });
        }

        // Re-render on theme change
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', renderCharts);

        // Init
        document.addEventListener('DOMContentLoaded', renderCharts);
    </script>
</body>
</html>"""


def generate_html_report(
    summary: Dict[str, Any],
    title: str = "Mastermind Decision Audit",
    output_path: str = "mastermind_report.html"
) -> str:
    """
    Generate a clean, accessible HTML report from Mastermind analysis.

    Args:
        summary: Analysis summary from analyze_options()
        title: Report title
        output_path: Output file path

    Returns:
        Path to generated HTML file
    """

    # Extract data
    trend = summary.get("trend_warning_radar", {})
    options = summary.get("options_analysis", {})

    # Badge
    badge = trend.get("badge", "UNSPECIFIED")
    if "GREEN" in badge:
        badge_class, badge_color, badge_text = "green", "#16a34a", "GREEN — Master Deeply"
    elif "AMBER" in badge:
        badge_class, badge_color, badge_text = "amber", "#d97706", "AMBER — Tactical 80/20 Only"
    elif "RED" in badge:
        badge_class, badge_color, badge_text = "red", "#dc2626", "RED — Pivot Away"
    else:
        badge_class, badge_color, badge_text = "", "#999", "Unspecified"

    # Key metrics
    best_ev = summary.get("best_ev_under_uncertainty", 0)
    evpi = summary.get("evpi_missing_data_value", 0)
    half_life = trend.get("estimated_half_life_years", "N/A")
    durability = trend.get("composite_durability_score", "N/A")

    metrics = trend.get("metrics_input", {})
    lindy_years = metrics.get("lindy_years", "N/A")
    hype_index = metrics.get("hype_inflation_index", "N/A")
    prod_adoption = metrics.get("production_adoption_score", "N/A")
    auto_vuln = metrics.get("automation_vulnerability", "N/A")

    ev_class = "good" if best_ev > 0 else "bad" if best_ev < 0 else ""
    durability_class = "good" if isinstance(durability, (int, float)) and durability >= 65 else "warning" if isinstance(durability, (int, float)) and durability >= 40 else "bad"

    directive = trend.get("strategic_directive", "No directive available.")

    # Build tables
    risk_table_rows = ""
    mc_table_rows = ""
    chart_payoffs = []
    chart_asymmetry = []
    chart_monte = []

    for name, data in options.items():
        payoffs = data.get("payoffs", [0,0,0,0])
        ev = data.get("expected_value", 0)
        convexity = data.get("convexity_ratio", "N/A")
        door = data.get("door_classification", "N/A")
        posture = data.get("recommended_posture", "N/A")
        max_downside = data.get("max_downside", 0)

        # Posture badge class
        posture_cls = "posture-probe"
        if "GO - HIGH" in posture: posture_cls = "posture-go"
        elif "AVOID" in posture: posture_cls = "posture-avoid"

        risk_table_rows += f"""
        <tr>
            <td><strong>{html.escape(name)}</strong></td>
            <td>{payoffs[0]:.0f}</td>
            <td>{payoffs[1]:.0f}</td>
            <td>{payoffs[2]:.0f}</td>
            <td>{payoffs[3]:.0f}</td>
            <td><strong>{ev:.1f}</strong></td>
            <td>{convexity if isinstance(convexity, str) else f"{convexity:.1f}"}</td>
            <td>{html.escape(door)}</td>
            <td><span class="posture {posture_cls}">{html.escape(posture.split("(")[0].strip())}</span></td>
        </tr>"""

        mc = data.get("monte_carlo_stress_test", {})
        mc_table_rows += f"""
        <tr>
            <td><strong>{html.escape(name)}</strong></td>
            <td>{mc.get('optimal_win_rate_pct', 0)}%</td>
            <td>{mc.get('tail_ruin_exposure_pct', 0)}%</td>
            <td>{mc.get('ev_p10_pessimistic', 0):.1f}</td>
            <td>{mc.get('ev_p50_median', 0):.1f}</td>
            <td>{mc.get('ev_p90_optimistic', 0):.1f}</td>
        </tr>"""

        chart_payoffs.append({"name": name, "values": payoffs, "ev": ev})
        chart_asymmetry.append({"name": name, "ev": ev, "tail": max_downside})
        chart_monte.append({
            "name": name,
            "p10": mc.get("ev_p10_pessimistic", 0),
            "p50": mc.get("ev_p50_median", 0),
            "p90": mc.get("ev_p90_optimistic", 0)
        })

    # Insights
    evpi_val = summary.get("evpi_missing_data_value", 0)
    if evpi_val >= 5:
        evpi_class, evpi_label = "danger", "HIGH — Missing Data Could Change Decision"
    else:
        evpi_class, evpi_label = "success", "LOW — Current Data Sufficient"
    evpi_directive = summary.get("missing_data_directive", "")

    survivorship_bias = "Success stories hide the many who tried and failed. The visible winners often had hidden advantages (capital, network, timing, prior expertise) that aren't obvious in retrospect."
    omitted_confounders = "What looks like skill may be luck + prerequisites. Always ask: what did the winners have that the silent failures didn't?"

    defense_question = "Explain the core mechanism of this skill from first principles — no jargon, no buzzwords."
    diagnostic_drill = "Build the smallest thing that proves you understand the 20% that delivers 80% of the value. Must work without tutorials."

    chart_data = {"payoffs": chart_payoffs, "asymmetry": chart_asymmetry, "monteCarlo": chart_monte}

    # Render
    template = Template(HTML_TEMPLATE)
    html_content = template.substitute(
        title=html.escape(title),
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
        badge_class=badge_class,
        badge_color=badge_color,
        badge_text=html.escape(badge_text),
        directive=html.escape(directive),
        best_ev=f"{best_ev:.1f}",
        evpi=f"{evpi:.1f}",
        half_life=str(half_life),
        durability=str(durability),
        lindy_years=str(lindy_years),
        hype_index=str(hype_index),
        prod_adoption=str(prod_adoption),
        auto_vuln=str(auto_vuln),
        ev_class=ev_class,
        durability_class=durability_class,
        risk_table_rows=risk_table_rows,
        mc_table_rows=mc_table_rows,
        evpi_class=evpi_class,
        evpi_label=evpi_label,
        evpi_directive=html.escape(evpi_directive),
        survivorship_bias=html.escape(survivorship_bias),
        omitted_confounders=html.escape(omitted_confounders),
        defense_question=html.escape(defense_question),
        diagnostic_drill=html.escape(diagnostic_drill),
        chart_data_json=json.dumps(chart_data)
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return output_path


if __name__ == "__main__":
    # Quick test
    test = {
        "scenarios": ["Bull", "Base", "Bear", "Tail"],
        "trend_warning_radar": {
            "badge": "GREEN: MASTER DEEPLY",
            "composite_durability_score": 75,
            "estimated_half_life_years": 10,
            "metrics_input": {"lindy_years": 12, "hype_inflation_index": 30, "production_adoption_score": 85, "automation_vulnerability": 20},
            "strategic_directive": "High durability, invest deeply."
        },
        "options_analysis": {
            "Full Commit": {"probabilities": [0.3,0.4,0.2,0.1], "payoffs": [90,55,10,-20], "expected_value": 45, "max_upside": 90, "max_downside": -20, "convexity_ratio": 4.5, "door_classification": "Type 2", "recommended_posture": "GO - HIGH CONVEXITY (Asymmetric Upside)", "monte_carlo_stress_test": {"optimal_win_rate_pct": 70, "tail_ruin_exposure_pct": 2, "ev_p10_pessimistic": 30, "ev_p50_median": 45, "ev_p90_optimistic": 60}},
            "Probe Only": {"probabilities": [0.3,0.4,0.2,0.1], "payoffs": [60,40,15,-5], "expected_value": 35, "max_upside": 60, "max_downside": -5, "convexity_ratio": 12, "door_classification": "Type 2", "recommended_posture": "GO - HIGH CONVEXITY (Asymmetric Upside)", "monte_carlo_stress_test": {"optimal_win_rate_pct": 30, "tail_ruin_exposure_pct": 0, "ev_p10_pessimistic": 25, "ev_p50_median": 35, "ev_p90_optimistic": 45}}
        },
        "best_ev_under_uncertainty": 45,
        "evpi_missing_data_value": 4,
        "missing_data_directive": "LOW EVPI: Proceed with top option."
    }
    generate_html_report(test, "Test Report", "test_simple.html")
    print("Generated test_simple.html")