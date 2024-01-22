#Programme to add up all items on a shopping list and provide a total 

peaches_num = int(input("How many cans of peaches ?"))
peaches_cost = float(input("How much did the can(s) of peaches cost: ?"))
beans_num = int(input("How many cans of beans ?"))
beans_cost = float(input("How much did the can(s) of beans cost: ?"))
chicken_num = int(input("How many chicken pieces ?"))
chicken_cost = float(input("How much did chicken cost: ?"))
socks_num = int(input("How many socks ?"))
socks_cost = float(input("How much did the socks cost: ?"))
water_num = int(input("How many bottles of water ?"))
water_cost = float(input("How much did the bottles of water cost: ?"))

total_number = (peaches_num + beans_num + chicken_num + socks_num + water_num)
total_cost = (peaches_num * peaches_cost + beans_num * beans_cost + chicken_num * chicken_cost + socks_num * socks_cost + water_num * water_cost)

print(
    f"The total number of items bought: {total_number} \nThe total of your weekly shop is: £{total_cost}"
)