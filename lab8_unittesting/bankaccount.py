"""
BankAccount Class
Samuel Martinez
"""

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        try:
            if amount > 0:
                self.balance += amount
                print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Error! Deposit amount must be positive.")
        except ValueError:
            print("Error! Invalid deposit amount.")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                print(f"Error! Insufficient funds. Cannot withdraw ${amount:.2f}.")
            elif amount > 0:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Error! Withdrawal amount must be positive.")
        except ValueError:
            print("Error! Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance



