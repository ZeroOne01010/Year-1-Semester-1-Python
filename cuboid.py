#Programme to calculate volume and surface area of a cuboid
width = int(input(("Please enter the width of the cuboid: ")))
length = int(input(("Please enter the length of the cuboid: ")))
height = int(input(("Please enter the height of the cuboid: ")))

volume = width * length * height
surface_area = (length * width * 2) + (length * height * 2) + (height * width * 2)

print(
    
    f"The Volume is {volume}, and the surface area is {surface_area} "
)