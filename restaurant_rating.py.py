integers = []


def count_occurrences():#function to store how many times each number occurs, stored in a dict
    occurrences = {}

    for num in integers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    return occurrences


while True:
    try:
        inputs = int(input('Welcome to the voting platform\nPlease enter all votes, once all votes have been entered, enter -1 to return your results.\nEnter numbers between 1 and 5: '))

        if inputs == 0 or inputs > 5:
            print('Invalid input')

        elif 0 < inputs <= 5:
            integers.append(inputs)

        elif inputs == -1:
            print('End of the program')
            break

    except ValueError as error_variable:
        print(f'Error: {error_variable}')

# Call the count_occurrences function after user input is done
result = count_occurrences()
total_sum = 0
total_count = 0

for num in sorted(result.keys()):
    print(f"{num}: {result[num]} times")
    total_sum += num * result[num]
    total_count += result[num]

try:
    average_rating = total_sum / total_count
    print(f'The average rating is {int(average_rating)}')
except ZeroDivisionError as e:
    print(f'Error: Unable to divide by 0 - {e}')

