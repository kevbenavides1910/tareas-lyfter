def display_menu():
    print("\nAvailable Operations:")
    print("  [1] Add      [2] Subtract  [3] Multiply")
    print("  [4] Divide   [5] Reset     [6] Exit")
    print("  (Type 'm' to show this menu again)")

def get_number(prompt_text):
    """Safely gets a float from the user."""
    try:
        user_input = input(prompt_text)
        return float(user_input)
    except ValueError:
        print("!! Invalid input: Please enter a numeric value.")
        return None

def run_calculator():
    """Main calculator logic with improved UX and bug fixes."""
    current_value = 0.0
    # Definimos los nombres de las operaciones una sola vez
    op_names = {'1': 'Add', '2': 'Subtract', '3': 'Multiply', '4': 'Divide'}
    
    display_menu()
    
    while True:
        print(f"\n>>> CURRENT TOTAL: {current_value}")
        
        selection = input("Operation [1-6/m]: ").lower().strip()

        # 1. Salida del programa
        if selection == '6':
            print("Goodbye!")
            break
        
        # 2. Reinicio del valor
        if selection == '5':
            current_value = 0.0
            print("Value reset to 0.")
            continue
            
        # 3. Mostrar menú de nuevo
        if selection == 'm':
            display_menu()
            continue

        # 4. Validación de opciones (La corrección principal)
        if selection not in op_names:
            print("!! Invalid option. Type 'm' for menu.")
            continue # Esto evita que el código siga hacia abajo y cause un KeyError

        # 5. Obtención del segundo número
        new_number = get_number(f"Number to {op_names[selection]}: ")
        
        if new_number is None:
            continue

        # 6. Ejecución de operaciones
        if selection == '1':
            current_value += new_number
        elif selection == '2':
            current_value -= new_number
        elif selection == '3':
            current_value *= new_number
        elif selection == '4':
            try:
                current_value /= new_number
            except ZeroDivisionError:
                print("!! Math Error: Cannot divide by zero.")

if __name__ == "__main__":
    run_calculator()