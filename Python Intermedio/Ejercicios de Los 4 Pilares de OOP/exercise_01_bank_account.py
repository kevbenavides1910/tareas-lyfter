class BankAccount:
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance: float = 0.0, min_balance: float = 0.0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"Withdrawal denied: balance would fall below minimum ({self.min_balance})."
            )
        self.balance -= amount


def prompt_float(message: str) -> float:
    """Ask the user for a float value, retrying on invalid input."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def run_bank_account() -> None:
    """Interactive demo for BankAccount."""
    print("\n--- BankAccount ---")
    initial_balance = prompt_float("Enter initial balance: ")
    account = BankAccount(balance=initial_balance)

    deposit_amount = prompt_float("Enter amount to deposit: ")
    try:
        account.deposit(deposit_amount)
        print(f"Balance after deposit: {account.balance}")
    except ValueError as e:
        print(f"Error: {e}")

    withdraw_amount = prompt_float("Enter amount to withdraw: ")
    try:
        account.withdraw(withdraw_amount)
        print(f"Balance after withdrawal: {account.balance}")
    except ValueError as e:
        print(f"Error: {e}")


def run_savings_account() -> None:
    """Interactive demo for SavingsAccount."""
    print("\n--- SavingsAccount ---")
    initial_balance = prompt_float("Enter initial balance: ")
    min_balance = prompt_float("Enter minimum balance allowed: ")
    savings = SavingsAccount(balance=initial_balance, min_balance=min_balance)

    withdraw_amount = prompt_float("Enter amount to withdraw: ")
    try:
        savings.withdraw(withdraw_amount)
        print(f"Balance after withdrawal: {savings.balance}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_bank_account()
    run_savings_account()
