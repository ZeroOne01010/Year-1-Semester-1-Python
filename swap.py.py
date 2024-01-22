# Program to return 2 inputs in reverse order

def swap(a, b):
    return b, a

def print_int_list():
    a = input('Please enter your first character: ')
    b = input('Please enter your second character: ')
    result = swap(a, b)
    print(f'{result[0]}, {result[1]}')

print_int_list()
