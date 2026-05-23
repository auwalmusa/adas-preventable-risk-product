from pathlib import Path

import pandas as pd
import pytest

from src.data_loader import load_crash_labels


def test_load_crash_labels_standardises_columns_and_dates(tmp_path: Path) -> None:
    file_path = tmp_path / "labels.csv"
    file_path.write_text(
        "Date Watched,Video-ID\n2025-05-23,EXAMPLE001\n",
        encoding="utf-8",
    )

    result = load_crash_labels(str(file_path))

    assert list(result.columns) == ["date_watched", "video_id"]
    assert result.loc[0, "video_id"] == "EXAMPLE001"
    assert pd.api.types.is_datetime64_any_dtype(result["date_watched"])


def test_load_crash_labels_raises_for_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_crash_labels(str(tmp_path / "missing.csv"))
