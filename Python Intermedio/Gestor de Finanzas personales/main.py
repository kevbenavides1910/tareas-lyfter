"""Entry point for the personal finance manager.

This is the only module allowed to know about interfaz.py, logica.py,
and persistencia.py at the same time. It wires them together and
starts the GUI event loop. No business rules and no widget code live
here — just construction and delegation.
"""

import os

from interfaz import start_main_window
from logica import FinanceManager
from persistencia import JsonFinanceRepository

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "finanzas.json")


def main():
    repository = JsonFinanceRepository(DATA_FILE_PATH)
    finance_manager = FinanceManager(repository)
    start_main_window(finance_manager)


if __name__ == "__main__":
    main()
