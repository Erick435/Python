from random import randint
from unittest import result

def roll_dice(number = 1, sides = 20):
#this already DEFAULTS the numbers of dice and sides ^^^^
    result = 0

    for i in range(0, number):
        result += randint(1, sides)

    return result


print(roll_dice(2, 20))
# rolling 2 dices (20 sided dice each)

#if i just call the function, it will send the default which is 1, 20
print(roll_dice())

#when just stating which parameter, the other parameter will be default
print(roll_dice(number = 3))


def generate_new_character():
    #rolles six sets of 3d6 dice and supplies them as stats
    #in dictionary format

    character = {}

    character ['STR'] = roll_dice(3, 6)
    character ['DEX'] = roll_dice(3, 6)
    character ['CON'] = roll_dice(3, 6)
    character ['WIS'] = roll_dice(3, 6)
    character ['INT'] = roll_dice(3, 6)
    character ['CHA'] = roll_dice(3, 6)

    return character

new_character = generate_new_character()
print("\n\n\nGENERATING CHARACTER... ERICK THE DRAGON SLAYER")
print(new_character, "\n\n")


def generate_new_character2():
    character = {}
    stats = ['STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']

    for attribute in stats:
        character[attribute] = roll_dice(3, 6)

    return character
new_character = generate_new_character2()
print("\n\n\nGENERATING CHARACTER... ERICK THE DRAGON SLAYER")
print(new_character, "\n\n")

def generate_new_character3():
    character = {
        'STR': roll_dice(3, 6), 
        'DEX': roll_dice(3, 6),
        'CON': roll_dice(3, 6),
        'WIS': roll_dice(3, 6),
        'INT': roll_dice(3, 6),
        'CHA': roll_dice(3, 6)
    }

    return character
new_character = generate_new_character3()
print("\n\n\nGENERATING CHARACTER... ERICK THE DRAGON SLAYER")
print(new_character, "\n\n")