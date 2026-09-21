import unittest

from logica import FinanceManager, Transaction, parse_date, validate_transaction_date


class InMemoryFinanceRepository:
    """Fake repository that keeps data in memory instead of writing to disk.

    Used only in tests so FinanceManager can be exercised without any
    real file I/O, per the exercise's requirement that tests run
    independently of the GUI and persistence layer.
    """

    def __init__(self, initial_data=None):
        self.data = initial_data or {"categories": [], "transactions": []}
        self.save_call_count = 0

    def load(self):
        return self.data

    def save(self, data):
        self.data = data
        self.save_call_count += 1


class TestFinanceManagerCategories(unittest.TestCase):
    """Tests for category-related behavior."""

    def setUp(self):
        self.repository = InMemoryFinanceRepository()
        self.manager = FinanceManager(self.repository)

    def test_add_category_registers_it(self):
        self.manager.add_category("Comida")

        self.assertTrue(self.manager.category_exists("Comida"))

    def test_add_duplicate_category_raises_error(self):
        self.manager.add_category("Comida")

        with self.assertRaises(ValueError):
            self.manager.add_category("Comida")

    def test_add_category_triggers_a_save(self):
        self.manager.add_category("Comida")

        self.assertEqual(self.repository.save_call_count, 1)


class TestFinanceManagerTransactions(unittest.TestCase):
    """Tests for adding expenses and incomes."""

    def setUp(self):
        self.repository = InMemoryFinanceRepository()
        self.manager = FinanceManager(self.repository)
        self.manager.add_category("Comida")

    def test_add_expense_with_valid_category_succeeds(self):
        self.manager.add_expense("Almuerzo", 15, "Comida")

        transactions = self.manager.get_all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].transaction_type, Transaction.EXPENSE)

    def test_add_income_with_valid_category_succeeds(self):
        self.manager.add_income("Salario", 1000, "Comida")

        transactions = self.manager.get_all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].transaction_type, Transaction.INCOME)

    def test_add_expense_without_any_category_raises_error(self):
        empty_manager = FinanceManager(InMemoryFinanceRepository())

        with self.assertRaises(ValueError):
            empty_manager.add_expense("Almuerzo", 15, "Comida")

    def test_add_expense_with_nonexistent_category_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense("Almuerzo", 15, "Transporte")

    def test_add_transaction_with_non_positive_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense("Almuerzo", 0, "Comida")

        with self.assertRaises(ValueError):
            self.manager.add_income("Salario", -100, "Comida")


class TestFinanceManagerBalance(unittest.TestCase):
    """Tests for balance and totals calculations."""

    def setUp(self):
        self.repository = InMemoryFinanceRepository()
        self.manager = FinanceManager(self.repository)
        self.manager.add_category("Comida")
        self.manager.add_category("Trabajo")

    def test_get_balance_reflects_income_and_expenses(self):
        self.manager.add_income("Salario", 1000, "Trabajo")
        self.manager.add_expense("Almuerzo", 200, "Comida")

        self.assertEqual(self.manager.get_balance(), 800)

    def test_get_total_income_sums_only_income_transactions(self):
        self.manager.add_income("Salario", 1000, "Trabajo")
        self.manager.add_expense("Almuerzo", 200, "Comida")

        self.assertEqual(self.manager.get_total_income(), 1000)

    def test_get_total_expenses_sums_only_expense_transactions(self):
        self.manager.add_income("Salario", 1000, "Trabajo")
        self.manager.add_expense("Almuerzo", 200, "Comida")
        self.manager.add_expense("Bus", 50, "Comida")

        self.assertEqual(self.manager.get_total_expenses(), 250)


class TestFinanceManagerLoadsExistingData(unittest.TestCase):
    """Tests that FinanceManager correctly loads data already present in the repository."""

    def test_loads_categories_and_transactions_on_init(self):
        existing_data = {
            "categories": [{"name": "Comida", "color": None}],
            "transactions": [
                {
                    "title": "Almuerzo",
                    "amount": 15,
                    "category": "Comida",
                    "transaction_type": Transaction.EXPENSE,
                    "date": "2026-01-01",
                }
            ],
        }
        repository = InMemoryFinanceRepository(initial_data=existing_data)

        manager = FinanceManager(repository)

        self.assertTrue(manager.category_exists("Comida"))
        self.assertEqual(len(manager.get_all_transactions()), 1)


class TestDateValidation(unittest.TestCase):
    """Tests for the standalone date-parsing/validation helpers."""

    def test_parse_date_accepts_correct_format(self):
        result = parse_date("20/07/2025")

        self.assertEqual(result.isoformat(), "2025-07-20")

    def test_parse_date_rejects_wrong_format(self):
        with self.assertRaises(ValueError):
            parse_date("2025-07-20")

    def test_validate_transaction_date_rejects_future_date(self):
        with self.assertRaises(ValueError):
            validate_transaction_date("01/01/2099")

    def test_validate_transaction_date_accepts_past_date(self):
        # Should not raise for a date that has already happened.
        validate_transaction_date("01/01/2020")


class TestAddTransactionWithCustomDate(unittest.TestCase):
    """Tests for adding a transaction with a user-supplied date."""

    def setUp(self):
        self.repository = InMemoryFinanceRepository()
        self.manager = FinanceManager(self.repository)
        self.manager.add_category("Comida")

    def test_add_expense_with_valid_custom_date_succeeds(self):
        transaction = self.manager.add_expense("Pizza", 40, "Comida", date="03/07/2025")

        self.assertEqual(transaction.date, "03/07/2025")

    def test_add_expense_with_invalid_date_format_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense("Pizza", 40, "Comida", date="2025/07/03")

    def test_add_expense_with_future_date_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense("Pizza", 40, "Comida", date="01/01/2099")


class TestGetTransactionsInRange(unittest.TestCase):
    """Tests for filtering transactions by a date range."""

    def setUp(self):
        self.repository = InMemoryFinanceRepository()
        self.manager = FinanceManager(self.repository)
        self.manager.add_category("Trabajo")
        self.manager.add_category("Comida")
        self.manager.add_income("Salario", 1000, "Trabajo", date="02/07/2025")
        self.manager.add_expense("Comida", 20, "Comida", date="03/07/2025")
        self.manager.add_expense("Ropa", 50, "Comida", date="12/07/2025")

    def test_returns_only_transactions_inside_the_range(self):
        result = self.manager.get_transactions_in_range("01/07/2025", "10/07/2025")

        titles = [t.title for t in result]
        self.assertEqual(titles, ["Salario", "Comida"])

    def test_returns_empty_list_when_no_transaction_is_in_range(self):
        result = self.manager.get_transactions_in_range("01/01/2025", "01/02/2025")

        self.assertEqual(result, [])

    def test_raises_error_when_start_date_is_after_end_date(self):
        with self.assertRaises(ValueError):
            self.manager.get_transactions_in_range("10/07/2025", "01/07/2025")


if __name__ == "__main__":
    unittest.main()
