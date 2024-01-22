#Program to calculate cost of tickets 

#ticket prices
ADULT_PRICE = 10.50
CHILD_PRICE = 7.30
CONCESSION_PRICES = 8.40

#user to input total tickets required and enter str yes or no for pick up at venue or delivery required 
adult_tickets = int(input('Please enter the amount of adults'))
child_tickets =  int(input('Please enter the amount of child tickets'))
concessions_tickets = int(input('Please enter the amount of concession tickets'))  
pickup_tickets = str(input('Tickets collected from venue ? yes or no ? (delivery is charged at £2.34)')).lower()

#calculate free adult ticket for every 10 child tickets bought and additional if statment to ensure at least 1 adult or concession remians
if child_tickets > 10:
    adult_tickets -= min(child_tickets // 10, adult_tickets)
    if concessions_tickets == 0 and adult_tickets == 0:
        adult_tickets + 1

#total cost of tickets for each type of person
total_adult = max(adult_tickets, 0) * ADULT_PRICE
total_child = child_tickets * CHILD_PRICE
total_concession = concessions_tickets * CONCESSION_PRICES

total_price = total_adult + total_child + total_concession

#10% discount applied for total cost over £100
if total_price > 100:
    total_price = total_price * 0.9
    print('A 10 percent discount has being appled')

#calculate wether or not delivery applied and variable to print on statment if charge applied or not 
if pickup_tickets == 'no':
    total_price = total_price + 2.34
    delivery_applied = 'yes'
else:
    delivery_applied = 'no'

#print a reciept
print(
    f'Adult tickets {adult_tickets}\nChild tickets {child_tickets}\nConcession tickets {concessions_tickets}\nDelivery charged applied? {delivery_applied}\n=============================\nThe total price for your tickets is £{total_price:.2f}'
    )




