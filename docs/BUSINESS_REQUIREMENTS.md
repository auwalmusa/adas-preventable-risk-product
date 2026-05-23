# Business Requirements

## Project Title

ADAS Preventable Risk Detection Product: Secondary Crash Analysis

## Business Problem

Chain-reaction crashes can produce multiple secondary impacts after the initial collision. These later impacts may increase injury risk, vehicle damage, road disruption, insurance exposure, and operational response demand.

The central business question is:

> Assuming the first impact is unavoidable, how many secondary impacts could plausibly be prevented or reduced by existing ADAS technologies such as Automatic Emergency Braking, Forward Collision Warning, and Adaptive Cruise Control?

## Business Objective

Build a reproducible analytical product that helps risk and intelligence stakeholders:

- quantify preventable secondary crash risk
- identify high-risk conditions such as weather, road type, and human factors
- review evidence through an interactive dashboard
- understand limitations, assumptions, and uncertainty

## Stakeholders

- Risk and intelligence analysts
- Preventative risking teams
- Operational decision makers
- Senior leaders reviewing risk trends and interventions

## Users

The primary user is an analyst or risk lead who needs to understand where secondary impacts appear preventable and what conditions are associated with higher preventability.

The secondary user is a senior stakeholder who needs a concise evidence-based briefing rather than raw crash records.

## Scope

### In Scope

- public YouTube dashcam and traffic-camera source discovery
- source metadata extraction
- incident-level manual labelling
- data dictionary and labelling rules
- data validation and QA checks
- risk summary metrics
- weather-level preventability profile
- Streamlit dashboard
- tests, CI, and reproducibility documentation
- interview presentation package

### Out of Scope

- computer vision or automatic crash detection
- legal determination of liability
- engineering certification of ADAS capability
- claims pricing or actuarial modelling
- personally identifiable data collection
- national representativeness claims

## Success Criteria

The final interview-ready product should:

- include at least 80 labelled crash incidents, with a target range of 80-120
- preserve a reproducible source and labelling process
- have no missing critical fields in the final labelled dataset
- have no records where secondary impacts exceed total impacts
- produce clear risk metrics and segmentations
- run locally using documented commands
- pass linting, formatting checks, and tests
- provide a stakeholder-facing dashboard and executive narrative

## Current Dataset Position

The current repository includes:

- 25 validated source videos for metadata extraction
- a tracked labelled-data template with one example row
- local generated metadata extracts ignored by Git
- a dashboard and analytical pipeline ready to consume the full labelled dataset

The project should not claim final analytical findings until the labelled dataset is scaled and reviewed.

## Assumptions

- Public crash footage can be used as a proxy dataset for a portfolio product.
- Human review is sufficient for initial labelling when supported by clear rules.
- Existing ADAS technologies can be assessed at a high level using visible crash context.
- Long compilation videos may contain multiple separately labelled incidents.

## Risks & Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Sampling bias in public videos | Findings may over-represent dramatic or winter crashes | Document limitations and avoid population-level claims |
| Subjective labelling | Inconsistent preventability decisions | Use labelling guide, QA rules, and review notes |
| Video availability changes | Source videos may be removed | Store metadata extracts locally and maintain source list |
| Overclaiming ADAS capability | Weakens credibility | Use `Yes`, `Partial`, `No` categories and document uncertainty |
| Small labelled sample | Dashboard metrics may be misleading | Clearly separate seed/template state from final labelled dataset |

## Ethical & Governance Considerations

- Use publicly available videos only.
- Do not collect personal data.
- Do not identify drivers or victims.
- Document methodology, limitations, and uncertainty.
- Treat preventability as an analytical judgement, not a legal conclusion.

## Expected Outputs

- labelled incident dataset
- validation and QA summary
- preventability metrics
- risk breakdowns by weather and other available fields
- interactive dashboard
- executive briefing
- technical demo script
- reproducibility and QA documentation

## Senior Analyst Value

This project demonstrates end-to-end analytical ownership:

- translating a broad idea into a clear risk question
- designing a governed data model
- automating repeatable data acquisition
- building tested analytical modules
- delivering a stakeholder-facing product
- documenting assumptions, limitations, and reproducibility
