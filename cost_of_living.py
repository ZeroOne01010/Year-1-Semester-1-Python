#programme to prompt user for input of bills and then format into a table 

rent = float(input("Please enter your monthly rent: "))
gas = float(input("Please enter monthly gas payments: "))
elec = float(input("Please enter monthly electricity payments: "))
water = float(input("Please enter monthly payments for water rates: "))
council_tax = float(input("Please enter monthly council tax payments: "))

total = rent + gas + elec + water + council_tax

print(f"Rent:{'£':>17} {rent:.2f}\nGas:{'£':>18} {gas:.2f}\nElectricity:{'£':>10} {elec:.2f}\nWater:{'£':>16} {water:.2f}\nCouncil tax:{'£':>10} {council_tax:.2f}"
)
print("=".center(27, "="))
print(
    f"Total outgoings are: £{total:.2f}"
    )
print("=".center(27, "="))
