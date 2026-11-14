# Bank Transactions
class Customer:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Invalid value entry")
        else:
            self.balance += amount
            print(f"Deposited - {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            print(f"Withdrawn - {amount}")

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Email: {self.email}")
        print(f"Initial Balance: {self.balance}")

    def display_balance(self):
        print(f"Current Balance - {self.balance}")

eg = Customer("Alb", "Alb@gmail.com", 8000)
eg.display_details()
eg.deposit(2000)
eg.withdraw(1000)
eg.display_balance()