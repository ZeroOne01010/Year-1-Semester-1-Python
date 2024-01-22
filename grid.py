rows = []
height = []

rows = int(input("Please provide the width of the grid: "))
height = int(input("Please provide the height of the grid: "))

for r in range(rows):
    for h in range(height):
        print('*',end = ' ')
    print()
