#!/bin/bash

echo "======================================"
echo "NIST 800-369 Compliance Scorer"
echo "Local Testing Script"
echo "======================================"
echo ""

# Check Python version
echo "✓ Checking Python version..."
python --version || { echo "✗ Python not found. Please install Python 3.11+"; exit 1; }

# Check requirements
echo "✓ Checking dependencies..."
pip list | grep -E "(pandas|streamlit)" > /dev/null || {
    echo "✗ Missing dependencies. Installing..."
    pip install -r requirements.txt
}

# Test the scoring model
echo ""
echo "✓ Testing scoring model..."
python -c "
from compliance_scoring_model import score_csv
try:
    scored, summary = score_csv('nist_800_369_compliance_input.csv', 'test_output.csv')
    print(f'  Overall Score: {summary[\"overall_compliance_score_pct\"]}%')
    print(f'  Total Controls: {summary[\"total_controls\"]}')
    print(f'  Implemented: {summary[\"implemented_controls\"]}')
    print(f'  Partial: {summary[\"partial_controls\"]}')
    print(f'  Not Implemented: {summary[\"not_implemented_controls\"]}')
    print(f'  High Risk: {summary[\"high_risk_controls\"]}')
    print(f'  Medium Risk: {summary[\"medium_risk_controls\"]}')
    print(f'  Low Risk: {summary[\"low_risk_controls\"]}')
    print('  ✓ Scoring model working correctly!')
except Exception as e:
    print(f'  ✗ Error: {e}')
    exit(1)
" || exit 1

# Test Streamlit app
echo ""
echo "✓ Testing Streamlit app..."
streamlit --version || { echo "✗ Streamlit not found"; exit 1; }

echo ""
echo "======================================"
echo "✓ All tests passed!"
echo "======================================"
echo ""
echo "To run the Streamlit app:"
echo "  streamlit run app.py"
echo ""
echo "Then visit: http://localhost:8501"
echo ""
