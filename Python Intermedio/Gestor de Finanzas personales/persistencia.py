"""Concrete storage for the personal finance manager.

JsonFinanceRepository knows nothing about Category or Transaction
objects — it only reads and writes plain dictionaries/lists to a JSON
file. FinanceManager (in logica.py) is responsible for converting its
domain objects to and from those plain structures.
"""

import csv
import json
import os

DEFAULT_DATA = {"categories": [], "transactions": []}
CSV_HEADINGS = ["Fecha", "Título", "Monto", "Categoría", "Tipo"]


class JsonFinanceRepository:
    """Loads and saves finance data to a JSON file on disk."""

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return dict(DEFAULT_DATA)

        with open(self.file_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                # Empty or corrupted file: start fresh instead of crashing.
                return dict(DEFAULT_DATA)

    def save(self, data):
        directory = os.path.dirname(self.file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


def export_transactions_to_csv(file_path, rows, totals):
    """Write transaction rows and totals to a CSV file.

    `rows` and `totals` are plain dicts (as returned by
    FinanceManager.get_export_rows() / get_totals()) — this function
    has no knowledge of Transaction or Category objects, keeping the
    file-writing concern separate from the domain model.
    """
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADINGS)

        for row in rows:
            writer.writerow(
                [row["date"], row["title"], row["amount"], row["category"], row["type_label"]]
            )

        writer.writerow([])
        writer.writerow(["Totales:"])
        writer.writerow(["Ingresos", totals["income"]])
        writer.writerow(["Gastos", totals["expenses"]])
        writer.writerow(["Balance Neto", totals["balance"]])
