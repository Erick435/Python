class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
        self.other_user_balance = self.account_balance
        


    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:" + str(self.name) + ", Balance: $" + str(self.account_balance))
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     self.amount += amount
    #     self.other_user_balance += amount
        
        

guido = User("Guido van Rossum")
monty = User("Monty Python")
erick = User("Erick Ortega")

print("\n")
guido.make_deposit(250).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

monty.make_deposit(640).make_deposit(320).make_withdrawal(100).make_withdrawal(275).display_user_balance()

erick.make_deposit(1250).make_withdrawal(150).make_withdrawal(50).make_withdrawal(550).display_user_balance()

# guido.transfer_money(100, "Erick Ortega")
# guido.display_user_balance()
# erick.display_user_balance()

print("\n")
