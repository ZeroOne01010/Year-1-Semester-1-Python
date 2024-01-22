# Program to take user input and format it into an address 

surname = str(input("Please enter your Surname: "))
house_number = int(input("Please enter your house number: "))
road = str(input("Please enter the road you live on: "))
town = str(input("Please enter the town you live in:" ))

print(
    f"""Mr & Mrs {surname},
{house_number}, {road}
{town}"""
)