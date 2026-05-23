from pathlib import Path

import pandas as pd


def standardise_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with consistent snake_case column names."""
    standardised = df.copy()
    standardised.columns = [
        col.strip().lower().replace(" ", "_").replace("-", "_")
        for col in standardised.columns
    ]
    return standardised


def load_crash_labels(
    file_path: str = "data/raw/crash_labels_2025.csv",
) -> pd.DataFrame:
    """Load the labelled crash dataset."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(path)
    df = standardise_column_names(df)

    if "date_watched" in df.columns:
        df["date_watched"] = pd.to_datetime(df["date_watched"], errors="coerce")

    return df


def load_raw_metadata(
    file_path: str = "data/raw/raw_metadata.csv",
) -> pd.DataFrame | None:
    """Load raw video metadata when an extracted metadata file is available."""
    path = Path(file_path)
    if not path.exists():
        return None
    return standardise_column_names(pd.read_csv(path))
