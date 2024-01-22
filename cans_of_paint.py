# program to calculate how many tins of paint are required and how many tins per box and how many boxes full of paint are needed to complete the job

import math

paint_pot = 5.1

length = 40
width = 30
height = 3.4

area_length = length * height * 2
area_width = width * height * 2
total_area = area_width + area_length

Amount_of_paint = total_area / paint_pot

print("The total number of tins required is " + (str(math.ceil(Amount_of_paint))))

box_length = 60
box_width = 35
box_height = 30

Diameter_paint = 15
box_capacity = math.floor((box_length / Diameter_paint) * math.floor(box_width / Diameter_paint))

print("In each box there will be " + (str(math.floor(box_capacity))) + (" tins of paint"))
print("A total of " + (str(math.floor(Amount_of_paint / box_capacity))) + " boxes will be required to complete the job")
print("There will be " + (str(math.ceil(Amount_of_paint % box_capacity))) + " tins left over not in boxes")
