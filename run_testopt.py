import argparse
import pandas as pd
import os
from testopt.compare_tests import compare_and_select_best
from utils.loader import load_latest_csv  # 👈 import loader

def main():
    parser = argparse.ArgumentParser(description="Test Optimization Framework")
    parser.add_argument("--data", type=str, help="Path to test data CSV (optional)")
    args = parser.parse_args()

    # ✅ Use loader if no path is provided
    if args.data:
        if not os.path.exists(args.data):
            raise FileNotFoundError(f"❌ File not found: {args.data}")
        data = pd.read_csv(args.data)
        print(f"✅ Loaded CSV from --data: {args.data}")
    else:
        data = load_latest_csv(folder_path="data")  # or "." if stored in root
        print("📦 Auto-loaded latest CSV from /data/")

    # Process test data
    test_cases = {row['test_case']: set(row['mutants'].split(',')) for _, row in data.iterrows()}
    mutants = set.union(*test_cases.values())
    defect_data = data.drop(columns=['test_case', 'mutants'])

    best_method, results = compare_and_select_best(test_cases, mutants, defect_data)

    print(f"\n🏆 Best Optimization Method: {best_method}")
    print(f"📊 Results: {results}")

if __name__ == "__main__":
    main()

