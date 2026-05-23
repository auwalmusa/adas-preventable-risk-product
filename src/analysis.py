import pandas as pd

from src.validation import percentage, require_columns

ANALYSIS_COLUMNS = [
    "weather",
    "num_secondary_impacts",
    "secondary_preventable_by_adas",
]


def generate_risk_summary(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Generate headline risk metrics and a weather-level preventability breakdown."""
    require_columns(df, ANALYSIS_COLUMNS)

    has_secondary = df["num_secondary_impacts"] > 0
    preventable_or_partial = df["secondary_preventable_by_adas"].isin(
        ["Yes", "Partial"]
    )
    summary = {
        "total_crashes": len(df),
        "crashes_with_secondary": int(has_secondary.sum()),
        "pct_with_secondary": percentage(has_secondary),
        "pct_preventable_by_adas": percentage(preventable_or_partial),
        "avg_secondary_impacts": float(round(df["num_secondary_impacts"].mean(), 2)),
    }

    by_weather = (
        df.groupby("weather")["secondary_preventable_by_adas"]
        .value_counts(normalize=True)
        .unstack(fill_value=0)
        .round(3)
    )

    return pd.DataFrame([summary]), by_weather
