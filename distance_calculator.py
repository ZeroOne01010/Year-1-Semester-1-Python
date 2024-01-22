#program that calculates the distance travelled by an object moving with constant acceleration.

initial_velocity = float(input("Please enter the initial velocity: "))
time_taken = float(input("Please enter the total time taken: "))
acceleration = float(input("Please enter the rate of acceleration: "))

distance = initial_velocity * time_taken + acceleration * time_taken**2 * 0.5

print(
    f"The total distance covered is {distance} meters "
    )