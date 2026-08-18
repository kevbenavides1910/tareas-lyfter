"""Core domain logic for the personal finance manager.

This module has no dependency on the GUI (interfaz.py) or on the
concrete storage mechanism (persistencia.py). FinanceManager receives
a repository object through its constructor (dependency injection),
so it can be tested with an in-memory fake repository instead of a
real JSON file.
"""

import datetime

DATE_FORMAT = "%d/%m/%Y"


def today_str():
    """Return today's date formatted as dd/mm/yyyy."""
    return datetime.date.today().strftime(DATE_FORMAT)


def parse_date(date_str):
    """Parse a dd/mm/yyyy string into a date object, or raise ValueError."""
    try:
        return datetime.datetime.strptime(date_str, DATE_FORMAT).date()
    except (ValueError, TypeError):
        raise ValueError("Formato de fecha inválido (use dd/mm/yyyy)")


def validate_transaction_date(date_str):
    """Validate that a date string is well-formed and not in the future."""
    date_obj = parse_date(date_str)
    if date_obj > datetime.date.today():
        raise ValueError("La fecha no puede ser en el futuro")
    return date_str


class Category:
    """A spending/income category, e.g. 'Comida' or 'Transporte'."""

    def __init__(self, name, color=None):
        self.name = name
        self.color = color

    def to_dict(self):
        return {"name": self.name, "color": self.color}

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], color=data.get("color"))


class Transaction:
    """A single income or expense entry."""

    INCOME = "income"
    EXPENSE = "expense"

    def __init__(self, title, amount, category, transaction_type, date=None):
        self.title = title
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date or today_str()

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            amount=data["amount"],
            category=data["category"],
            transaction_type=data["transaction_type"],
            date=data.get("date"),
        )


class FinanceManager:
    """Coordinates categories and transactions, delegating storage to a repository."""

    def __init__(self, repository):
        self.repository = repository
        self.categories = []
        self.transactions = []
        self._load_data()

    def _load_data(self):
        data = self.repository.load()
        self.categories = [Category.from_dict(c) for c in data.get("categories", [])]
        self.transactions = [
            Transaction.from_dict(t) for t in data.get("transactions", [])
        ]

    def _save_data(self):
        data = {
            "categories": [c.to_dict() for c in self.categories],
            "transactions": [t.to_dict() for t in self.transactions],
        }
        self.repository.save(data)

    def category_exists(self, name):
        return any(category.name == name for category in self.categories)

    def add_category(self, name, color=None):
        if self.category_exists(name):
            raise ValueError(f"Category '{name}' already exists")

        self.categories.append(Category(name, color))
        self._save_data()

    def add_expense(self, title, amount, category_name, date=None):
        return self._add_transaction(title, amount, category_name, Transaction.EXPENSE, date)

    def add_income(self, title, amount, category_name, date=None):
        return self._add_transaction(title, amount, category_name, Transaction.INCOME, date)

    def _add_transaction(self, title, amount, category_name, transaction_type, date=None):
        if not self.categories:
            raise ValueError("No categories available. Add a category first.")

        if not self.category_exists(category_name):
            raise ValueError(f"Category '{category_name}' does not exist")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if date is not None:
            validate_transaction_date(date)
        else:
            date = today_str()

        transaction = Transaction(title, amount, category_name, transaction_type, date=date)
        self.transactions.append(transaction)
        self._save_data()
        return transaction

    def get_all_transactions(self):
        return list(self.transactions)

    def get_transactions_in_range(self, start_date_str, end_date_str):
        """Return transactions whose date falls within [start_date_str, end_date_str], inclusive."""
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        if start_date > end_date:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha final")

        return [
            transaction
            for transaction in self.transactions
            if start_date <= parse_date(transaction.date) <= end_date
        ]

    def get_total_income(self):
        return sum(
            t.amount for t in self.transactions if t.transaction_type == Transaction.INCOME
        )

    def get_total_expenses(self):
        return sum(
            t.amount for t in self.transactions if t.transaction_type == Transaction.EXPENSE
        )

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    def get_totals(self):
        return {
            "income": self.get_total_income(),
            "expenses": self.get_total_expenses(),
            "balance": self.get_balance(),
        }

    def get_export_rows(self):
        """Return plain dict rows (no domain objects) ready for a CSV exporter."""
        rows = []
        for transaction in self.transactions:
            type_label = "Ingreso" if transaction.transaction_type == Transaction.INCOME else "Gasto"
            rows.append(
                {
                    "date": transaction.date,
                    "title": transaction.title,
                    "amount": transaction.amount,
                    "category": transaction.category,
                    "type_label": type_label,
                }
            )
        return rows
