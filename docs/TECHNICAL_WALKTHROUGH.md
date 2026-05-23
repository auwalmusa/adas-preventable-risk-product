# Technical Walkthrough - For HMRC Senior Data Analyst Interview

## 1. Project Setup & Governance

- Professional folder structure (`src/`, `tests/`, `dashboard/`, `docs/`)
- `requirements.txt`, `Makefile`, proper `.gitignore`

## 2. Data Ingestion (`src/youtube_extractor.py`)

- Uses `yt-dlp` to automatically extract metadata from YouTube dashcam videos
- Includes error handling and logging

## 3. Data Model & Governance

- Strict data dictionary with clear labelling rules
- Consistent schema for reproducibility and auditability

## 4. Core Pipeline

- Modular Python code for loading labelled data, validating quality rules, and producing risk summaries
- Tested modules in `src/data_loader.py`, `src/validation.py`, and `src/analysis.py`

## 5. Delivery Layer

- Professional Streamlit dashboard in `dashboard/app.py`
- Uses the Phase 4 pipeline modules for validation and analysis
- Presents headline risk metrics, data quality checks, preventability distribution, weather breakdowns, and a labelled data preview

This product is designed to the standard I would deliver in a live HMRC risk product.

## 6. Testing & Final Polish

- Validation tests confirm quality metrics and invalid-count behaviour.
- Data loader tests confirm column standardisation, date parsing, and missing-file handling.
- CI runs linting, formatting checks, and the full pytest suite on every push and pull request.

## 7. Documentation & Reproducibility

- `docs/REPRODUCIBILITY.md` explains setup, generated files, checks, extraction, and dashboard execution.
- `docs/DATA_QUALITY_QA.md` documents automated and manual data quality rules.
- `docs/LABELLING_GUIDE.md` standardises incident selection, timestamping, preventability decisions, and severity labels.
