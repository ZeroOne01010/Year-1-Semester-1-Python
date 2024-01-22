pos = []
neg = []

for i in range(0, 10):
    user_input = int(input("Please enter 10 different numbers either positive or negative"))
        
    if user_input>= 0:
        pos.append(user_input)
    else:
        neg.append(user_input)

sum_pos = sum(pos)
sum_neg = sum(neg)
print(f'The total of all the positive numbers {sum_pos}, the total of all the negative numbers is {sum_neg}')
