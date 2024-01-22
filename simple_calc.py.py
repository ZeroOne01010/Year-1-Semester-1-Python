# Program to calculate user input

# Read user input
try:
    choice_1 = int(input('Please enter the first number: '))
    choice_2 = int(input('Please enter the second number: '))
    choice_sign = input('Please enter your chosen sign (+, -, /, or *): ')

    # Calculation
    if choice_sign == '+':
        result = choice_1 + choice_2
    elif choice_sign == '-':
        result = choice_1 - choice_2
    elif choice_sign == '/':
        if choice_2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = choice_1 / choice_2
    elif choice_sign == '*':
        result = choice_1 * choice_2
    else:
        raise ValueError("Invalid operator. Please enter +, -, /, or *.")

except ValueError as e:
    print(f'Error: {e}')
    print('Invalid input, please try again')

else:
    print(f'Your sum is {choice_1} {choice_sign} {choice_2} and the result is {int(result)}')

