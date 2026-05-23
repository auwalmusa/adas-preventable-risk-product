# Data Quality & QA Guide

## Purpose

The project depends on manually labelled crash incidents, so data quality is a core analytical risk. This guide defines the QA checks used to keep the labelled dataset consistent, auditable, and suitable for an HMRC Senior Data Analyst technical presentation.

## Critical Fields

The current validation module treats these fields as critical:

- `initial_impact_unavoidable`
- `secondary_preventable_by_adas`
- `num_total_impacts`
- `num_secondary_impacts`

Missing or inconsistent values in these fields directly affect headline metrics.

## Automated Checks

`src/validation.py` currently reports:

- total record count
- missing critical fields
- records where `num_secondary_impacts > num_total_impacts`
- percentage of records preventable or partially preventable by ADAS
- percentage of records with at least one secondary impact

These checks are covered by tests in `tests/test_validation.py` and `tests/test_phase4_pipeline.py`.

## Manual QA Rules

Each labelled row should be reviewed against these rules:

- `num_total_impacts` must include the first impact and all subsequent impacts.
- `num_secondary_impacts` must equal total impacts after the first impact.
- `num_secondary_impacts` must never exceed `num_total_impacts`.
- `secondary_preventable_by_adas` must be based on realistic current ADAS capabilities, not speculative future autonomy.
- If visibility is poor, record uncertainty in `notes` rather than forcing certainty.
- Long compilation videos must be labelled at incident/timestamp level, not as a single crash.

## Review Process

Use a two-pass process:

1. First pass: label each incident quickly but consistently.
2. Second pass: review rows with severe crashes, ambiguous preventability, or uncertain impact counts.

Rows needing later review should include `Needs review` in `notes`.

## Acceptance Threshold

For the interview-ready dataset:

- minimum 80 labelled incidents
- target 80-120 labelled incidents
- no invalid secondary-impact counts
- no missing critical fields
- clear notes for ambiguous cases

## Bias & Limitations

The dataset is based on public dashcam and traffic-camera footage. It may over-represent dramatic incidents, winter conditions, and countries with high dashcam publication rates. These limitations should be stated clearly in the presentation.
