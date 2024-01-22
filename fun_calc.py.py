# Program to calculate user input

# Calculation function
def calculation(choice_1, choice_2, choice_sign):
    if choice_sign == '1':
        return choice_1 + choice_2
    elif choice_sign == '2':
        return choice_1 - choice_2
    elif choice_sign == '4':
        if choice_2 == 0:
            raise ValueError("Cannot divide by zero.")
        return choice_1 / choice_2
    elif choice_sign == '3':
        return choice_1 * choice_2
    elif choice_sign == '5':
        return choice_1 % choice_2
    else:
        raise ValueError("Invalid operator. Please enter a number 1 - 5")

# Read user input and perform calculation
try:
    choice_1 = int(input('Please enter the first number: '))
    choice_2 = int(input('Please enter the second number: '))
    choice_sign = input('1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Remainder\n: ')
    result = calculation(choice_1, choice_2, choice_sign)
    print(f'The result is {int(result)}')

except ValueError as e:
    print(f'Error: {e}')
    print('Invalid input, please try again')
