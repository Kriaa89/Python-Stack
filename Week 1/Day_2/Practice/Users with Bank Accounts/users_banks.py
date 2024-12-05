class BankAccount:
    def __init__(self, init_rate=0.02, balance=0):
        self.init_rate = init_rate
        self.balance = balance

    def deposit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            print("Users with Bank Accounts")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.init_rate
            return self 
    def display_account_info(self):
        print(f"Balance: ${self.balance: .2f}")
        return self
    
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {} # dictionary to hold accounts
    def add_account(self, account_name, in_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(in_rate, balance)
        return self
    
    def make_deposit(self, account_anme, amount):
        if account_anme in self.accounts:
            self.accounts[account_anme]
        print:(f"account '{account_name} does not exist.")
        return self
    
    def make_withdrawl(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else: 
            print:(f"account '{account_name} does not exist.")
        return self
    def display_user_balance(self, account_name): 
        if account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        else: 
            print(f"Account '{account_name}' does not exist.")
        return self
    
    def transfer_money(self, amount, other_user, from_account, to_account):
        if from_account in self.accounts and to_account in other_user.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].withdraw(amount)
                other_user.accounts[to_account].deposit(amount)
                print(f"Transfered ${amount} from {self.name} {from_account} to {to_account}.")
            else:
                print("sorry no transfer.")
        else:
            print("one of the accounts does not exist.")

# creating user 
user1 = user("abdallah", "abdallahkriaa@gmailcom")
user2 = user("yessine", "yessine@gmailcom")

# adding account to users
user1.add_account("saving", 0.01, 100).add_account("checking", 0.02, 200)
user2.add_account("saving", 0.01, 150).add_account("checking", 0.02, 300)

user1.make_deposit("saving", 50).make_deposit("saving", 100).make_deposit("saving",200).make_withdrawl("saving", 150).accounts["saving"].yield_interest().display_account_info()
user2.make_deposit("chekcing", 300).make_deposit("chekcing", 200).make_deposit("chekcing",200).make_withdrawl("chekcing", 50).make_withdrawl("chekcing", 100).make_withdrawl("chekcing", 200).make_withdrawl("checking", 50).accounts["checking"].yield_interest().display_account_info()

user1.transfer_money(100, user2, "savings", "checking")

# display all accounts info for both users
print("user1 Account:")
for account_name in user1.accounts:
    user1.display_user_balance(account_name)

print("user2 Account:")
for account_name in user2.accounts:
    user2.display_user_balance(account_name)