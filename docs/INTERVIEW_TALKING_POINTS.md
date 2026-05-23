# Interview Talking Points

## Short Project Summary

"I built an end-to-end analytical product to estimate preventable secondary crash risk from public dashcam footage. The product covers ingestion, labelling governance, validation, analysis, dashboard delivery, testing, CI, and reproducibility documentation."

## Why This Is Senior-Level

- It starts with a risk question, not a tool.
- It defines a data model and QA process before scaling analysis.
- It separates ingestion, validation, analysis, and dashboard layers.
- It uses tests and CI to make the product maintainable.
- It documents limitations and uncertainty rather than hiding them.

## Strong Technical Points

- `yt-dlp` automation extracts metadata for source videos.
- The extractor validates YouTube IDs and logs extraction errors.
- The loader standardises schema and parses dates.
- Validation catches missing critical fields and invalid impact counts.
- Analysis produces repeatable headline metrics and breakdowns.
- The dashboard consumes tested pipeline functions rather than duplicating logic.
- CI runs linting, formatting checks, and tests on every push and pull request.

## Data Governance Points

- Publicly available videos only.
- Incident-level labelling for compilations.
- Clear inclusion and exclusion criteria.
- Explicit ADAS preventability decision rules.
- Uncertain cases documented in `notes`.
- Raw generated metadata ignored, tracked template retained.

## How To Explain The Dataset Size

"The target is not thousands of videos. For this presentation, the right target is 80-120 carefully labelled incidents. That is enough to show credible proportions and segmentation while keeping the labelling quality high."

## How To Handle Challenge Questions

### Is this computer vision?

"No. Full computer vision is deliberately out of scope. This project focuses on the analytical product: sourcing, labelling, validating, analysing, and presenting evidence. Computer vision would be a future enhancement."

### How do you avoid subjective labels?

"I use a data dictionary, labelling guide, decision rules, QA checks, and notes for ambiguous cases. For a production version, I would add second-review sampling and inter-rater agreement checks."

### Why YouTube data?

"It is an accessible public proxy dataset for a portfolio product. I document the sampling limitations clearly and avoid claiming it is nationally representative."

### What would you do next?

"Scale to at least 80 labelled incidents, add confidence intervals, broaden segmentation, review ambiguous rows, and produce a concise executive briefing for stakeholders."

### How does this relate to HMRC?

"The domain is road risk, but the method is directly transferable: define a preventative risk question, build a governed dataset, validate quality, generate risk profiles, and deliver reproducible insight to decision makers."

## Closing Line

"The project demonstrates the full analytical lifecycle: problem framing, governed data acquisition, tested analysis, dashboard delivery, and clear communication of limitations and next steps."
