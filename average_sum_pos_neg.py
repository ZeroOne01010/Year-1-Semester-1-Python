pos = []
neg = []

# code to take user input and store it in related dictionary wether it is positive or negative 
for i in range(0, 10):
    user_input = int(input("Please enter 10 different numbers either positive or negative: "))
        
    if user_input>= 0:
        pos.append(user_input)
    else:
        neg.append(user_input)

# sum negs and pos 
sum_pos = sum(pos)
sum_neg = sum(neg)

#statment to output if no negs or pos was inputted 
if pos == []:
    print('no positive numbers were entered!')
elif neg == []:
    print('no negative numbers were entered!')



print(f'The total of all the positive numbers is {sum_pos}, the total of all the negative numbers is {sum_neg}')

avg_pos = sum_pos // len(pos) if pos else 0
avg_neg = sum_neg // len(neg) if neg else 0

print(f'The average of all the positive numbers is {avg_pos} & the average of all the negatice numbers is {avg_neg}')

