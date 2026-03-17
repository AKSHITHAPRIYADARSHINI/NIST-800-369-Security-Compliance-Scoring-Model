# Quick Start Guide

Get the NIST 800-369 Compliance Scoring Model up and running in 5 minutes.

## 1️⃣ Install & Run (Local)

```bash
# Install dependencies
pip install -r requirements.txt

# Start the Streamlit app
streamlit run app.py
```

Opens at: **http://localhost:8501** ✅

## 2️⃣ Download Example Data

In the sidebar, click **"⬇️ Download Example CSV"**

This gives you: `nist_800_369_compliance_input.csv` with 38 real compliance controls

## 3️⃣ Upload & Score

1. Click **"Upload your compliance CSV"**
2. Select the CSV file
3. View the dashboard instantly ✅

## 4️⃣ Customize Your Data

1. Download the example CSV
2. Edit in Excel/Sheets:
   - Update `implementation_status`: `Implemented` / `Partial` / `Not Implemented`
   - Update `weight`: importance level (1-5)
   - Keep columns: domain, control_requirement, etc.
3. Upload your edited version
4. See updated scores! ✅

## 5️⃣ Export Results

Click **"Download scored CSV"** to save results with:
- Calculated `status_score` (0.0-1.0)
- Weighted points
- Risk levels (Low/Medium/High)

---

## 📊 What You'll See

| Metric | Example |
|--------|---------|
| Overall Compliance Score | 78.5% |
| Total Controls | 38 |
| Implemented | 26 ✅ |
| Partial | 12 ⚠️ |
| Not Implemented | 6 ❌ |
| High Risk | 2 |
| Medium Risk | 8 |
| Low Risk | 28 |

---

## 🚀 Deploy to Firebase Cloud Run

```bash
# One command deployment
gcloud builds submit --config cloudbuild.yaml
```

For detailed instructions, see [DEPLOY.md](DEPLOY.md)

---

## 📁 CSV Format

**Minimum 5 columns required:**

```csv
domain,nist_800_369_control,control_requirement,weight,implementation_status
Secure SDLC,NIST 800-369.V.1,Secure design,3,Implemented
Data Protection,NIST 800-369.W.1,Data encryption,5,Partial
```

**Optional columns** for richer data:
- `nist_800_171_control` - NIST 171 mapping
- `nist_800_53_control` - NIST 53 mapping
- `tailored_for_school_environment` - Yes/No
- `control_owner` - Person responsible
- `review_notes` - Assessment notes

See [README.md](README.md) for full column reference.

---

## ⚠️ Common Issues

### "Missing required column(s)"
✅ **Fix**: Make sure CSV has exactly:
- `domain`
- `nist_800_369_control`
- `control_requirement`
- `weight`
- `implementation_status`

### Scores showing as 0%
✅ **Fix**: Check `implementation_status` spelling:
- ✅ `Implemented`
- ✅ `Partial`
- ✅ `Not Implemented`
- ❌ `implemented` (lowercase)
- ❌ `IMPLEMENTED` (uppercase)

### App won't start
✅ **Fix**: Install dependencies
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Port already in use
✅ **Fix**: Change port
```bash
streamlit run app.py --server.port 8502
```

---

## 📚 Sample Files

| File | Purpose |
|------|---------|
| `nist_800_369_compliance_input.csv` | Full example (38 controls) |
| `nist_800_369_sample_minimal.csv` | Quick test (8 controls) |
| `nist_800_369_scored_output.csv` | Example output |

---

## 🔗 Next Steps

- ✅ Try with example data
- ✅ Edit CSV with your school's data
- ✅ Track changes over time
- ✅ Deploy to Firebase for team access
- ✅ Monitor compliance dashboard

---

## 📖 Learn More

- [Full Documentation](README.md)
- [Deployment Guide](DEPLOY.md)
- [NIST 800-369 Standards](https://csrc.nist.gov/publications/detail/sp/800-369/final)

---

**Ready?** Run `streamlit run app.py` and open http://localhost:8501 🎉
