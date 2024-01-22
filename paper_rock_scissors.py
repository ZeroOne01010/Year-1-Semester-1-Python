import random

computer_points = 0
user_points = 0

computer = ['scissors', 'rock', 'paper']

while computer_points < 3  and user_points < 3:
    computer_choice = random.choice(computer)
    user_choice = (input('Welcome to rock, paper, scissors, please make your choice: ')).lower()
    
    if user_choice not in ['scissors', 'rock', 'paper']:
        print('Please only enter rock, paper or scissors: ')
        continue
        
    
    print(f'computer chose {computer_choice} & you chose {user_choice}')
    
    if user_choice == computer_choice:
        print('a draw, no points awarded')
        
    elif user_choice == 'scissors' and computer_choice == 'rock':
        computer_points += 1
        print('You chose scissors and the computer chose rock.\nComputer wins this round')
        
    elif user_choice == 'scissors' and computer_choice == 'paper':
        user_points += 1
        print('You chose scissors and the computer chose paper.\nYou wins this round')
        
    elif user_choice == 'rock' and computer_choice == 'scissors':
        user_points += 1
        print('You chose rock and the computer chose scissors.\nYou wins this round')
        
    elif user_choice == 'rock' and computer_choice == 'paper':
        computer_points += 1
        print('You chose rock and the computer chose paper.\nComputer wins this round')
        
    elif user_choice == 'paper' and computer_choice == 'rock':
        user_points += 1
        print('You chose paper and the computer chose rock.\nYou wins this round')
        
    elif user_choice == 'paper' and computer_choice == 'scissors':
        computer_points += 1
        print('You chose paper and the computer chose scissors.\nComputer wins this round')
        
    print(f'Computer has {computer_points} and user has {user_points}\nThe computer needs {3 - computer_points} to win and you need {3 - user_points} to win\n====================================')
    
if user_points >= 3:
    print('Congratulations, you beat the computer!')
else:
    print('Boo, the computer wins!')

