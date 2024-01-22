shopping_list = []

for i in range(5):
    item = input('Please enter the name of the item: ')
    price = float(input('Please enter the price of the item: '))
    shopping_list.append((item, price))

shopping_list = sorted(shopping_list, key=lambda x: x[1], reverse = True)
print('Here is your shopping list:')
for item, price in shopping_list:
    print(f'{item}: £{price:.2f}')
