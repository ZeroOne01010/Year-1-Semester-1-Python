#program to calculate a range of positive and negative numbers and sum the positive numers and print out and sum negative numbers and print out 

positive_num = []
negative_num = []

for i in range(5):
    user_input = int(input('Please enter 5 numbers either negitive or positive numbers'))

    if user_input > 0:
        positive_num.append(user_input)
    elif user_input < 0:
        negative_num.append(user_input)
    else:
        print('0 is not a positive or negative, please try again')
        break

    total_pos = sum(positive_num)
    total_neg = sum(negative_num)
                                
   
print(
    f'Positive number total is {total_pos}\nNegative number total is {total_neg}'
)

