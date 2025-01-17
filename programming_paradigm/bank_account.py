class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        elif amount > self.account_balance:
            return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
