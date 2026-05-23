# Reproducibility Guide

## Purpose

This guide explains how another analyst can reproduce the current project state from a clean checkout. It covers installation, test execution, metadata extraction, dashboard launch, and expected local artifacts.

## Environment

- Python 3.12
- Git
- Internet access for YouTube metadata extraction
- Dependencies listed in `requirements.txt`

## Setup

```bash
python -m pip install -r requirements.txt
```

Using a virtual environment is recommended:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Quality Checks

Run the same commands used by CI:

```bash
python -m ruff check src tests dashboard
python -m black --check src tests dashboard
python -m pytest tests/ -v
```

Expected result at Phase 7:

- Linting passes.
- Formatting check passes.
- Test suite passes.

## Metadata Extraction

Run:

```bash
python src\youtube_extractor.py
```

Expected local outputs:

- `data/raw/raw_metadata.csv`
- `data/raw/raw_metadata_errors.csv`

These files are intentionally ignored by Git because they are generated raw extracts. The tracked labelling template is `data/raw/crash_labels_2025.csv`.

## Dashboard

Run:

```bash
python -m streamlit run dashboard/app.py
```

The dashboard reads `data/raw/crash_labels_2025.csv`, runs validation and risk summary logic, and displays metrics and Plotly charts.

## CI

GitHub Actions is configured in `.github/workflows/ci.yml`. It runs on pushes and pull requests to `main` and executes install, lint, formatting check, and tests.

## Known Local-Only Files

The following are ignored and should not be committed:

- `.pytest_cache/`
- `.ruff_cache/`
- `__pycache__/`
- `data/raw/raw_metadata.csv`
- `data/raw/raw_metadata_errors.csv`
- `.venv/`
