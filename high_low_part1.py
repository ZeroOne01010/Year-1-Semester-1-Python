import random
#program to deal a random card from a deck of cards 
first_card = random.randint(1,13)
if first_card == 1:
    print('The first card is an ACE')
elif first_card == 11:
    print('The first card is a Jack')
elif first_card == 12:
    print('The first card is a Queen')
elif first_card == 13:
    print('The first card is a King')
else: 
    first_card > 1 and first_card < 10
    print(
    f'The first card is a {first_card}'
    )