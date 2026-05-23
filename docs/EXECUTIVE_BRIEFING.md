# Executive Briefing

## Product

ADAS Preventable Risk Detection Product: Secondary Crash Analysis

## Business Question

Assuming the first impact in a chain-reaction crash is unavoidable, how many secondary impacts could plausibly be prevented or reduced by existing ADAS technologies such as AEB, FCW, and ACC?

## Why It Matters

Secondary impacts can increase injury risk, road disruption, insurance exposure, and operational response cost. A repeatable analytical product helps risk teams understand where preventative technologies and behavioural interventions may reduce harm.

## Current Product Capability

The product currently provides:

- automated YouTube metadata extraction for validated dashcam and pile-up source videos
- a governed labelling schema for incident-level crash assessment
- a data dictionary and labelling guide for consistent manual review
- validation checks for critical fields and impossible impact counts
- summary risk metrics and weather-level preventability breakdowns
- an interactive Streamlit dashboard for stakeholder exploration
- tests, CI, reproducibility guidance, and QA documentation

## Current Dataset Position

The repo contains a tracked labelling template and a local generated metadata extract for 25 validated source videos. The final interview-ready target is 80-120 labelled crash incidents, with 80 as the minimum threshold.

Long compilation videos are handled at incident/timestamp level. One video may therefore contribute multiple labelled incidents.

## Analytical Controls

The project uses:

- explicit inclusion and exclusion criteria
- critical-field validation
- impact-count consistency checks
- documented ADAS decision rules
- documented uncertainty handling in `notes`
- CI-backed tests for loader, validation, analytics, extractor, and dashboard behaviour

## Limitations

The dataset is based on public video footage, so it may over-represent dramatic crashes, winter conditions, and countries where dashcam publication is common. ADAS preventability is an analytical judgement, not a legal or engineering determination.

## Recommended Next Step

Scale labelling to at least 80 incidents, review ambiguous rows, then use the dashboard and summary outputs to present initial preventability patterns by weather, road type, country, and human factor.
