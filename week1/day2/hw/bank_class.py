# declare a class and give it name User
class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):


    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
#the specific user's account increases by the amount of the value recieved




guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print("\n")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python


print("\n")
#changing the bank's name on an instance/object
print(guido.bank_name) #output: Dojo Credit Union
print(monty.bank_name) #output: First National Dojo

# Accessing the instance's attributes
print("\n")
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael
print("\n")


guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty
print("\n")

User.bank_name = "Bank of Dojo"
#this changes the bank's name within the class
print(guido.bank_name)
print(monty.bank_name)
print("\n")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
print("\n")

