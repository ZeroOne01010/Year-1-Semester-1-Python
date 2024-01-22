def select_dish(options, prompt):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return int(input("Please select: "))

print("Main dishes are:")
main_dishes = ["Lasagne", "Stir Fry"]
main_dish = select_dish(main_dishes, "Please select dish:")

if main_dish == 1:
    print("Side dishes are:")
    side_dishes = ["Garlic bread", "Fries"]
    side_dish = select_dish(side_dishes, "Please select side dish:")
    if side_dish == 1:
        print("You have selected Lasagne with garlic bread")
    elif side_dish == 2:
        print("You have selected Lasagne with fries")
    else:
        print("Invalid item selected")
        
if main_dish == 2:
    print("Side dishes are:")
    side_dishes = ["Noodles", "Crispy Seaweed"]
    side_dish = select_dish(side_dishes, "Please select side dish:")
    if side_dish == 1:
        print("You have selected Stir fry with Noodles")
    elif side_dish == 2:
        print("You have selected Stir fry with Crispy Seaweed")
    else:
        print("Invalid item selected")
        

