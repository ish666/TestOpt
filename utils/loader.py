import os
import pandas as pd

def load_latest_csv(data_dir="data"):
    """
    Loads the most recently modified CSV file from the specified data directory.

    Args:
        data_dir (str): The directory where CSV files are stored.

    Returns:
        pd.DataFrame: Loaded DataFrame from the latest CSV file.

    Raises:
        FileNotFoundError: If no CSV files are found in the directory.
    """
    csv_files = [
        os.path.join(data_dir, f)
        for f in os.listdir(data_dir)
        if f.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in '{data_dir}' directory.")

    latest_file = max(csv_files, key=os.path.getmtime)
    print(f"🕵️‍♂️ Using latest file: {latest_file}")
    return pd.read_csv(latest_file)
