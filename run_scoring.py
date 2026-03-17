from __future__ import annotations
import argparse
from compliance_scoring_model import score_csv

def main() -> None:
    parser = argparse.ArgumentParser(description="Score a NIST 800-369 compliance CSV.")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("-o", "--output", default="nist_800_369_scored_output.csv", help="Output CSV file path")
    args = parser.parse_args()

    scored, summary = score_csv(args.input_csv, args.output)

    print("\nNIST 800-369 Compliance Summary")
    print("-" * 40)
    for key, value in summary.items():
        print(f"{key}: {value}")
    print(f"\nScored CSV saved to: {args.output}")

if __name__ == "__main__":
    main()