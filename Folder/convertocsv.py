import pandas as pd
import os
from glob import glob

# Folder containing the Excel files
folder = r"C:\Users\ppd19\Desktop\practice\upi daily stats from npci"

# Find all .xlsx files
excel_files = glob(os.path.join(folder, "*.xlsx"))

for file in excel_files:
    # Read the first sheet
    df = pd.read_excel(file)

    # Create CSV filename
    csv_file = os.path.splitext(file)[0] + ".csv"

    # Save as CSV
    df.to_csv(csv_file, index=False)

    print(f"Converted: {file} -> {csv_file}")

print("\nAll files converted successfully!")
