class BankAccount:
    def __init__(self, balance = 0, interest_rate = 0.01):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        return(self)

    def display_account_info(self):
        print("Balance: $", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self


bank1 = BankAccount()
bank2 = BankAccount(100)

print("\n")
bank1.deposit(250).deposit(100).deposit(75).withdraw(285).yield_interest().display_account_info()
print("\n")

bank2.deposit(150).deposit(565).withdraw(75).withdraw(190).withdraw(25).withdraw(85).yield_interest().display_account_info()
print("\n")