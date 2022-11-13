

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(amount, description=""):
        self.balance += float(amount)
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(amount, description=""):
        self.balance -= float(amount)
        self.ledger.append({"amount": float(amount), "description": description})

    def get_balance(self):
        return self.balance

    def transfer(self, amount, description):
        if self.withdraw(amount, description):
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance > amount:
            return True
        else:
            return False


Shopping_Cats = Category("Groceries")
Shopping_Cats.deposit(300)
