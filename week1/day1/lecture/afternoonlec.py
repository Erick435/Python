# sample functions
# accept a list of integers as its unput
# output a new list consisting of only positive integers

#we use "def" instead of function like in javascript to 
# define a function

input_list = [1, 3, 0, -6, -7, 20]

def sample_function_name(input_list):
    # everything inside the function is indented one layer
    output_list = []

    for items in input_list:
        if items >= 0:
            output_list.append(items)

    return output_list

print("This is not in the function")
