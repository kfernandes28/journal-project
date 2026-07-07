from pathlib import Path
import csv
import subprocess
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "Data" / "Thoughts.csv"

today = datetime.today().strftime("%d/%m/%Y")

print("Journal Capture")
print("----------------")

date_input = input(f"\nDate (DD/MM/YYYY, Enter = today): [{today}] ").strip()

if date_input:
    timestamp = datetime.strptime(date_input, "%d/%m/%Y").strftime("%d/%m/%Y")
else:
    timestamp = today

print("\nCopy your thought to the clipboard first.")
input("Press Enter to import from clipboard...")

thought = subprocess.run(
    ["pbpaste"],
    capture_output=True,
    text=True
).stdout.strip()

if not thought:
    print("No thought entered. Nothing saved.")
    exit()

# Ensure the existing CSV ends with a newline before appending as it was adding it as a new column instead
with CSV_PATH.open("rb+") as file:
    file.seek(0, 2)
    if file.tell() > 0:
        file.seek(-1, 2)
        if file.read(1) != b"\n":
            file.write(b"\n")

with CSV_PATH.open("a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([timestamp, thought])

print("Thought saved.")

print("Rebuilding dashboard...")

subprocess.run(
    ["python3", str(PROJECT_ROOT / "Scripts" / "build_dashboard.py")],
    check=True
)

print("Dashboard updated.")