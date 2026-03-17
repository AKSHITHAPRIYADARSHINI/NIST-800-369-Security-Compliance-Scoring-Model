# NIST 800-369 Compliance Scoring Model

## Overview
This project provides a simple way to calculate and visualize compliance for a **NIST 800-369 Youth Cybersecurity Framework** controls matrix.

It uses a single CSV file as the input source, applies a weighted scoring model, derives control-level risk, and then displays the result in either:

- a **command-line summary**, or
- a **simple Streamlit dashboard UI**.

The goal is to make compliance scoring easy to understand, easy to update, and easy to demonstrate in a presentation or project review.

---

## Project Files

### `nist_800_369_compliance_input.csv`
This is the main input file.

It contains one row per control and includes the fields needed for scoring, such as:

- `domain`
- `nist_800_369_control`
- `nist_800_171_control`
- `nist_800_53_control`
- `control_requirement`
- `weight`
- `implementation_status`

This CSV is the only file you need to edit when you want to update the compliance state.

---

### `compliance_scoring_model.py`
This is the core scoring engine.

It:

1. reads the CSV data into a pandas DataFrame,
2. validates that required columns exist,
3. converts implementation status into numeric values,
4. computes weighted points,
5. assigns a risk level to each control,
6. calculates the overall compliance score,
7. generates domain-wise summaries and risk summaries.

This file contains the main business logic.

---

### `run_scoring.py`
This is the command-line runner.

It allows you to score a CSV file directly from the terminal and save the result as a new CSV.

Example:

```bash
python run_scoring.py nist_800_369_compliance_input.csv -o nist_800_369_scored_output.csv
```

This is useful when you want a quick result without opening the dashboard.

---

### `app.py`
This is the Streamlit dashboard UI.

It provides a simple web interface where you can:

- upload a CSV file,
- calculate the compliance score,
- view summary metrics,
- see domain-level compliance,
- view risk distribution,
- inspect the scored controls table,
- download the scored result as CSV.

Example:

```bash
streamlit run app.py
```

---

### `nist_800_369_scored_output.csv`
This is the generated output file.

It contains the original control data plus calculated fields such as:

- `status_score`
- `weighted_points`
- `risk_level`

This file is useful for reporting, dashboard feeding, or presentation evidence.

---

## How the Scoring Works

### 1. Status Mapping
Each implementation status is converted to a numeric score:

- `Implemented` = `1.0`
- `Partial` = `0.5`
- `Not Implemented` = `0.0`

This allows qualitative compliance data to be measured numerically.

---

### 2. Weighting
Each control has a `weight` value.

This represents the importance of the control. A more critical control should have a higher weight.

Example:

- Authentication or Data Protection controls may have a higher weight
- Less critical controls may have a lower weight

---

### 3. Weighted Points
For each control:

```text
weighted_points = weight × status_score
```

Examples:

- Weight 5 + Implemented → `5 × 1.0 = 5.0`
- Weight 5 + Partial → `5 × 0.5 = 2.5`
- Weight 5 + Not Implemented → `5 × 0.0 = 0.0`

---

### 4. Overall Compliance Score
The final score is calculated as:

```text
Overall Compliance Score = (Sum of weighted points / Sum of weights) × 100
```

This gives a normalized percentage score for the entire framework.

---

### 5. Risk Level Logic
The model also derives a basic risk level from implementation status and control weight.

Current rule set:

- `Not Implemented` and weight >= 4 → `High`
- `Not Implemented` and weight < 4 → `Medium`
- `Partial` and weight >= 4 → `Medium`
- everything else → `Low`

This is a simple rule-based approach and can be expanded later.

---

## What Happens in the Dashboard
When a CSV is uploaded in the Streamlit UI:

1. The file is read into pandas.
2. The controls are normalized and scored.
3. Summary metrics are displayed:
   - Overall Compliance Score
   - Total Controls
   - High Risk Controls
   - Pending / Partial Controls
4. A domain-wise bar chart is shown.
5. A risk distribution chart is shown.
6. A detailed scored controls table is shown.
7. The user can download the final scored CSV.

So the dashboard is acting as a visual reporting layer on top of the scoring engine.

---

## Required CSV Columns
The scoring engine requires these columns:

- `domain`
- `nist_800_369_control`
- `control_requirement`
- `weight`
- `implementation_status`

Other columns can be kept for documentation and traceability, but they are not required for the core calculation.

---

## Example Workflow

### Option 1: Using the UI
1. Open the Streamlit app.
2. Upload the CSV file.
3. Review the compliance score.
4. Review domain summaries and risks.
5. Download the scored output.

### Option 2: Using the CLI
1. Edit the CSV file.
2. Run the Python script.
3. Save the scored CSV.
4. Use the result for reporting or dashboard integration.

---

## Installation
Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies currently used:

- `pandas`
- `streamlit`

---

## Run Instructions

### Run the dashboard
```bash
streamlit run app.py
```

### Run terminal scoring
```bash
python run_scoring.py nist_800_369_compliance_input.csv -o nist_800_369_scored_output.csv
```

---

## Why This Project Is Useful
This project helps convert a static control matrix into something measurable and interactive.

It is useful for:

- compliance tracking,
- demonstration dashboards,
- security maturity reporting,
- academic presentations,
- framework validation exercises.

Instead of manually calculating implementation maturity, the CSV + Python approach makes the process repeatable and scalable.

---

## Recommended Future Enhancements
You can improve this project further by adding:

- domain-specific weights,
- real-time filtering,
- trend scoring over time,
- historical comparison across review periods,
- export to Excel or PDF,
- more advanced risk formulas,
- role-based dashboard views,
- traffic-light indicators for presentation mode.

---

## Notes
The current CSV already includes some calculated columns (`status_score`, `weighted_points`, `risk_level`), but the Python model recalculates them dynamically. This keeps the scoring consistent even if the CSV is edited manually.

For best results, use the CSV as the editable control source and allow Python to compute the final values.
