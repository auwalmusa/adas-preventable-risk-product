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

## 4. Core Pipeline (upcoming)

- Modular Python code with validation, analysis, and visualisation

## 5. Delivery Layer

- Interactive Streamlit dashboard for stakeholders

This product is designed to the standard I would deliver in a live HMRC risk product.
