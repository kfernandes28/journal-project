from pathlib import Path
import csv
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "Data" / "Thoughts.csv"


date_input = input("Enter date (DD/MM/YYYY), or press Enter for today: ").strip()

if date_input:
    timestamp = datetime.strptime(date_input, "%d/%m/%Y").strftime("%d/%m/%Y")
else:
    timestamp = datetime.today().strftime("%d/%m/%Y")

thought = input("Paste thought: ").strip()

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