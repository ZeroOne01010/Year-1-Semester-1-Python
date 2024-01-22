#program to take integer as the width of a diamond and return the full diamond of * 

#this section ensures only positive numbers between 2 and 40 are entered
user_input = int(input('Please enter a number between 2 and 40: '))
if user_input < 2:
    print('Please try again, enter a value between 2 and 40 ')
elif user_input > 40:
    print('Please try again, enter a value between 2 and 40 ')
else:
    
    stored = user_input
    base = user_input
#multiplies an empty space by the user input to ensure correct spacing and have 1 * as the top of the diamond, the loop iterates removing 1 space and adding one * each time until the stored variable is equal to the base variable which was the same as the users initial input
    for i in range(stored):
        print(' ' * user_input + "* " * (i + 1))
        user_input -= 1
#this code reverses the above process forming the lower half of the diamond
    if stored == base:
        user_input += 1 #makes sure we start with a spacing of one to align the two halves
        for i in range(stored - 1, 0, -1):
            print(' ' * user_input + " *" * i)
            user_input += 1