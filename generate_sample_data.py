import pandas as pd
import os

# ✅ Path to output CSV
csv_path = "data/sample_data.csv"

# ✅ Define base data (can be updated easily)
sample_data = [
    {'test_case': 'TC1', 'mutants': 'M1 M2', 'lines_of_code': 80, 'cyclomatic_complexity': 8, 'code_churn': 2, 'prior_defects': 0, 'defective': 0},
    {'test_case': 'TC2', 'mutants': 'M3', 'lines_of_code': 100, 'cyclomatic_complexity': 12, 'code_churn': 5, 'prior_defects': 1, 'defective': 1},
    {'test_case': 'TC3', 'mutants': 'M2 M4', 'lines_of_code': 250, 'cyclomatic_complexity': 20, 'code_churn': 10, 'prior_defects': 2, 'defective': 1},
    {'test_case': 'TC4', 'mutants': 'M5', 'lines_of_code': 60, 'cyclomatic_complexity': 6, 'code_churn': 1, 'prior_defects': 0, 'defective': 0},
    {'test_case': 'TC5', 'mutants': 'M6 M3', 'lines_of_code': 180, 'cyclomatic_complexity': 18, 'code_churn': 7, 'prior_defects': 1, 'defective': 1},
    {'test_case': 'TC6', 'mutants': 'M1 M7', 'lines_of_code': 90, 'cyclomatic_complexity': 10, 'code_churn': 3, 'prior_defects': 1, 'defective': 0},
]

def generate_sample_csv(data, output_path):
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Sample data CSV generated at: {output_path}")

if __name__ == "__main__":
    generate_sample_csv(sample_data, csv_path)
