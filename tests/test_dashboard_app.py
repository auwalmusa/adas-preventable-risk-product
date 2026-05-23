from pathlib import Path

import dashboard.app as app


def test_load_crash_data_without_raw_csv_files(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(app, "RAW_DATA_DIR", tmp_path)

    data = app.load_crash_data()

    assert list(data.columns) == [
        "video_id",
        "chain_reaction",
        "secondary_impact",
        "adas_preventable",
    ]
