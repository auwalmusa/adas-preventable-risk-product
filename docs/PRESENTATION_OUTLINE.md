# Presentation Outline

## Slide 1 - Title

ADAS Preventable Risk Detection Product

Subtitle: Secondary crash analysis for risk intelligence

## Slide 2 - Business Problem

Question: when the first impact is unavoidable, how many secondary impacts could current ADAS plausibly prevent?

Key points:

- chain-reaction crashes compound risk
- secondary impacts are often behaviourally or technologically preventable
- the product converts public crash footage into structured risk evidence

## Slide 3 - Product Scope

End-to-end lifecycle:

- source discovery
- metadata extraction
- incident labelling
- data validation
- risk analysis
- dashboard delivery
- testing and reproducibility

## Slide 4 - Data Acquisition

Show:

- `src/youtube_extractor.py`
- 25 validated seed videos
- metadata and error outputs

Message: repeatable ingestion, not manual spreadsheet collection.

## Slide 5 - Data Model & Governance

Show:

- data dictionary
- labelling guide
- QA guide

Message: the manual labelling process is controlled, documented, and auditable.

## Slide 6 - Analytical Pipeline

Show:

- loader
- validation
- analysis modules

Message: dashboard logic is backed by tested Python modules.

## Slide 7 - Data Quality Controls

Highlight:

- missing critical fields
- invalid impact counts
- preventability categories
- timestamp-level incident tracking

Message: quality control is built into the product.

## Slide 8 - Dashboard Demo

Show:

- headline metrics
- QA snapshot
- preventability distribution
- weather breakdown
- dataset preview

Message: stakeholders can inspect both insight and data quality.

## Slide 9 - Testing & Reproducibility

Show:

- 13 passing tests
- GitHub Actions CI
- reproducibility guide

Message: the product can be maintained and rerun.

## Slide 10 - Limitations & Next Steps

Limitations:

- public dashcam sampling bias
- manual judgement in ADAS preventability
- final dataset still needs scaling

Next steps:

- label 80-120 incidents
- add confidence intervals
- segment by weather, road type, country, and human factor
- add exportable executive summary

## Slide 11 - Closing

Core message:

"This demonstrates senior-level analytical ownership: framing the risk problem, building the pipeline, governing the data, validating quality, and delivering insight through a reproducible product."
