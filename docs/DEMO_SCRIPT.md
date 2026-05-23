# Demo Script

## Target Length

10-12 minutes.

## 0:00-1:00 - Opening

"This project asks a practical risk question: if the first crash in a chain reaction is unavoidable, how many of the later impacts could be prevented or reduced by existing driver assistance technology?"

Position the work as a complete analytical product, not a standalone notebook:

- business question
- data acquisition
- governance
- validation
- analytics
- dashboard
- tests and reproducibility

## 1:00-2:00 - Business Context

Explain why secondary impacts matter:

- they compound injury and damage risk
- they affect road disruption and response demand
- they are plausibly preventable through AEB, FCW, and ACC

Connect to HMRC Senior Data Analyst expectations:

- structured risk thinking
- evidence-based methodology
- repeatable process
- stakeholder-facing output

## 2:00-3:00 - Repo Walkthrough

Show the folder structure:

- `src/` for production-style Python modules
- `tests/` for automated checks
- `dashboard/` for the Streamlit app
- `docs/` for business, QA, reproducibility, and interview documentation
- `data/raw/crash_labels_2025.csv` for the tracked labelling template

Emphasise that raw generated extracts are intentionally ignored.

## 3:00-4:30 - Data Ingestion

Open `src/youtube_extractor.py`.

Explain:

- validated source URL list
- `yt-dlp` metadata extraction
- duplicate URL handling
- invalid URL detection
- separate error log output

Say: "This gives me a repeatable way to build the source pool without manually copying metadata."

## 4:30-6:00 - Data Model & Labelling Governance

Open:

- `docs/data_dictionary.md`
- `docs/LABELLING_GUIDE.md`
- `docs/DATA_QUALITY_QA.md`

Explain:

- unit of analysis is the incident, not always the whole video
- timestamp-level labelling for compilations
- explicit decision rules for unavoidable first impact
- `Yes`, `Partial`, `No` preventability categories
- review notes for ambiguous cases

## 6:00-7:30 - Core Pipeline

Open:

- `src/data_loader.py`
- `src/validation.py`
- `src/analysis.py`

Explain:

- loader standardises column names and parses dates
- validation checks critical fields and impossible impact counts
- analysis produces headline metrics and weather breakdowns

Say: "This is the analytical engine behind the dashboard, so the dashboard is not doing hidden business logic."

## 7:30-9:30 - Dashboard Demo

Run:

```bash
python -m streamlit run dashboard/app.py
```

Show:

- headline metrics
- data quality snapshot
- preventability chart
- weather breakdown
- labelled dataset preview

Explain that with the full 80-120 incident dataset, this becomes the main stakeholder view.

## 9:30-10:30 - Testing & Reproducibility

Run or show:

```bash
python -m ruff check src tests dashboard
python -m black --check src tests dashboard
python -m pytest tests/ -v
```

Mention:

- CI uses the same commands
- tests cover extraction validation, loader behaviour, data validation, analytics, and dashboard loading
- `docs/REPRODUCIBILITY.md` explains how another analyst can repeat the work

## 10:30-12:00 - Close

Close with:

"The value of the project is not just the dashboard. It is the full product workflow: a clear risk question, a governed data model, repeatable ingestion, tested analytics, and a stakeholder-facing delivery layer."

Optional final point:

"The next step would be scaling the labelled incidents to 80-120, then adding confidence intervals and segmentation by weather, road type, country, and human factor."
