class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def balance_enq(self):
        print(f"Current balance: {self.balance}")


# Example usage
account = Account(1000)  # Start with an initial balance of 1000

account.balance_enq()  # Check balance
account.deposit(500)   # Deposit 500
account.balance_enq()
account.withdraw(200)  # Withdraw 200
account.balance_enq()  # Check balance again
account.withdraw(2000)
account.balance_enq()  