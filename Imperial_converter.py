#Program to calculate imperial to metric height 

feet = int(input('Please enter the amount of feet: '))
inches = int(input('Please enter the amount of inches: '))

millimeters = feet * 304.8 + inches * 25.4
centimeters = millimeters / 10
meters = centimeters / 100
kilometers = meters / 1000

print(
    f'Height in kilometers: {kilometers}\nHeight in meters: {meters}\nHeight in centimeters:" {centimeters}\nHeight in millimeters: {millimeters}'
)