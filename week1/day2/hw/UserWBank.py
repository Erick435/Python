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
        return self

    def display_account_info(self):
        print("Balance: $", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0, 0.02)

    def user_name(self):
        pass

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self


    def user_account_info(self):
        print("User: " + str(self.name) + ", Balance: $" + str(self.account.balance))
        return self

erick = User("Erick")
richard = User("Richard")
erick.make_deposit(150).make_withdrawal(75).user_account_info()
richard.make_deposit(250).make_deposit(50).make_deposit(125).make_withdrawal(300).user_account_info()

    # def make_withdrawal(self, amount):
    #     self.account_balance -= amount

    # def display_user_balance(self):
    #     print("User:" + str(self.name) + ", Balance: $" + str(self.account_balance))



#we can call the BankAccount instance's method
#self.account.deposit(100)

#or acces its attributes by stating
#print(self.account.balance)