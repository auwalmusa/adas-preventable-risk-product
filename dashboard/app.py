from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"


def load_crash_data() -> pd.DataFrame:
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))
    if not csv_files:
        return pd.DataFrame(
            columns=[
                "video_id",
                "chain_reaction",
                "secondary_impact",
                "adas_preventable",
            ]
        )

    frames = [pd.read_csv(path) for path in csv_files]
    return pd.concat(frames, ignore_index=True)


def main() -> None:
    st.set_page_config(page_title="ADAS Preventable Risk", layout="wide")
    st.title("ADAS Preventable Risk")

    data = load_crash_data()
    if data.empty:
        st.info("Add crash-analysis CSV files to data/raw to populate the dashboard.")
        return

    total_events = len(data)
    preventable_count = int(
        data.get("adas_preventable", pd.Series(dtype=bool)).fillna(False).sum()
    )
    secondary_count = int(
        data.get("secondary_impact", pd.Series(dtype=bool)).fillna(False).sum()
    )

    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Events", total_events)
    col_b.metric("Secondary impacts", secondary_count)
    col_c.metric("ADAS preventable", preventable_count)

    if "adas_preventable" in data.columns:
        summary = (
            data["adas_preventable"]
            .fillna(False)
            .value_counts()
            .rename_axis("Preventable")
            .reset_index(name="Count")
        )
        fig = px.bar(
            summary,
            x="Preventable",
            y="Count",
            title="Preventable Impact Classification",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(data, use_container_width=True)


if __name__ == "__main__":
    main()
