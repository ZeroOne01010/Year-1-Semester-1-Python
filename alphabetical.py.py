#programme alphabetical sorting 

empty_list = []

for words in range(5):
    word = input('Please enter 5 differnt words: ')
    empty_list.append(word)

empty_list.sort()
print(f'Here are your words in alphabetical order: {empty_list}')
