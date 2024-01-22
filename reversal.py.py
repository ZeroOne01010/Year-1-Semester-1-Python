while True:
    #this block of code is input validation ensuring only integers are entered and returns an error code otherwise 
    try:
        inputs = (input('Please enter a range of digits, minimum of 2, maximum of 11 or -1 to quit: '))
        num = int(inputs)
    except ValueError:
        print('Input is not valid')
        
    #this code allows the user to exit the programme 
    if inputs == '-1':
        print('End of programme')
        break

    sign = 1
    reversed_num = 0
    
    #this code handles any negative numbers ensuring num is returned as an absolute number but the sign is stored and reapplied after the number has being reversed 
    if num < 0:
        sign = -1
        num = abs(num)
    
    # while the number above 0 this while loop iterates all the digits form the input. 
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    reversed_num *= sign #adds the negative sign back in if required 
    
    if len(str(reversed_num)) == 1:
        print('You need to enter at least 2 digits')
    elif len(str(reversed_num)) >= 12:
        print('Please enter no more than 11 digits')
    else:
        print(f'Reversed integer is {reversed_num}')

    
    
        


