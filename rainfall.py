def create_histogram():
    months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    # user input stored for each month 
    rainfall_data = [int(input(f"Enter the amount of rainfall for {month} (in mm): ")) for month in months]

    max_rainfall = max(rainfall_data)

    # nested for loop to plot the histogram 
    for i in range(max_rainfall, 0, -1):
        for j in range(len(months)):
            print('X' if rainfall_data[j] >= i else ' ', end='    ')
        print()
    # for loop to print each month aligned to each month 
    for month in months:
        print(month[:3], end='  ')


create_histogram()
