
from pathlib import Path
import pandas as pd

# STEP 1: Define project and dataset paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_PATH = PROJECT_ROOT / "data" / "raw" / (
    "PRSA_Data_Aotizhongxin_20130301-20170228.csv"
)

# STEP 2: Check dataset existence
if not CSV_PATH.is_file():
    raise FileNotFoundError(f"Dataset not found: {CSV_PATH}")

# STEP 3: Load CSV
df = pd.read_csv(CSV_PATH)

print("DATASET LOADED")
print("Rows and columns:", df.shape)
print("Column names:", df.columns.tolist())
print("First five rows:")
print(df.head())

# STEP 4: Inspect data types
print("\nDATA TYPES")
print(df.dtypes)

# STEP 5: Check missing values
print("\nMISSING VALUES PER COLUMN")
missing_counts = df.isna().sum()
print(missing_counts)

print("\nTOTAL MISSING CELLS")
print(missing_counts.sum())

# STEP 6: PM2.5 statistics
print("\nPM2.5 SUMMARY")
print(df["PM2.5"].describe())

# STEP 7: Duplicate rows
print("\nNUMBER OF DUPLICATE ROWS")
print(df.duplicated().sum())

# STEP 8: Create timestamp
df["timestamp"] = pd.to_datetime(
    df[["year", "month", "day", "hour"]]
)

print("\nTIME RANGE")
print("First timestamp:", df["timestamp"].min())
print("Last timestamp:", df["timestamp"].max())
print("Timestamps sorted:", df["timestamp"].is_monotonic_increasing)

# STEP 9: Save inspection report
report_path = PROJECT_ROOT / "reports" / "inspection_report.txt"

with report_path.open("w", encoding="utf-8") as report:
    report.write(f"Shape: {df.shape}\n")
    report.write("Missing values by column:\n")
    report.write(missing_counts.to_string())
    report.write("\n\nPM2.5 summary:\n")
    report.write(df["PM2.5"].describe().to_string())
    report.write("\n")

print("Report saved to:", report_path)
