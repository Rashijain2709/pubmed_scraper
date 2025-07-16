import csv
from typing import List, Dict

def write_to_csv(data: List[Dict], filename: str) -> None:
    if not data:
        print("[WARNING] No data provided to write.")
        return

    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except (IOError, OSError) as e:
        print(f"[ERROR] Failed to write to {filename}: {e}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while writing to CSV: {e}")
