# Mastermind v2.0.1 - Visualization Enhancement Plan

## Objective
Add interactive HTML webpage visualization of the solution/roadmap created by the Mastermind agent to improve user understanding and data visualization.

## Changes Required

### 1. New HTML Visualization Module (`scripts/visualization.py`)
- Create interactive HTML report generation
- Include:
  - Executive summary dashboard
  - Trend warning badge with color-coded indicators
  - Risk matrix visualization (interactive table)
  - EV/EVPI/Convexity charts using Chart.js
  - Monte Carlo results visualization
  - Learning roadmap timeline with phases
  - Responsive design (mobile-friendly)
  - Dark/light theme support

### 2. Update `scripts/risk_and_trend_analyzer.py`
- Add `--html` output option
- Integrate with new visualization module
- Support HTML chart generation alongside existing Matplotlib charts

### 3. Update `SKILL.md`
- Document new HTML visualization capability
- Add trigger examples for HTML reports
- Update execution workflow to mention HTML output

### 4. Update `CHANGELOG.md`
- Add v2.0.1 entry with new features

### 5. Update `assets/decision-and-mastery-report-template.md`
- Add HTML report section reference

## Technical Approach

### HTML Visualization Features:
1. **Executive Dashboard**: Summary cards with key metrics
2. **Trend Badge**: Animated GREEN/AMBER/RED indicator
3. **Risk Matrix**: Sortable, filterable table
4. **Charts**: Chart.js for EV distribution, Monte Carlo ranges, Asymmetry map
5. **Learning Roadmap**: Interactive timeline with phase expanders
6. **Export**: Print-friendly CSS, PDF generation via browser

### Dependencies:
- Chart.js (via CDN)
- No additional Python dependencies (generate static HTML)

## Implementation Steps

1. Create `scripts/visualization.py` with HTML template generation
2. Modify `risk_and_trend_analyzer.py` to import and use visualization module
3. Test with `--selftest` and example JSON payload
4. Update documentation files
5. Verify backwards compatibility

## Success Criteria
- [ ] HTML report generates without errors
- [ ] Interactive charts render correctly
- [ ] Works on mobile and desktop
- [ ] Dark/light theme toggle works
- [ ] All existing tests still pass
- [ ] New `--html` CLI option works