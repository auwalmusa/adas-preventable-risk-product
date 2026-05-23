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
            .stApp {
                background-color: #f8fafc;
                color: #111827;
            }
            [data-testid="stHeader"] {
                background-color: #f8fafc;
            }
            [data-testid="stAppViewContainer"] {
                background-color: #f8fafc;
            }
            [data-testid="stMainBlockContainer"] {
                padding-top: 3rem;
                padding-bottom: 3rem;
                max-width: 1480px;
            }
            h1, h2, h3, p, span, label {
                color: #111827 !important;
            }
            h1 {
                font-weight: 700;
                letter-spacing: 0;
            }
            [data-testid="stMetric"] {
                background-color: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 18px 20px;
                box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08);
                min-height: 118px;
            }
            [data-testid="stMetric"] * {
                color: #111827 !important;
            }
            [data-testid="stMetricLabel"] {
                color: #4b5563 !important;
                font-weight: 600;
            }
            [data-testid="stMetricValue"] {
                color: #0f172a !important;
                font-weight: 700;
            }
            .stAlert {
                background-color: #eff6ff;
                border: 1px solid #bfdbfe;
                color: #1e3a8a;
            }
            div[data-testid="stDataFrame"] {
                border: 1px solid #e5e7eb;
                border-radius: 8px;
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

    if len(data) < 80:
        st.info(
            "Current view uses the tracked seed/template dataset. The interview-ready "
            "target is 80-120 labelled incidents."
        )

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
    fig_pie.update_layout(
        height=420,
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font_color="#111827",
        title_font_color="#111827",
        legend_font_color="#111827",
        margin={"l": 24, "r": 24, "t": 64, "b": 24},
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Preventability by Weather Conditions")
    fig_bar = px.bar(
        by_weather,
        title="Preventability Profile by Weather",
        labels={"value": "Proportion", "weather": "Weather Condition"},
        barmode="group",
    )
    fig_bar.update_layout(
        height=420,
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font_color="#111827",
        title_font_color="#111827",
        legend_font_color="#111827",
        margin={"l": 24, "r": 24, "t": 64, "b": 48},
    )
    fig_bar.update_xaxes(gridcolor="#e5e7eb", linecolor="#cbd5e1")
    fig_bar.update_yaxes(gridcolor="#e5e7eb", linecolor="#cbd5e1")
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("Labelled Dataset Preview")
    st.dataframe(data.head(20), use_container_width=True)

    st.caption("Built as a complete, reproducible Senior Data Analyst product.")


if __name__ == "__main__":
    main()
