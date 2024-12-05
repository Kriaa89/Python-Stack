class BankAccount:
    def __init__(self, in_rate, balance=0):
        self.in_rate = in_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
        else:
            print("Insufficient funds: Charging a $5 ")
            self.balance -= 5 
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.in_rate
        return self 

account1 = BankAccount(0.01, 100)
account2 = BankAccount(0.02, 200)

account1.deposit(50).deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()
account2.deposit(100).deposit(50).withdraw(30).withdraw(30).withdraw(50).withdraw(200).yield_interest().display_account_info()