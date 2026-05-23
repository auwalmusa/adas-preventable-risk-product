# ADAS Preventable Risk Detection Product

**Status: Phase 6 Complete**

A senior-level analytical product built for the HMRC Senior Data Analyst (Risk & Intelligence Service) technical presentation.

## Business Problem

Chain-reaction crashes frequently cause preventable secondary impacts after the initial collision. This product estimates how many secondary crashes could be avoided using existing ADAS technologies such as Automatic Emergency Braking, Forward Collision Warning, and Adaptive Cruise Control.

## Completed Phases

- Business requirements and scoping
- Professional project structure and governance
- YouTube metadata extraction
- Robust data model and data dictionary
- Core analytics pipeline for loading, validation, and risk analysis
- Professional Streamlit dashboard
- Testing framework and reproducibility checks

## How to Run

```bash
python -m pip install -r requirements.txt
python -m streamlit run dashboard/app.py
```

## Quality Checks

```bash
python -m ruff check src tests dashboard
python -m black --check src tests dashboard
python -m pytest tests/ -v
```

Built with Python best practices, testing, documentation, and reproducibility.
