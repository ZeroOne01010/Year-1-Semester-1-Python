


rainbow = {1:'red', 2:'orange', 3:'yellow', 4:'green', 5:'blue', 6:'indigo', 7:'violet'}

while True:
        choice = input('Please enter a number between 1 and 7 to display a rainbow colour or -1 to quit: ')
        num = int(choice)
        
        if num in rainbow:
            colour = rainbow[num]
            print(f'The colour for {num} is {colour}')
            
        elif num == -1:
            print('end of programme')
            break
        
        else:
            print('Not a valid choice')
        

