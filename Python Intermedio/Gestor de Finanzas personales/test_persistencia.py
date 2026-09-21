import os
import tempfile
import unittest

from persistencia import DEFAULT_DATA, JsonFinanceRepository, export_transactions_to_csv


class TestJsonFinanceRepository(unittest.TestCase):
    """Tests for JsonFinanceRepository. Uses a temp directory so tests
    never touch real project files and clean up after themselves."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "finanzas.json")
        self.repository = JsonFinanceRepository(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_returns_default_data_when_file_does_not_exist(self):
        result = self.repository.load()

        self.assertEqual(result, DEFAULT_DATA)

    def test_save_creates_the_file(self):
        self.repository.save({"categories": [], "transactions": []})

        self.assertTrue(os.path.exists(self.file_path))

    def test_save_then_load_returns_the_same_data(self):
        data = {
            "categories": [{"name": "Comida", "color": "#FFA500"}],
            "transactions": [
                {
                    "title": "Almuerzo",
                    "amount": 15,
                    "category": "Comida",
                    "transaction_type": "expense",
                    "date": "2026-01-01",
                }
            ],
        }

        self.repository.save(data)
        result = self.repository.load()

        self.assertEqual(result, data)

    def test_save_overwrites_previous_data(self):
        self.repository.save({"categories": [{"name": "Comida", "color": None}], "transactions": []})
        self.repository.save({"categories": [{"name": "Transporte", "color": None}], "transactions": []})

        result = self.repository.load()

        self.assertEqual(result["categories"], [{"name": "Transporte", "color": None}])

    def test_save_creates_missing_parent_directories(self):
        nested_path = os.path.join(self.temp_dir.name, "data", "subfolder", "finanzas.json")
        repository = JsonFinanceRepository(nested_path)

        repository.save({"categories": [], "transactions": []})

        self.assertTrue(os.path.exists(nested_path))

    def test_load_returns_default_data_for_corrupted_file(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("{ esto no es JSON valido")

        result = self.repository.load()

        self.assertEqual(result, DEFAULT_DATA)


class TestExportTransactionsToCsv(unittest.TestCase):
    """Tests for export_transactions_to_csv. Uses a temp directory."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "export.csv")
        self.rows = [
            {
                "date": "01/07/2025",
                "title": "Salario",
                "amount": 1200,
                "category": "Trabajo",
                "type_label": "Ingreso",
            },
            {
                "date": "02/07/2025",
                "title": "Comida",
                "amount": -100,
                "category": "Alimentación",
                "type_label": "Gasto",
            },
        ]
        self.totals = {"income": 1200, "expenses": 100, "balance": 1100}

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_creates_the_csv_file(self):
        export_transactions_to_csv(self.file_path, self.rows, self.totals)

        self.assertTrue(os.path.exists(self.file_path))

    def test_csv_contains_headings_and_row_data(self):
        export_transactions_to_csv(self.file_path, self.rows, self.totals)

        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertIn("Fecha,Título,Monto,Categoría,Tipo", content)
        self.assertIn("01/07/2025,Salario,1200,Trabajo,Ingreso", content)
        self.assertIn("02/07/2025,Comida,-100,Alimentación,Gasto", content)

    def test_csv_contains_totals(self):
        export_transactions_to_csv(self.file_path, self.rows, self.totals)

        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertIn("Ingresos,1200", content)
        self.assertIn("Gastos,100", content)
        self.assertIn("Balance Neto,1100", content)

    def test_creates_missing_parent_directories(self):
        nested_path = os.path.join(self.temp_dir.name, "exports", "reporte.csv")

        export_transactions_to_csv(nested_path, self.rows, self.totals)

        self.assertTrue(os.path.exists(nested_path))


if __name__ == "__main__":
    unittest.main()
