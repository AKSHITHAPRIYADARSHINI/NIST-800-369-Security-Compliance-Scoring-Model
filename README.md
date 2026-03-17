# NIST 800-369 Compliance Scoring Model

A Streamlit-based web application for assessing and scoring NIST 800-369 compliance controls in educational institutions. This tool helps schools evaluate their cybersecurity posture against NIST standards tailored for K-12 environments.

## Features

- 📊 **Interactive Dashboard** - View compliance scores by domain and risk levels
- 📥 **CSV Upload** - Upload your compliance assessment data
- 📈 **Real-time Scoring** - Automatic calculation of compliance percentages and risk levels
- ⬇️ **Download Results** - Export scored assessments with detailed metrics
- 🎯 **Domain Analysis** - Drill down into specific security domains
- ⚠️ **Risk Assessment** - Identify high, medium, and low-risk controls

## Quick Start

### Prerequisites
- Python 3.11+
- pip package manager

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to `http://localhost:8501`

3. Download the example CSV from the sidebar or use the provided `nist_800_369_compliance_input.csv`

4. Upload the CSV to view the compliance dashboard

## CSV Input Format

### Required Columns

Your compliance assessment CSV must include these columns:

| Column | Type | Description |
|--------|------|-------------|
| `domain` | string | Compliance domain (e.g., "Secure Software Development Lifecycle") |
| `nist_800_369_control` | string | NIST 800-369 control reference (e.g., "NIST 800-369.V.1") |
| `control_requirement` | string | Description of what the control requires |
| `weight` | number | Importance weight (typically 1-5) |
| `implementation_status` | string | One of: `Implemented`, `Partial`, `Not Implemented` |

### Optional Columns

| Column | Type | Description |
|--------|------|-------------|
| `nist_800_171_control` | string | Corresponding NIST 800-171 control |
| `nist_800_53_control` | string | Corresponding NIST 800-53 control |
| `tailored_for_school_environment` | string | Yes/No if tailored for K-12 |
| `control_owner` | string | Person/team responsible for the control |
| `review_notes` | string | Assessment notes or comments |

### Example Row

```csv
domain,nist_800_369_control,nist_800_171_control,nist_800_53_control,control_requirement,weight,implementation_status,tailored_for_school_environment,control_owner,review_notes
Secure Software Development Lifecycle (SDLC),NIST 800-369.V.1,3.16 System & Services Acquisition,SA – System & Services Acquisition,Secure design principles and coding standards,3,Implemented,Yes,IT Security,
```

## Scoring Methodology

### Status Scoring
- **Implemented** = 1.0 (100% complete)
- **Partial** = 0.5 (50% complete)
- **Not Implemented** = 0.0 (0% complete)

### Weighted Score Calculation
```
Compliance Score (%) = (Σ(weight × status_score) / Σ(weight)) × 100
```

### Risk Level Determination
- **High Risk**: Not Implemented + weight ≥ 4, OR Partial + weight ≥ 4
- **Medium Risk**: Not Implemented + weight < 4
- **Low Risk**: Implemented, OR Partial + weight < 4

## Using the Example CSV

The app includes a ready-to-use example file: **`nist_800_369_compliance_input.csv`**

This example file contains:
- **38 compliance controls** across 8 security domains
- **26 Implemented** controls
- **12 Partial** controls
- **6 Not Implemented** controls
- Real-world school environment scenarios

### How to Use It

1. **Download** the example CSV from the sidebar ("Download Example CSV")
2. **Edit** the file to match your school's actual compliance status
3. **Upload** your edited CSV back to the app
4. **Review** the compliance dashboard and risk analysis
5. **Download** the scored output for your records

## Domains Covered

1. **Secure Software Development Lifecycle (SDLC)**
2. **Data Classification & Protection**
3. **Third-Party Security & Vendor Management**
4. **Student Data Privacy & FERPA Compliance**
5. **Classroom Device & Endpoint Security**
6. **Educational Technology Platform Security**
7. **Security Monitoring & Dashboard Reporting**

## Dashboard Metrics

### Key Performance Indicators
- **Overall Compliance Score** - Percentage compliance across all controls
- **Total Controls** - Number of controls assessed
- **High Risk Controls** - Controls with potential critical impact
- **Pending/Partial Controls** - Controls not fully implemented

### Visualizations
- **Compliance Score by Domain** - Bar chart showing each domain's compliance percentage
- **Risk Distribution** - Breakdown of controls by risk level
- **Scored Controls Table** - Detailed view of all controls with filters

## Deployment to Firebase Cloud Run

### Prerequisites
- Google Cloud Project with Firebase enabled
- `gcloud` CLI configured
- Docker installed locally

### Deployment Steps

1. **Authenticate with Google Cloud**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

2. **Enable Required APIs**
   ```bash
   gcloud services enable cloudbuild.googleapis.com run.googleapis.com
   ```

3. **Deploy Using Cloud Build**
   ```bash
   gcloud builds submit --config cloudbuild.yaml
   ```

4. **View Deployment**
   - Go to Cloud Run console
   - Click on the `nist-compliance-scorer` service
   - Visit the service URL

### Environment Configuration

For production deployments, you may want to set Streamlit config variables:

Create `.streamlit/config.toml`:
```toml
[server]
headless = true
port = 8080
enableXsrfProtection = true

[logger]
level = "info"
```

## Testing the Application

### Local Testing
```bash
# Run the app
streamlit run app.py

# In another terminal, test the CLI scorer
python run_scoring.py nist_800_369_compliance_input.csv -o test_output.csv
```

### Cloud Testing
1. Deploy to Cloud Run
2. Open the service URL in your browser
3. Download the example CSV
4. Upload it to verify functionality
5. Check the downloaded scored output

## File Structure

```
.
├── app.py                                          # Streamlit web application
├── compliance_scoring_model.py                     # Scoring engine and logic
├── run_scoring.py                                  # CLI tool for batch scoring
├── nist_800_369_compliance_input.csv               # Example input data
├── nist_800_369_scored_output.csv                  # Example scored output
├── requirements.txt                                # Python dependencies
├── Dockerfile                                      # Container configuration
├── cloudbuild.yaml                                 # Cloud Build pipeline
└── README.md                                       # This file
```

## Scoring Model Details

### Functions

- `normalize_dataframe()` - Validates required columns and calculates scores
- `overall_score()` - Computes weighted compliance percentage
- `domain_scores()` - Groups and analyzes by security domain
- `risk_summary()` - Categorizes controls by risk level
- `build_summary()` - Generates executive summary statistics

## Support and Feedback

For issues, suggestions, or questions:
1. Review the "How scoring works" section in the app sidebar
2. Check the CSV format against the Required Columns section above
3. Verify all `implementation_status` values are spelled exactly: `Implemented`, `Partial`, or `Not Implemented`

## License

This project is designed for educational K-12 institutions to assess NIST 800-369 compliance.

## About NIST 800-369

**NIST Special Publication 800-369** provides guidelines and standards for cybersecurity in K-12 educational systems. This tool helps schools:
- Assess current security posture
- Identify gaps and risks
- Plan remediation efforts
- Track compliance progress over time

---

**Last Updated**: March 2026
**Current Version**: 1.0
