from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from src.analysis import generate_risk_summary
from src.data_loader import load_crash_labels
from src.validation import validate_crash_data

ROOT_DIR = Path(__file__).resolve().parents[1]
LABELS_PATH = ROOT_DIR / "data" / "raw" / "crash_labels_2025.csv"
EMPTY_LABEL_COLUMNS = [
    "date_watched",
    "video_id",
    "video_title",
    "video_url",
    "country",
    "weather",
    "road_type",
    "crash_timestamp_start",
    "initial_impact_unavoidable",
    "reason_unavoidable",
    "num_total_impacts",
    "num_secondary_impacts",
    "secondary_preventable_by_adas",
    "adas_features_needed",
    "main_human_error_in_secondary",
    "estimated_severity",
    "notes",
]


def load_dashboard_data(file_path: Path = LABELS_PATH) -> pd.DataFrame:
    if not file_path.exists():
        return pd.DataFrame(columns=EMPTY_LABEL_COLUMNS)
    return load_crash_labels(str(file_path))


def render_metric(label: str, value: object) -> None:
    st.metric(label, value)


def main() -> None:
    st.set_page_config(
        page_title="ADAS Preventable Risk Product",
        layout="wide",
    )

    st.markdown(
        """
        <style>
            .main {background-color: #f8f9fa;}
            h1 {color: #1f2937; font-weight: 600;}
            [data-testid="stMetric"] {
                background-color: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 16px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("ADAS Preventable Risk Detection Product")
    st.caption(
        "Senior Data Analyst portfolio product for quantifying preventable "
        "secondary crash risk."
    )

    data = load_dashboard_data()
    if data.empty:
        st.info(
            "Dashboard is ready. Populate data/raw/crash_labels_2025.csv to view insights."
        )
        return

    validation = validate_crash_data(data)
    summary, by_weather = generate_risk_summary(data)
    metrics = summary.iloc[0]

    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        render_metric("Total Crashes Analysed", int(metrics["total_crashes"]))
    with col_b:
        render_metric("Preventable by ADAS", f"{metrics['pct_preventable_by_adas']}%")
    with col_c:
        render_metric("With Secondary Impacts", f"{metrics['pct_with_secondary']}%")
    with col_d:
        render_metric("Average Secondary Impacts", metrics["avg_secondary_impacts"])

    st.subheader("Data Quality Snapshot")
    qa_a, qa_b, qa_c = st.columns(3)
    qa_a.metric("Records", validation["total_records"])
    qa_b.metric("Invalid Impact Counts", validation["invalid_secondary_count"])
    qa_c.metric(
        "Missing Critical Fields",
        sum(validation["missing_critical_fields"].values()),
    )

    st.subheader("Secondary Impact Preventability")
    preventability_counts = (
        data["secondary_preventable_by_adas"]
        .fillna("Unknown")
        .value_counts()
        .rename_axis("Preventability")
        .reset_index(name="Crashes")
    )
    fig_pie = px.pie(
        preventability_counts,
        names="Preventability",
        values="Crashes",
        title="Proportion of Secondary Impacts Preventable by Current ADAS",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Preventability by Weather Conditions")
    fig_bar = px.bar(
        by_weather,
        title="Preventability Profile by Weather",
        labels={"value": "Proportion", "weather": "Weather Condition"},
        barmode="group",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("Labelled Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)

    st.caption("Built as a complete, reproducible Senior Data Analyst product.")


if __name__ == "__main__":
    main()
