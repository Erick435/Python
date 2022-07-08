class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
        self.other_user_balance = self.account_balance
        


    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User:" + str(self.name) + ", Balance: $" + str(self.account_balance))

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        self.amount += amount
        self.other_user_balance += amount
        
        

guido = User("Guido van Rossum")
monty = User("Monty Python")
erick = User("Erick Ortega")

print("\n")
guido.make_deposit(250)
guido.make_deposit(150)
guido.make_deposit(75)
guido.make_withdrawal(100)
guido.display_user_balance()

monty.make_deposit(640)
monty.make_deposit(320)
monty.make_withdrawal(100)
monty.make_withdrawal(275)
monty.display_user_balance()

erick.make_deposit(1250)
erick.make_withdrawal(150)
erick.make_withdrawal(50)
erick.make_withdrawal(550)
erick.display_user_balance()

guido.transfer_money(100, "Erick Ortega")
guido.display_user_balance()
erick.display_user_balance()

print("\n")
