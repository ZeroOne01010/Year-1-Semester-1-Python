
def print_grid(grid):
    print("  1 2 3 4")
    for i, row in enumerate(grid):
        print(f"{i+1} {' '.join(row)}")

def get_user_choice(prompt):
    while True:
        print(prompt, end='')
        x, y = int(input('> ')), int(input('> '))
        if display_grid[x-1][y-1] != 'X':
            return x-1, y-1
        print("Not a correct choice, please try again.")

#counters for guesses and number of pairs found
number_of_guesses = 0
number_of_pairs_found = 0

#array grid for card locations
card_grid = [["J", "J", "J", "J"],
             ["Q", "Q", "Q", "Q"],
             ["K", "K", "K", "K"],
             ["A", "A", "A", "A"]]
display_grid = [['*' for _ in range(4)] for _ in range(4)]

#prints out the display grid 
print_grid(display_grid)

# while not all pairs have been found while loop 
while number_of_pairs_found < 8:
    number_of_guesses += 1

    x1, y1 = get_user_choice("Enter co-ordinates of your first choice (x, y): ")
    display_grid[x1][y1] = card_grid[x1][y1]
    print_grid(display_grid)

    x2, y2 = get_user_choice("Enter co-ordinates of your second choice (x, y): ")
    display_grid[x2][y2] = card_grid[x2][y2]
    print_grid(display_grid)

    if card_grid[x1][y1] == card_grid[x2][y2]:
        display_grid[x1][y1] = 'X'
        display_grid[x2][y2] = 'X'
        number_of_pairs_found += 1
        print(f"Congratulations, you have now found {number_of_pairs_found} pairs")
    else:
        display_grid[x1][y1] = '*'
        display_grid[x2][y2] = '*'
        print("Hard luck! Try again")

    print_grid(display_grid)

print(f"You took {number_of_guesses} guesses to find all the pairs")
