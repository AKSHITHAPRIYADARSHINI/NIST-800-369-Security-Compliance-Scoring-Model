from __future__ import annotations
import pandas as pd

STATUS_MAP = {
    "Implemented": 1.0,
    "Partial": 0.5,
    "Not Implemented": 0.0,
}

def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    required = [
        "domain",
        "nist_800_369_control",
        "control_requirement",
        "weight",
        "implementation_status",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")

    out = df.copy()
    out["weight"] = pd.to_numeric(out["weight"], errors="coerce").fillna(1.0)
    out["status_score"] = out["implementation_status"].map(STATUS_MAP).fillna(0.0)
    out["weighted_points"] = out["weight"] * out["status_score"]

    def derive_risk(row) -> str:
        weight = row["weight"]
        status = row["implementation_status"]
        if status == "Not Implemented" and weight >= 4:
            return "High"
        if status == "Not Implemented":
            return "Medium"
        if status == "Partial" and weight >= 4:
            return "Medium"
        return "Low"

    out["risk_level"] = out.apply(derive_risk, axis=1)
    return out

def overall_score(df: pd.DataFrame) -> float:
    total_weight = float(df["weight"].sum())
    if total_weight == 0:
        return 0.0
    return round(float(df["weighted_points"].sum()) / total_weight * 100, 2)

def domain_scores(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("domain", dropna=False)
        .agg(total_weight=("weight", "sum"), points=("weighted_points", "sum"))
        .reset_index()
    )
    grouped["compliance_score_pct"] = (grouped["points"] / grouped["total_weight"] * 100).round(2)
    return grouped.sort_values(["compliance_score_pct", "domain"], ascending=[False, True])

def risk_summary(df: pd.DataFrame) -> pd.DataFrame:
    risk = (
        df.groupby("risk_level")
        .size()
        .reindex(["High", "Medium", "Low"], fill_value=0)
        .reset_index(name="control_count")
    )
    return risk

def build_summary(df: pd.DataFrame) -> dict:
    return {
        "overall_compliance_score_pct": overall_score(df),
        "total_controls": int(len(df)),
        "implemented_controls": int((df["implementation_status"] == "Implemented").sum()),
        "partial_controls": int((df["implementation_status"] == "Partial").sum()),
        "not_implemented_controls": int((df["implementation_status"] == "Not Implemented").sum()),
        "high_risk_controls": int((df["risk_level"] == "High").sum()),
        "medium_risk_controls": int((df["risk_level"] == "Medium").sum()),
        "low_risk_controls": int((df["risk_level"] == "Low").sum()),
    }

def score_csv(input_csv: str, output_csv: str | None = None) -> tuple[pd.DataFrame, dict]:
    df = pd.read_csv(input_csv)
    scored = normalize_dataframe(df)
    summary = build_summary(scored)
    if output_csv:
        scored.to_csv(output_csv, index=False)
    return scored, summary