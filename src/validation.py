from typing import Any

import pandas as pd

CRITICAL_FIELDS = [
    "initial_impact_unavoidable",
    "secondary_preventable_by_adas",
]

REQUIRED_COLUMNS = [
    *CRITICAL_FIELDS,
    "num_total_impacts",
    "num_secondary_impacts",
]


def require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def percentage(series: pd.Series) -> float:
    return float(round(series.mean() * 100, 1))


def validate_crash_data(df: pd.DataFrame) -> dict[str, Any]:
    """Run data quality validation for the labelled crash dataset."""
    require_columns(df, REQUIRED_COLUMNS)

    has_secondary = df["num_secondary_impacts"] > 0
    preventable_or_partial = df["secondary_preventable_by_adas"].isin(
        ["Yes", "Partial"]
    )

    return {
        "total_records": len(df),
        "missing_critical_fields": df[CRITICAL_FIELDS].isna().sum().to_dict(),
        "invalid_secondary_count": int(
            (df["num_secondary_impacts"] > df["num_total_impacts"]).sum()
        ),
        "preventable_rate": percentage(preventable_or_partial),
        "pct_with_secondary": percentage(has_secondary),
    }
