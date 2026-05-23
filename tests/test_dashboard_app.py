from pathlib import Path

import dashboard.app as app


def test_load_dashboard_data_without_label_file(tmp_path: Path) -> None:
    data = app.load_dashboard_data(tmp_path / "missing.csv")

    assert list(data.columns) == app.EMPTY_LABEL_COLUMNS
