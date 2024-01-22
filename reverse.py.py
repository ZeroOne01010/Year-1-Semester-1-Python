rev_list = [] #empty list 

try:#input validation
    for _ in range(1, 6):
        user_input = int(input("Enter an integer: ")) 
        rev_list.insert(0, user_input) #this code inserts the input at the the beginning of the array, reversing the user input 
        
    print(f'Reverse list: {rev_list}')
        
except ValueError:
        print("Invalid input. Please enter a valid integer.")


        
        
