def generate_checkerboard(x, y):
    result = [] #result is a list of lists

    # create first for loop for column followed by 
    # second loop for the rows ( 2 for loops)
    for j in range(0, y):
        temp = []
    #creating a temporary array to add the array we made 
        for i in range(0, x):
            temp.append((i + j) % 2)
        '''This will bring our array to look like 
        [0,1,0]
        [1,0,1]
        '''
        result.append(temp) # this is used only to visually 
        #see the board in the terminal

    return result
