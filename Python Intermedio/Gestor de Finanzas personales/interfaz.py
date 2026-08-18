"""Presentation layer for the personal finance manager.

This module owns everything related to FreeSimpleGUI: building
windows, reading form values, and turning FinanceManager exceptions
into user-facing error popups. It contains no business rules itself —
every rule (category must exist, amount must be positive, date format,
etc.) lives in logica.py and is simply displayed here when it raises.
"""

import FreeSimpleGUI as sg

from logica import today_str
from persistencia import export_transactions_to_csv

TRANSACTION_TABLE_HEADINGS = ["Fecha", "Título", "Categoría", "Tipo", "Monto"]


def parse_amount(amount_text):
    """Convert user input to a float, accepting both '.' and ',' as decimal separator."""
    normalized_text = amount_text.strip().replace(",", ".")
    return float(normalized_text)


def build_transaction_row(transaction):
    """Convert a Transaction into a row for the main table."""
    type_label = "Ingreso" if transaction.transaction_type == "income" else "Gasto"
    return [
        transaction.date,
        transaction.title,
        transaction.category,
        type_label,
        f"{transaction.amount:.2f}",
    ]


def build_rows_and_colors(finance_manager, transactions):
    """Build table rows plus a row_colors list based on each category's color."""
    category_colors = {c.name: c.color for c in finance_manager.categories if c.color}

    rows = []
    row_colors = []
    for index, transaction in enumerate(transactions):
        rows.append(build_transaction_row(transaction))
        color = category_colors.get(transaction.category)
        if color:
            row_colors.append((index, color))

    return rows, row_colors


def update_table(window, finance_manager, transactions):
    rows, row_colors = build_rows_and_colors(finance_manager, transactions)
    window["-TABLE-"].update(values=rows, row_colors=row_colors)


def build_main_window(finance_manager):
    layout = [
        [sg.Text("Gestor de Finanzas Personales", font=("Any", 14))],
        [
            sg.Table(
                values=[],
                headings=TRANSACTION_TABLE_HEADINGS,
                key="-TABLE-",
                auto_size_columns=True,
                expand_x=True,
                num_rows=12,
            )
        ],
        [
            sg.Button("Agregar categoría", key="-ADD-CATEGORY-"),
            sg.Button("Agregar gasto", key="-ADD-EXPENSE-"),
            sg.Button("Agregar ingreso", key="-ADD-INCOME-"),
            sg.Button("Exportar a CSV", key="-EXPORT-CSV-"),
        ],
        [
            sg.Text("Desde:"),
            sg.Input(key="-FILTER-START-", size=(10, 1)),
            sg.Text("Hasta:"),
            sg.Input(key="-FILTER-END-", size=(10, 1)),
            sg.Button("Filtrar", key="-FILTER-"),
            sg.Button("Quitar filtro", key="-CLEAR-FILTER-"),
        ],
        [sg.Text("", key="-BALANCE-", font=("Any", 12))],
    ]
    return sg.Window("Gestor de Finanzas Personales", layout, finalize=True)


def refresh_main_window(window, finance_manager):
    """Show all transactions and the overall balance (clears any active filter)."""
    update_table(window, finance_manager, finance_manager.get_all_transactions())
    window["-BALANCE-"].update(f"Balance: {finance_manager.get_balance():.2f}")


def show_add_category_window():
    """Open a small window to collect a category name and color.

    Returns a tuple (name, color) or None if cancelled. `color` may be
    None if the user didn't pick one.
    """
    layout = [
        [sg.Text("Nombre de la categoría:")],
        [sg.Input(key="-NAME-")],
        [
            sg.Text("Color:"),
            sg.Input(key="-COLOR-", size=(10, 1), disabled=True),
            sg.ColorChooserButton("Elegir color", target="-COLOR-"),
        ],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    window = sg.Window("Agregar categoría", layout, modal=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            window.close()
            return None

        if event == "Guardar":
            name = values["-NAME-"].strip()
            if not name:
                sg.popup_error("El nombre de la categoría no puede estar vacío")
                continue

            color = values["-COLOR-"].strip() or None
            window.close()
            return name, color


def show_add_transaction_window(category_names, title_text):
    """Open a window to collect title, amount, category, and date for a transaction.

    Returns a tuple (title, amount, category, date) or None if cancelled.
    """
    layout = [
        [sg.Text(title_text, font=("Any", 12))],
        [sg.Text("Título:"), sg.Input(key="-TITLE-")],
        [sg.Text("Monto:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Categoría:"), sg.Combo(category_names, key="-CATEGORY-", readonly=True)],
        [sg.Text("Fecha (dd/mm/yyyy):"), sg.Input(key="-DATE-", default_text=today_str())],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    window = sg.Window(title_text, layout, modal=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            window.close()
            return None

        if event == "Guardar":
            title = values["-TITLE-"].strip()
            category = values["-CATEGORY-"]
            amount_text = values["-AMOUNT-"].strip()
            date_text = values["-DATE-"].strip()

            if not title or not category:
                sg.popup_error("Debe completar el título y seleccionar una categoría")
                continue

            try:
                amount = parse_amount(amount_text)
            except ValueError:
                sg.popup_error("El monto debe ser un número válido")
                continue

            window.close()
            return title, amount, category, date_text


def handle_add_category(finance_manager, window):
    result = show_add_category_window()
    if result is None:
        return

    name, color = result
    try:
        finance_manager.add_category(name, color)
    except ValueError as error:
        sg.popup_error(str(error))
        return

    refresh_main_window(window, finance_manager)


def handle_add_expense(finance_manager, window):
    _handle_add_transaction(finance_manager, window, "Agregar gasto", finance_manager.add_expense)


def handle_add_income(finance_manager, window):
    _handle_add_transaction(finance_manager, window, "Agregar ingreso", finance_manager.add_income)


def _handle_add_transaction(finance_manager, window, title_text, add_method):
    category_names = [category.name for category in finance_manager.categories]

    if not category_names:
        sg.popup_error("No hay categorías disponibles. Agregue una categoría primero.")
        return

    result = show_add_transaction_window(category_names, title_text)
    if result is None:
        return

    title, amount, category, date = result
    try:
        add_method(title, amount, category, date=date)
    except ValueError as error:
        sg.popup_error(str(error))
        return

    refresh_main_window(window, finance_manager)


def handle_filter(finance_manager, window, values):
    start_date = values["-FILTER-START-"].strip()
    end_date = values["-FILTER-END-"].strip()

    try:
        transactions = finance_manager.get_transactions_in_range(start_date, end_date)
    except ValueError as error:
        sg.popup_error(str(error))
        return

    update_table(window, finance_manager, transactions)
    window["-BALANCE-"].update(
        f"Mostrando {len(transactions)} movimiento(s) entre {start_date} y {end_date}"
    )


def handle_clear_filter(finance_manager, window):
    refresh_main_window(window, finance_manager)


def handle_export_csv(finance_manager, window):
    file_path = sg.popup_get_file(
        "Guardar como",
        save_as=True,
        default_extension=".csv",
        file_types=(("CSV", "*.csv"),),
        no_window=True,
    )
    if not file_path:
        return

    export_transactions_to_csv(
        file_path, finance_manager.get_export_rows(), finance_manager.get_totals()
    )
    sg.popup("Movimientos exportados correctamente")


def start_main_window(finance_manager):
    """Build the main window and run its event loop until the user closes it."""
    window = build_main_window(finance_manager)
    refresh_main_window(window, finance_manager)

    event_handlers = {
        "-ADD-CATEGORY-": lambda fm, win, vals: handle_add_category(fm, win),
        "-ADD-EXPENSE-": lambda fm, win, vals: handle_add_expense(fm, win),
        "-ADD-INCOME-": lambda fm, win, vals: handle_add_income(fm, win),
        "-EXPORT-CSV-": lambda fm, win, vals: handle_export_csv(fm, win),
        "-FILTER-": handle_filter,
        "-CLEAR-FILTER-": lambda fm, win, vals: handle_clear_filter(fm, win),
    }

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        handler = event_handlers.get(event)
        if handler:
            handler(finance_manager, window, values)

    window.close()
