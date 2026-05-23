# Final Interview Briefing

ADAS Preventable Risk Detection Product

HMRC Senior Data Analyst (Risk & Intelligence Service) Technical Presentation

Prepared for: Auwal Musa

## How To Use This Document

Read it once, then close it and practise the walkthrough out loud. The aim is not to memorise every line. The aim is to explain the project clearly, confidently, and without overstating the current evidence.

## Current Evidence Position

Use these numbers accurately:

- 25 validated source videos collected for metadata extraction.
- 1 tracked labelling template row currently exists.
- The target final dataset is 80-120 labelled crash incidents, with 80 as the minimum interview-ready threshold.
- Long compilation videos will be labelled at incident and timestamp level.
- The dashboard and pipeline are ready to analyse the full labelled dataset once labelling is scaled.

Do not claim final findings such as an exact preventable percentage until the labelled dataset has been completed.

## Opening Script

"For my technical presentation, I built a complete analytical product called ADAS Preventable Risk Detection.

The business question is: assuming the first impact in a chain-reaction crash is unavoidable, how many secondary impacts could plausibly be prevented or reduced by existing ADAS technologies such as AEB, FCW, and ACC?

I built this as a full product rather than a one-off notebook: it includes data ingestion, labelling governance, validation, analysis, a Streamlit dashboard, tests, CI, and reproducibility documentation."

## Core Message

"The main point of the project is not just the dashboard. It is the end-to-end analytical lifecycle: defining a risk problem, creating a governed dataset, validating quality, generating insight, and delivering a reproducible product for stakeholders."

## Demo Flow

### 1. Project Structure

Show:

- `src/`
- `tests/`
- `dashboard/`
- `docs/`
- `.github/workflows/ci.yml`

Say:

"I used a production-style structure so the work is maintainable. The analytical logic sits in `src/`, tests are separate, the dashboard is in `dashboard/`, and all methodology and interview documentation is in `docs/`."

### 2. Data Ingestion

Open `src/youtube_extractor.py`.

Say:

"This module automates YouTube metadata extraction using `yt-dlp`. It validates YouTube IDs, removes duplicate URLs, writes successful metadata to a raw extract, and writes failures to an error log. That gives me a repeatable source-acquisition process rather than manual copying."

Mention:

- 25 validated source videos
- generated metadata files are ignored by Git
- labelling is done against the tracked schema

### 3. Data Governance

Open:

- `docs/data_dictionary.md`
- `docs/LABELLING_GUIDE.md`
- `docs/DATA_QUALITY_QA.md`

Say:

"Because the dataset depends on human labelling, governance is critical. I defined the schema, decision rules, inclusion criteria, exclusion criteria, timestamping rules, and uncertainty handling before scaling the dataset."

### 4. Core Analytics Pipeline

Open:

- `src/data_loader.py`
- `src/validation.py`
- `src/analysis.py`

Say:

"The dashboard is not where the analytical rules live. The pipeline modules load and standardise the data, validate critical quality rules, and calculate the risk metrics. That makes the analysis testable and reusable."

Important validation rule:

"One key rule is that secondary impacts must never exceed total impacts. The validation module also checks missing critical fields and calculates preventability and secondary-impact rates."

### 5. Testing & CI

Show:

- `tests/`
- `.github/workflows/ci.yml`

Say:

"The project has tests for loading, validation, analysis, extraction validation, and dashboard loading. CI runs the same checks I run locally: Ruff, Black, and Pytest."

Commands:

```bash
python -m ruff check src tests dashboard
python -m black --check src tests dashboard
python -m pytest tests/ -v
```

### 6. Live Dashboard

Run:

```bash
python -m streamlit run dashboard/app.py
```

Show:

- headline metrics
- data quality snapshot
- preventability distribution
- weather breakdown
- labelled dataset preview

Say:

"At the moment, the dashboard is connected to the tracked label template. Once the 80-120 incidents are labelled, this same product will show the full risk profile without changing the analytical workflow."

## Closing Script

"This project demonstrates senior-level analytical ownership: I reframed a broad idea into a clear preventative risk question, built a governed data model, automated source metadata extraction, created tested analytical modules, delivered a stakeholder dashboard, and documented the process so another analyst can reproduce it.

The next step is scaling the labelled dataset to 80-120 incidents, reviewing ambiguous cases, and then using the dashboard to present preventability patterns by weather, road type, country, and human factor."

## Mock Panel Questions

### Walk us through your project.

"I built an end-to-end analytical product to estimate preventable secondary crash risk. It starts with source metadata extraction, then a governed labelling process, then validation and analysis modules, and finally a dashboard for stakeholder exploration. The repo also includes tests, CI, and reproducibility documentation."

### How did you ensure data quality?

"I treated data quality as part of the product design. I created a data dictionary, labelling guide, QA guide, and validation module. The automated checks include missing critical fields and invalid impact counts, while the manual guide controls judgement calls like ADAS preventability."

### Why is this relevant to HMRC RIS?

"The domain is road risk, but the method is directly transferable to HMRC risk intelligence: define a preventative risk question, build a governed dataset, validate it, produce risk profiles, and deliver reproducible insight for decision makers."

### Why not use thousands of videos?

"For this product, quality is more important than raw volume. The right target is 80-120 carefully labelled incidents. That is enough to produce meaningful proportions and segmentations while keeping labelling quality high."

### Is this computer vision?

"No. Computer vision is deliberately out of scope. This project focuses on the analytical product lifecycle: sourcing, labelling, validation, analysis, and delivery. Computer vision would be a future enhancement once the labelled dataset is mature."

### How would you improve it next?

"First, I would scale labelling to at least 80 incidents. Then I would add confidence intervals, richer segmentation, inter-rater QA for a sample of labels, and exportable executive summaries from the dashboard."

## Lines To Practise

"I built this as a product, not a notebook."

"The dashboard is the delivery layer; the analytical rules live in tested Python modules."

"The current dataset is a seed and template. The product is ready to scale to the 80-120 labelled incidents needed for the final presentation."

"I documented uncertainty instead of hiding it, because that is essential in risk intelligence."

## Final Checklist

- Open the repo before the interview.
- Keep `docs/FINAL_INTERVIEW_BRIEFING.md` open as backup.
- Keep `dashboard/app.py` ready.
- Run `python -m pytest tests/ -v` before the interview.
- Run `python -m streamlit run dashboard/app.py` and confirm the dashboard opens.
- Practise the walkthrough out loud three times with a timer.
