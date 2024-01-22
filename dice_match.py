import random 
dice_a = random.randint(1, 6)
dice_b = random.randint(1 ,6)

while dice_a is not dice_b:
    dice_a = random.randint(1, 6)
    dice_b = random.randint(1, 6)
    print(f'no match {dice_a} is not equal to {dice_b}')

else:
    print(f'Its a match {dice_a} & {dice_b}')
