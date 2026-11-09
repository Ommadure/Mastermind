#!/usr/bin/env python3
"""
Mastermind HTML Visualization Generator
Version: 2.0.1
License: MIT

Generates interactive HTML reports from Mastermind analysis results.
Uses Chart.js for interactive visualizations (loaded via CDN).
"""

import json
import html
from typing import Dict, Any, List, Optional
from datetime import datetime
from string import Template


# HTML Template with embedded CSS and Chart.js
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
        :root {
            --bg-primary: #F8FAFC;
            --bg-secondary: #FFFFFF;
            --bg-card: #FFFFFF;
            --text-primary: #0F172A;
            --text-secondary: #475569;
            --text-muted: #94A3B8;
            --border-color: #E2E8F0;
            --accent-blue: #1E3A8A;
            --accent-teal: #0D9488;
            --accent-amber: #D97706;
            --accent-red: #DC2626;
            --accent-green: #16A34A;
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
            --radius: 8px;
            --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
            --font-sans: system-ui, -apple-system, sans-serif;
        }

        [data-theme="dark"] {
            --bg-primary: #0F172A;
            --bg-secondary: #1E293B;
            --bg-card: #1E293B;
            --text-primary: #F1F5F9;
            --text-secondary: #CBD5E1;
            --text-muted: #64748B;
            --border-color: #334155;
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.4);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: var(--font-sans);
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            transition: background 0.3s, color 0.3s;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 24px;
        }

        /* Header */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 32px;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border-color);
            flex-wrap: wrap;
            gap: 16px;
        }

        .header h1 {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .header .meta {
            color: var(--text-secondary);
            font-size: 0.875rem;
        }

        .theme-toggle {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            padding: 8px 16px;
            cursor: pointer;
            font-size: 0.875rem;
            color: var(--text-primary);
            transition: all 0.2s;
        }

        .theme-toggle:hover {
            background: var(--bg-card);
            border-color: var(--accent-blue);
        }

        /* Badge */
        .badge-container {
            margin-bottom: 32px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            padding: 16px 24px;
            border-radius: var(--radius);
            font-weight: 600;
            font-size: 1rem;
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.85; }
        }

        .badge.GREEN { background: #DCFCE7; color: #166534; border: 2px solid #16A34A; }
        .badge.AMBER { background: #FEF3C7; color: #92400E; border: 2px solid #D97706; }
        .badge.RED { background: #FEE2E2; color: #991B1B; border: 2px solid #DC2626; }
        .badge.UNSPECIFIED { background: #F1F5F9; color: #475569; border: 2px solid #94A3B8; }

        [data-theme="dark"] .badge.GREEN { background: #14532D; color: #86EFAC; border-color: #22C55E; }
        [data-theme="dark"] .badge.AMBER { background: #78350F; color: #FDE047; border-color: #F59E0B; }
        [data-theme="dark"] .badge.RED { background: #7F1D1D; color: #FCA5A5; border-color: #EF4444; }
        [data-theme="dark"] .badge.UNSPECIFIED { background: #334155; color: #94A3B8; border-color: #64748B; }

        .badge-icon {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            flex-shrink: 0;
        }

        /* Grid Layout */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
            margin-bottom: 32px;
        }

        .card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            padding: 24px;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.2s;
        }

        .card:hover { box-shadow: var(--shadow-md); }

        .card h2 {
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 16px;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .card h2::before {
            content: "";
            width: 4px;
            height: 20px;
            background: var(--accent-blue);
            border-radius: 2px;
        }

        /* Metrics Cards */
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 16px;
        }

        .metric {
            text-align: center;
            padding: 16px;
            background: var(--bg-secondary);
            border-radius: var(--radius);
            border: 1px solid var(--border-color);
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            font-family: var(--font-mono);
            line-height: 1.2;
        }

        .metric-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 4px;
        }

        .metric.GREEN .metric-value { color: #16A34A; }
        .metric.AMBER .metric-value { color: #D97706; }
        .metric.RED .metric-value { color: #DC2626; }

        /* Charts */
        .chart-container {
            position: relative;
            height: 300px;
            width: 100%;
        }

        .chart-wrapper {
            grid-column: 1 / -1;
        }

        /* Tables */
        .table-container {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.875rem;
        }

        th, td {
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }

        th {
            background: var(--bg-secondary);
            font-weight: 600;
            color: var(--text-secondary);
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            position: sticky;
            top: 0;
        }

        tr:hover td { background: var(--bg-secondary); }

        .posture-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .posture-GO { background: #DCFCE7; color: #166534; }
        .posture-PROBE { background: #FEF3C7; color: #92400E; }
        .posture-REJECT { background: #FEE2E2; color: #991B1B; }
        .posture-AVOID { background: #F1F5F9; color: #475569; }

        [data-theme="dark"] .posture-GO { background: #14532D; color: #86EFAC; }
        [data-theme="dark"] .posture-PROBE { background: #78350F; color: #FDE047; }
        [data-theme="dark"] .posture-REJECT { background: #7F1D1D; color: #FCA5A5; }
        [data-theme="dark"] .posture-AVOID { background: #334155; color: #94A3B8; }

        /* Roadmap Timeline */
        .timeline {
            position: relative;
            padding-left: 24px;
        }

        .timeline::before {
            content: "";
            position: absolute;
            left: 8px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--border-color);
        }

        .timeline-item {
            position: relative;
            padding-bottom: 32px;
        }

        .timeline-item:last-child { padding-bottom: 0; }

        .timeline-marker {
            position: absolute;
            left: -20px;
            top: 4px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            border: 3px solid var(--bg-card);
            z-index: 1;
        }

        .timeline-marker.GREEN { background: #16A34A; }
        .timeline-marker.AMBER { background: #D97706; }
        .timeline-marker.RED { background: #DC2626; }

        .timeline-content {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            padding: 16px;
        }

        .timeline-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 8px;
        }

        .timeline-title {
            font-weight: 600;
            font-size: 1rem;
        }

        .timeline-duration {
            font-size: 0.8rem;
            color: var(--text-muted);
            background: var(--bg-primary);
            padding: 2px 8px;
            border-radius: 4px;
        }

        .timeline-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            font-size: 0.875rem;
        }

        .detail-item {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .detail-label {
            font-size: 0.7rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .detail-value { color: var(--text-primary); }

        /* Shadow Data & EVPI */
        .shadow-item {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            padding: 16px;
            margin-bottom: 12px;
        }

        .shadow-item h4 {
            font-weight: 600;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .shadow-item h4::before {
            content: "";
            width: 8px;
            height: 8px;
            border-radius: 2px;
        }

        .shadow-survivorship h4::before { background: #DC2626; }
        .shadow-confounders h4::before { background: #D97706; }
        .shadow-evpi h4::before { background: #0D9488; }

        /* Legend */
        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid var(--border-color);
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.875rem;
        }

        .legend-color {
            width: 16px;
            height: 16px;
            border-radius: 4px;
        }

        /* Footer */
        .footer {
            margin-top: 48px;
            padding-top: 24px;
            border-top: 1px solid var(--border-color);
            text-align: center;
            color: var(--text-muted);
            font-size: 0.875rem;
        }

        .footer a { color: var(--accent-blue); }

        /* Collapsible Sections */
        .collapsible {
            cursor: pointer;
            user-select: none;
        }

        .collapsible-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
        }

        .collapsible[aria-expanded="true"] .collapsible-content {
            max-height: 2000px;
            transition: max-height 0.5s ease-in;
        }

        .collapsible-toggle {
            display: inline-block;
            transition: transform 0.2s;
        }

        .collapsible[aria-expanded="true"] .collapsible-toggle {
            transform: rotate(90deg);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .container { padding: 16px; }
            .header { flex-direction: column; align-items: flex-start; }
            .grid { grid-template-columns: 1fr; }
            .metrics-grid { grid-template-columns: repeat(2, 1fr); }
            .chart-container { height: 250px; }
            .timeline { padding-left: 16px; }
        }

        /* Print Styles */
        @media print {
            .theme-toggle { display: none; }
            .card { break-inside: avoid; page-break-inside: avoid; }
            body { background: white; color: black; }
            .badge { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div>
                <h1>${title}</h1>
                <div class="meta">Generated: ${timestamp} | Mastermind v2.0.1</div>
            </div>
            <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme">
                <span id="theme-icon">🌙</span> <span id="theme-text">Dark</span>
            </button>
        </header>

        <!-- Trend Badge -->
        <div class="badge-container">
            <div class="badge ${badge_class}">
                <span class="badge-icon" style="background: ${badge_color};"></span>
                <span>${badge_text}</span>
            </div>
        </div>

        <!-- Executive Metrics -->
        <div class="grid">
            <div class="card">
                <h2>Key Metrics</h2>
                <div class="metrics-grid">
                    <div class="metric ${ev_class}">
                        <div class="metric-value">${best_ev}</div>
                        <div class="metric-label">Best EV</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">${evpi}</div>
                        <div class="metric-label">EVPI</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">${half_life}</div>
                        <div class="metric-label">Half-Life (yrs)</div>
                    </div>
                    <div class="metric ${durability_class}">
                        <div class="metric-value">${durability}</div>
                        <div class="metric-label">Durability</div>
                    </div>
                </div>
            </div>

            <div class="card">
                <h2>Trend Analysis</h2>
                <div class="metrics-grid">
                    <div class="metric">
                        <div class="metric-value">${lindy_years}</div>
                        <div class="metric-label">Lindy Years</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">${hype_index}</div>
                        <div class="metric-label">Hype Index</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">${prod_adoption}</div>
                        <div class="metric-label">Prod Adoption</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">${auto_vuln}</div>
                        <div class="metric-label">Auto Vuln.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Charts Row -->
        <div class="grid">
            <div class="card chart-wrapper">
                <h2>Regime Payoffs</h2>
                <div class="chart-container">
                    <canvas id="payoffChart"></canvas>
                </div>
            </div>

            <div class="card chart-wrapper">
                <h2>Asymmetry Map (EV vs Tail Risk)</h2>
                <div class="chart-container">
                    <canvas id="asymmetryChart"></canvas>
                </div>
            </div>

            <div class="card chart-wrapper">
                <h2>Monte Carlo Robustness</h2>
                <div class="chart-container">
                    <canvas id="monteCarloChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Risk Matrix Table -->
        <div class="card">
            <h2>Strategic Options Risk Matrix</h2>
            <div class="table-container">
                <table id="riskTable">
                    <thead>
                        <tr>
                            <th>Option</th>
                            <th>Bull Payoff</th>
                            <th>Base Payoff</th>
                            <th>Bear (-40%)</th>
                            <th>Tail Shock</th>
                            <th>EV</th>
                            <th>Convexity</th>
                            <th>Door Type</th>
                            <th>Posture</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${risk_table_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Monte Carlo Details -->
        <div class="grid">
            <div class="card">
                <h2>Monte Carlo Stress Test Results</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Option</th>
                                <th>Win Rate</th>
                                <th>Tail Ruin Risk</th>
                                <th>P10 (Pessimistic)</th>
                                <th>P50 (Median)</th>
                                <th>P90 (Optimistic)</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${mc_table_rows}
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card">
                <h2>Missing Data & EVPI</h2>
                <div class="shadow-item shadow-evpi">
                    <h4>Expected Value of Perfect Information</h4>
                    <p><strong>EVPI:</strong> ${evpi}</p>
                    <p><strong>Directive:</strong> ${evpi_directive}</p>
                </div>
                <div class="shadow-item shadow-survivorship">
                    <h4>Survivorship Bias (Unobserved Graveyard)</h4>
                    <p>${survivorship_bias}</p>
                </div>
                <div class="shadow-item shadow-confounders">
                    <h4>Omitted Confounders</h4>
                    <p>${omitted_confounders}</p>
                </div>
            </div>
        </div>

        <!-- Learning Roadmap -->
        <div class="card">
            <h2>Zero-Cost 80/20 Mastery Roadmap</h2>
            <div class="timeline">
                ${roadmap_timeline}
            </div>
        </div>

        <!-- Pre-Mortem & Consequences -->
        <div class="grid">
            <div class="card collapsible" onclick="toggleCollapse(this)" aria-expanded="false">
                <h2 class="collapsible-header">
                    <span class="collapsible-toggle">▶</span> Pre-Mortem & Consequence Horizon
                </h2>
                <div class="collapsible-content">
                    <div class="shadow-item">
                        <h4>Top Failure Modes & Mitigations</h4>
                        <p>${failure_modes}</p>
                    </div>
                    <div class="shadow-item">
                        <h4>1st / 2nd / 3rd-Order Consequences</h4>
                        <p>${consequences}</p>
                    </div>
                </div>
            </div>

            <div class="card collapsible" onclick="toggleCollapse(this)" aria-expanded="false">
                <h2 class="collapsible-header">
                    <span class="collapsible-toggle">▶</span> Crucible Gate #1
                </h2>
                <div class="collapsible-content">
                    <div class="shadow-item">
                        <h4>First-Principles Defense Question</h4>
                        <p>${defense_question}</p>
                    </div>
                    <div class="shadow-item">
                        <h4>Hands-On Build / Diagnostic Drill</h4>
                        <p>${diagnostic_drill}</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="footer">
            <p>Generated by <strong>Mastermind v2.0.1</strong> — Rational Strategic Decision Engine</p>
            <p>MIT Licensed | <a href="https://github.com/mastermind-skill" target="_blank">Source Code</a> | <a href="#" onclick="window.print()">Print Report</a></p>
        </footer>
    </div>

    <script>
        // Data injection
        const chartData = ${chart_data_json};

        // Theme Management
        function toggleTheme() {
            const html = document.documentElement;
            const icon = document.getElementById('theme-icon');
            const text = document.getElementById('theme-text');

            if (html.getAttribute('data-theme') === 'dark') {
                html.removeAttribute('data-theme');
                icon.textContent = '🌙';
                text.textContent = 'Dark';
                localStorage.setItem('theme', 'light');
            } else {
                html.setAttribute('data-theme', 'dark');
                icon.textContent = '☀️';
                text.textContent = 'Light';
                localStorage.setItem('theme', 'dark');
            }

            // Re-render charts with new colors
            renderAllCharts();
        }

        // Load saved theme
        if (localStorage.getItem('theme') === 'dark' ||
            (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.setAttribute('data-theme', 'dark');
            document.getElementById('theme-icon').textContent = '☀️';
            document.getElementById('theme-text').textContent = 'Light';
        }

        // Collapsible Sections
        function toggleCollapse(element) {
            const expanded = element.getAttribute('aria-expanded') === 'true';
            element.setAttribute('aria-expanded', !expanded);
        }

        // Chart Colors (theme-aware)
        function getChartColors() {
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            return {
                gridColor: isDark ? '#334155' : '#E2E8F0',
                textColor: isDark ? '#CBD5E1' : '#475569',
                accentBlue: '#1E3A8A',
                accentTeal: '#0D9488',
                accentAmber: '#D97706',
                accentRed: '#DC2626',
                accentGreen: '#16A34A',
                bgColor: isDark ? '#1E293B' : '#FFFFFF'
            };
        }

        // Chart Instances
        let payoffChart = null;
        let asymmetryChart = null;
        let monteCarloChart = null;

        function renderAllCharts() {
            const colors = getChartColors();

            // Destroy existing
            if (payoffChart) payoffChart.destroy();
            if (asymmetryChart) asymmetryChart.destroy();
            if (monteCarloChart) monteCarloChart.destroy();

            // Chart 1: Payoffs by Regime
            payoffChart = new Chart(
                document.getElementById('payoffChart'),
                {
                    type: 'bar',
                    data: {
                        labels: ['Bull', 'Base', 'Bear (-40%)', 'Tail Shock'],
                        datasets: chartData.payoffs.map((p, i) => ({
                            label: `$${p.name} (EV: $${p.ev})`,
                            data: p.values,
                            backgroundColor: [
                                colors.accentBlue,
                                colors.accentTeal,
                                colors.accentAmber,
                                colors.accentRed
                            ][i % 4] + 'CC',
                            borderColor: [
                                colors.accentBlue,
                                colors.accentTeal,
                                colors.accentAmber,
                                colors.accentRed
                            ][i % 4],
                            borderWidth: 1
                        }))
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { position: 'bottom', labels: { color: colors.textColor, font: { size: 10 } } },
                            title: { display: false }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                grid: { color: colors.gridColor },
                                ticks: { color: colors.textColor }
                            },
                            x: {
                                grid: { color: colors.gridColor },
                                ticks: { color: colors.textColor }
                            }
                        }
                    }
                }
            );

            // Chart 2: Asymmetry Map
            asymmetryChart = new Chart(
                document.getElementById('asymmetryChart'),
                {
                    type: 'scatter',
                    data: {
                        datasets: [{
                            label: 'Options',
                            data: chartData.asymmetry.map(a => ({
                                x: a.tail,
                                y: a.ev,
                                option: a.name
                            })),
                            backgroundColor: chartData.asymmetry.map((a, i) => [
                                colors.accentBlue,
                                colors.accentTeal,
                                colors.accentAmber,
                                colors.accentRed
                            ][i % 4]),
                            borderColor: '#0F172A',
                            borderWidth: 2,
                            pointRadius: 8,
                            pointHoverRadius: 10
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: ctx => `$${ctx.raw.option}: EV=$${ctx.raw.y}, Tail=$${ctx.raw.x}`
                                }
                            }
                        },
                        scales: {
                            x: {
                                title: { display: true, text: 'Worst-Case Tail Consequence (Right = Safer)', color: colors.textColor },
                                grid: { color: colors.gridColor },
                                ticks: { color: colors.textColor }
                            },
                            y: {
                                title: { display: true, text: 'Expected Value (EV)', color: colors.textColor },
                                grid: { color: colors.gridColor },
                                ticks: { color: colors.textColor }
                            }
                        }
                    }
                }
            );

            // Chart 3: Monte Carlo
            monteCarloChart = new Chart(
                document.getElementById('monteCarloChart'),
                {
                    type: 'bar',
                    data: {
                        labels: chartData.monteCarlo.map(m => m.name),
                        datasets: [
                            {
                                label: 'P10 (Pessimistic)',
                                data: chartData.monteCarlo.map(m => m.p10),
                                backgroundColor: colors.accentRed + '80',
                                borderColor: colors.accentRed,
                                borderWidth: 1
                            },
                            {
                                label: 'P50 (Median)',
                                data: chartData.monteCarlo.map(m => m.p50),
                                backgroundColor: colors.accentBlue + '80',
                                borderColor: colors.accentBlue,
                                borderWidth: 1
                            },
                            {
                                label: 'P90 (Optimistic)',
                                data: chartData.monteCarlo.map(m => m.p90),
                                backgroundColor: colors.accentGreen + '80',
                                borderColor: colors.accentGreen,
                                borderWidth: 1
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        indexAxis: 'y',
                        plugins: {
                            legend: { position: 'bottom', labels: { color: colors.textColor, font: { size: 10 } } }
                        },
                        scales: {
                            x: {
                                grid: { color: colors.gridColor },
                                ticks: { color: colors.textColor }
                            },
                            y: {
                                grid: { color: colors.gridColor },
                                ticks: { color: colors.textColor }
                            }
                        }
                    }
                }
            );
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            renderAllCharts();

            // Keyboard navigation for collapsibles
            document.querySelectorAll('.collapsible').forEach(el => {
                el.addEventListener('keydown', e => {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        toggleCollapse(el);
                    }
                });
            });
        });

        // Handle theme change for charts
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        mediaQuery.addEventListener('change', () => {
            if (!localStorage.getItem('theme')) {
                renderAllCharts();
            }
        });
    </script>
</body>
</html>"""


def generate_html_report(
    summary: Dict[str, Any],
    title: str = "Mastermind Epistemic Risk & Trend Forensics Audit",
    output_path: str = "mastermind_report.html"
) -> str:
    """
    Generate an interactive HTML report from the Mastermind analysis summary.

    Args:
        summary: The analysis summary from analyze_options()
        title: Report title
        output_path: Path to save the HTML file

    Returns:
        Path to the generated HTML file
    """

    # Extract data from summary
    trend = summary.get("trend_warning_radar", {})
    options = summary.get("options_analysis", {})
    scenarios = summary.get("scenarios", ["Bull Regime", "Base Regime", "Bear (Forecast Off 40%+)", "Tail Shock"])

    # Badge info
    badge = trend.get("badge", "UNSPECIFIED")
    if "GREEN" in badge:
        badge_class = "GREEN"
        badge_color = "#16A34A"
    elif "AMBER" in badge:
        badge_class = "AMBER"
        badge_color = "#D97706"
    elif "RED" in badge:
        badge_class = "RED"
        badge_color = "#DC2626"
    else:
        badge_class = "UNSPECIFIED"
        badge_color = "#94A3B8"

    # Metrics
    best_ev = summary.get("best_ev_under_uncertainty", 0)
    evpi = summary.get("evpi_missing_data_value", 0)
    half_life = trend.get("estimated_half_life_years", "N/A")
    durability = trend.get("composite_durability_score", "N/A")

    metrics = trend.get("metrics_input", {})
    lindy_years = metrics.get("lindy_years", "N/A")
    hype_index = metrics.get("hype_inflation_index", "N/A")
    prod_adoption = metrics.get("production_adoption_score", "N/A")
    auto_vuln = metrics.get("automation_vulnerability", "N/A")

    # Determine metric classes
    ev_class = "GREEN" if best_ev > 0 else "RED" if best_ev < 0 else ""
    durability_class = "GREEN" if isinstance(durability, (int, float)) and durability >= 65 else "AMBER" if isinstance(durability, (int, float)) and durability >= 40 else "RED"

    # Build risk table rows
    risk_table_rows = ""
    chart_payoffs = []
    chart_asymmetry = []
    chart_monte_carlo = []

    colors = ["#1E3A8A", "#0D9488", "#D97706", "#DC2626"]

    for idx, (name, data) in enumerate(options.items()):
        probs = data.get("probabilities", [0,0,0,0])
        payoffs = data.get("payoffs", [0,0,0,0])
        ev = data.get("expected_value", 0)
        convexity = data.get("convexity_ratio", "N/A")
        door = data.get("door_classification", "N/A")
        posture = data.get("recommended_posture", "N/A")
        max_downside = data.get("max_downside", 0)

        # Posture class for badge
        posture_class = ""
        if "GO" in posture and "HIGH" in posture:
            posture_class = "posture-GO"
        elif "PROBE" in posture:
            posture_class = "posture-PROBE"
        elif "REJECT" in posture or "HEDGE" in posture:
            posture_class = "posture-REJECT"
        elif "AVOID" in posture:
            posture_class = "posture-AVOID"

        risk_table_rows += f"""
        <tr>
            <td><strong>{html.escape(name)}</strong></td>
            <td>{payoffs[0]:.1f}</td>
            <td>{payoffs[1]:.1f}</td>
            <td>{payoffs[2]:.1f}</td>
            <td>{payoffs[3]:.1f}</td>
            <td><strong>{ev:.1f}</strong></td>
            <td>{convexity if isinstance(convexity, str) else f"{convexity:.2f}"}</td>
            <td>{html.escape(door)}</td>
            <td><span class="posture-badge {posture_class}">{html.escape(posture.split()[0])}</span></td>
        </tr>"""

        # Chart data
        chart_payoffs.append({
            "name": name,
            "values": payoffs,
            "ev": ev
        })

        chart_asymmetry.append({
            "name": name,
            "ev": ev,
            "tail": max_downside
        })

        mc = data.get("monte_carlo_stress_test", {})
        chart_monte_carlo.append({
            "name": name,
            "p10": mc.get("ev_p10_pessimistic", 0),
            "p50": mc.get("ev_p50_median", 0),
            "p90": mc.get("ev_p90_optimistic", 0)
        })

    # Monte Carlo table rows
    mc_table_rows = ""
    for name, data in options.items():
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

    # Shadow data
    survivorship_bias = "Historical attrition rates and silent dropouts not visible in success stories. Winners' narratives omit the graveyard of failed attempts with identical starting conditions."
    omitted_confounders = "Prerequisites (capital, network, prior domain expertise), timing luck, and survivorship selection effects often masquerade as skill in retrospective analyses."
    evpi_directive = summary.get("missing_data_directive", "No directive available.")

    # Roadmap (placeholder - in real usage, this would come from Stage 4)
    roadmap_timeline = """
    <div class="timeline-item">
        <div class="timeline-marker GREEN"></div>
        <div class="timeline-content">
            <div class="timeline-header">
                <span class="timeline-title">Phase 1: Foundations</span>
                <span class="timeline-duration">20-40 hrs</span>
            </div>
            <div class="timeline-details">
                <div class="detail-item">
                    <span class="detail-label">Focus</span>
                    <span class="detail-value">Core Concepts & Mental Models</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Sources</span>
                    <span class="detail-value">Tier 1A Official Specs/Docs</span>
                </div>
            </div>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-marker AMBER"></div>
        <div class="timeline-content">
            <div class="timeline-header">
                <span class="timeline-title">Phase 2: Core Execution</span>
                <span class="timeline-duration">40-80 hrs</span>
            </div>
            <div class="timeline-details">
                <div class="detail-item">
                    <span class="detail-label">Focus</span>
                    <span class="detail-value">Applied Procedures & Edge Cases</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Sources</span>
                    <span class="detail-value">Tier 1B OCW & Papers</span>
                </div>
            </div>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-marker RED"></div>
        <div class="timeline-content">
            <div class="timeline-header">
                <span class="timeline-title">Phase 3: Production Mastery</span>
                <span class="timeline-duration">80-160 hrs</span>
            </div>
            <div class="timeline-details">
                <div class="detail-item">
                    <span class="detail-label">Focus</span>
                    <span class="detail-value">System Integration & Stress Testing</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Sources</span>
                    <span class="detail-value">Tier 1C Open Textbooks/Sandboxes</span>
                </div>
            </div>
        </div>
    </div>"""

    # Pre-mortem placeholders
    failure_modes = "1. Underestimating prerequisite knowledge gap — Mitigation: Diagnostic pre-assessment before Phase 1. 2. Resource depletion before verification gate — Mitigation: Time-box each phase with hard stop criteria."
    consequences = "Immediate: Time/capital loss. 2nd-order: Opportunity cost of alternative skills. 3rd-order: Career trajectory divergence if hype trap not identified."
    defense_question = "Explain the core mechanism of [skill] from first principles without using any domain-specific jargon or buzzwords."
    diagnostic_drill = "Build a minimal working artifact demonstrating the 20% of [skill] that delivers 80% of value. Must pass automated verification test."

    # Prepare chart data JSON
    chart_data = {
        "payoffs": chart_payoffs,
        "asymmetry": chart_asymmetry,
        "monteCarlo": chart_monte_carlo
    }

    # Render template
    template = Template(HTML_TEMPLATE)
    html_content = template.substitute(
        title=html.escape(title),
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        badge_class=badge_class,
        badge_color=badge_color,
        badge_text=html.escape(badge),
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
        survivorship_bias=html.escape(survivorship_bias),
        omitted_confounders=html.escape(omitted_confounders),
        evpi_directive=html.escape(evpi_directive),
        roadmap_timeline=roadmap_timeline,
        failure_modes=html.escape(failure_modes),
        consequences=html.escape(consequences),
        defense_question=html.escape(defense_question),
        diagnostic_drill=html.escape(diagnostic_drill),
        chart_data_json=json.dumps(chart_data)
    )

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return output_path


# For direct testing
if __name__ == "__main__":
    import sys

    # Test with sample data
    test_summary = {
        "scenarios": ["Bull Regime", "Base Regime", "Bear (Forecast Off 40%+)", "Tail Shock"],
        "trend_warning_radar": {
            "badge": "GREEN: MASTER DEEPLY",
            "composite_durability_score": 72.5,
            "estimated_half_life_years": 12.3,
            "metrics_input": {
                "lindy_years": 11,
                "hype_inflation_index": 35,
                "production_adoption_score": 82,
                "automation_vulnerability": 20
            },
            "strategic_directive": "High structural durability and asymmetric career leverage."
        },
        "options_analysis": {
            "Master Deeply": {
                "probabilities": [0.35, 0.40, 0.15, 0.10],
                "payoffs": [90, 55, 10, -20],
                "expected_value": 48.25,
                "max_upside": 90,
                "max_downside": -20,
                "convexity_ratio": 4.5,
                "door_classification": "Type 2 (Reversible / Capped Downside)",
                "recommended_posture": "GO - HIGH CONVEXITY (Asymmetric Upside)",
                "monte_carlo_stress_test": {
                    "optimal_win_rate_pct": 68.5,
                    "tail_ruin_exposure_pct": 2.1,
                    "ev_p10_pessimistic": 32.1,
                    "ev_p50_median": 47.8,
                    "ev_p90_optimistic": 65.4
                }
            },
            "Tactical 80/20 Probe": {
                "probabilities": [0.35, 0.40, 0.15, 0.10],
                "payoffs": [65, 45, 20, -5],
                "expected_value": 41.75,
                "max_upside": 65,
                "max_downside": -5,
                "convexity_ratio": 13.0,
                "door_classification": "Type 2 (Reversible / Capped Downside)",
                "recommended_posture": "GO - HIGH CONVEXITY (Asymmetric Upside)",
                "monte_carlo_stress_test": {
                    "optimal_win_rate_pct": 31.5,
                    "tail_ruin_exposure_pct": 0.0,
                    "ev_p10_pessimistic": 28.4,
                    "ev_p50_median": 41.2,
                    "ev_p90_optimistic": 55.8
                }
            }
        },
        "best_ev_under_uncertainty": 48.25,
        "ev_with_perfect_information": 55.2,
        "evpi_missing_data_value": 6.95,
        "missing_data_directive": "HIGH EVPI: Missing data can flip this decision. Run a 24-72h micro-experiment before full commitment."
    }

    output = generate_html_report(test_summary, "Test Mastermind Report", "test_report.html")
    print(f"Generated: {output}")