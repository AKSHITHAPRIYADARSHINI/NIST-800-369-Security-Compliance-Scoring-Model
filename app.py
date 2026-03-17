from __future__ import annotations

import io
from pathlib import Path

import pandas as pd
import streamlit as st

from compliance_scoring_model import (
    build_summary,
    domain_scores,
    normalize_dataframe,
    risk_summary,
)

st.set_page_config(page_title="NIST 800-369 Compliance Scoring Model", layout="wide")

st.title("NIST 800-369 Compliance Scoring Model")
st.caption("Upload a CSV, calculate compliance scores, and review domain-level risk in a simple dashboard.")

with st.sidebar:
    st.header("How scoring works")
    st.markdown(
        """
        **Status -> Score**
        - Implemented = 1.0
        - Partial = 0.5
        - Not Implemented = 0.0

        **Overall formula**
        - `(sum(weight * status_score) / sum(weight)) * 100`

        **Required columns**
        - `domain`
        - `nist_800_369_control`
        - `control_requirement`
        - `weight`
        - `implementation_status`
        """
    )

    st.divider()
    st.header("Example File")
    st.markdown("Download the example CSV to try the scoring model:")

    csv_file = Path(__file__).parent / "nist_800_369_compliance_input.csv"
    try:
        if csv_file.exists():
            example_df = pd.read_csv(csv_file)
            csv_buffer = io.StringIO()
            example_df.to_csv(csv_buffer, index=False)

            st.download_button(
                label="Download Example CSV",
                data=csv_buffer.getvalue(),
                file_name="nist_800_369_compliance_input.csv",
                mime="text/csv",
                key="download_example",
            )

            st.markdown("**Preview of example file:**")
            st.dataframe(example_df.head(5), use_container_width=True)
        else:
            st.warning("Example file not found in app directory")
    except Exception as exc:
        st.warning(f"Could not load example file: {exc}")

uploaded = st.file_uploader("Upload your compliance CSV", type=["csv"])

if uploaded is None:
    st.info("Upload the sample CSV or your edited CSV to view the dashboard.")
    st.stop()

try:
    raw_df = pd.read_csv(uploaded)
    scored_df = normalize_dataframe(raw_df)
    summary = build_summary(scored_df)
    domain_df = domain_scores(scored_df)
    risk_df = risk_summary(scored_df)
except Exception as exc:
    st.error(f"Unable to process uploaded file: {exc}")
    st.stop()

m1, m2, m3, m4 = st.columns(4)
m1.metric("Overall Compliance Score", f"{summary['overall_compliance_score_pct']}%")
m2.metric("Total Controls", summary["total_controls"])
m3.metric("High Risk Controls", summary["high_risk_controls"])
m4.metric(
    "Pending / Partial Controls",
    summary["partial_controls"] + summary["not_implemented_controls"],
)

left, right = st.columns([1.2, 1])

with left:
    st.subheader("Compliance Score by Domain")
    chart_df = domain_df.set_index("domain")[["compliance_score_pct"]]
    st.bar_chart(chart_df)

with right:
    st.subheader("Risk Distribution")
    risk_chart = risk_df.set_index("risk_level")[["control_count"]]
    st.bar_chart(risk_chart)

st.subheader("Domain Summary")
st.dataframe(
    domain_df.rename(
        columns={
            "domain": "Domain",
            "total_weight": "Total Weight",
            "points": "Weighted Points",
            "compliance_score_pct": "Compliance Score (%)",
        }
    ),
    use_container_width=True,
)

st.subheader("Scored Controls")
filter_domain = st.selectbox("Filter by domain", ["All"] + sorted(scored_df["domain"].dropna().unique().tolist()))
table_df = scored_df if filter_domain == "All" else scored_df[scored_df["domain"] == filter_domain]
st.dataframe(table_df, use_container_width=True)

download_df = scored_df.copy()
buffer = io.StringIO()
download_df.to_csv(buffer, index=False)
st.download_button(
    "Download scored CSV",
    data=buffer.getvalue(),
    file_name="nist_800_369_scored_output.csv",
    mime="text/csv",
)