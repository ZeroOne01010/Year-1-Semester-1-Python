integers = []

while True:
    try:
        inputs = int(input('Please enter a number between 1 and 11: '))

        if inputs == 0 or inputs > 11:
            print('invalid input')
        
        elif inputs > 0 and inputs < 12:
            integers.append(inputs)

        else: 
            inputs < 0
            
            print('end of the program')
            integers.reverse()
            print(integers)
            break
        
    except ValueError as error_variable:
        print(f'Error: {error_variable}')
        

        




 


