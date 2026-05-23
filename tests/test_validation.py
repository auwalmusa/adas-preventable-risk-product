import pandas as pd

from src.validation import validate_crash_data


def test_validation_returns_expected_quality_metrics() -> None:
    data = {
        "initial_impact_unavoidable": ["Yes", "Yes", "No"],
        "secondary_preventable_by_adas": ["Yes", "Partial", "No"],
        "num_total_impacts": [4, 3, 1],
        "num_secondary_impacts": [3, 2, 0],
    }
    df = pd.DataFrame(data)

    result = validate_crash_data(df)

    assert result["total_records"] == 3
    assert result["preventable_rate"] == 66.7
    assert result["pct_with_secondary"] == 66.7
    assert result["invalid_secondary_count"] == 0
