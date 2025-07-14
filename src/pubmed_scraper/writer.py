import csv
from typing import List, Dict

def write_to_csv(data: List[Dict], filename: str) -> None:
    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
