
from multiprocessing.sharedctypes import Value
from tokenize import Number
from unicodedata import numeric


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'},
    
]



sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

print("\n")
x[1][0] = 15;
print(x)

print("\n")
students[0]['last_name'] = 'Bryant'
print(students)
print("\n")

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
print("\n")

z[0]['y'] = 30
print(z)
print("\n")

def iterateDictionary(some_list):
    for current_dictionary in some_list:
        for key, value in current_dictionary.items():
            print( key + " - " + value)
    print("\n")

iterateDictionary(students)


def iterateDictionary2(key_name, some_list):
    for current_dictionary in some_list:
        for key, value in current_dictionary.items():
            if (key_name == key):
                print(value)
                

iterateDictionary2('first_name', students)
print("\n\n")
iterateDictionary2('last_name', students)
print("\n")
#this is a dicitonary inside of a list

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa',
                'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham',
                'Patrick', 'Minh', 'Devon']
}

print("\n")
#create a function printInfo(some_dict)
def printInfo(some_dict):
#print the length of each key
        for key, value in some_dict.items():
#print the key name
            print(len(value), " " + key.upper())
#print the values of each key
            for element in value:
                print("\n", element)
            print("===================================")
printInfo(dojo)