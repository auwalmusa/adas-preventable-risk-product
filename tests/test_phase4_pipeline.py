from pathlib import Path

import pandas as pd
import pytest

from src.analysis import generate_risk_summary
from src.data_loader import (
    load_crash_labels,
    load_raw_metadata,
    standardise_column_names,
)
from src.validation import validate_crash_data


def labelled_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "initial_impact_unavoidable": "Yes",
                "secondary_preventable_by_adas": "Yes",
                "num_total_impacts": 4,
                "num_secondary_impacts": 3,
                "weather": "Rain",
            },
            {
                "initial_impact_unavoidable": "No",
                "secondary_preventable_by_adas": "No",
                "num_total_impacts": 1,
                "num_secondary_impacts": 0,
                "weather": "Clear",
            },
        ]
    )


def test_standardise_column_names() -> None:
    df = pd.DataFrame(columns=["Date Watched", "Road-Type"])

    result = standardise_column_names(df)

    assert list(result.columns) == ["date_watched", "road_type"]


def test_load_crash_labels_converts_date(tmp_path: Path) -> None:
    csv_path = tmp_path / "labels.csv"
    csv_path.write_text("date_watched,video_id\n2025-05-23,abc123\n", encoding="utf-8")

    result = load_crash_labels(str(csv_path))

    assert list(result.columns) == ["date_watched", "video_id"]
    assert pd.api.types.is_datetime64_any_dtype(result["date_watched"])


def test_load_raw_metadata_returns_none_for_missing_file(tmp_path: Path) -> None:
    assert load_raw_metadata(str(tmp_path / "missing.csv")) is None


def test_validate_crash_data_returns_quality_metrics() -> None:
    result = validate_crash_data(labelled_frame())

    assert result["total_records"] == 2
    assert result["invalid_secondary_count"] == 0
    assert result["preventable_rate"] == 50.0
    assert result["pct_with_secondary"] == 50.0


def test_validate_crash_data_requires_core_columns() -> None:
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_crash_data(pd.DataFrame({"weather": ["Rain"]}))


def test_generate_risk_summary_returns_headline_and_weather_breakdown() -> None:
    summary, by_weather = generate_risk_summary(labelled_frame())

    assert summary.loc[0, "total_crashes"] == 2
    assert summary.loc[0, "crashes_with_secondary"] == 1
    assert summary.loc[0, "pct_preventable_by_adas"] == 50.0
    assert by_weather.loc["Rain", "Yes"] == 1.0
