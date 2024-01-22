#program to calculate maximum bandwidth 

Max_bandwidth = 1000 * 1000000
users = 200
application_A = 200000
application_B = 100000
new_application = 350000
current_usage = users * (application_A + application_B)
remaining = Max_bandwidth - current_usage
new_app_req = users * new_application
bandwidth_available = (Max_bandwidth - (current_usage + new_app_req)) // 1000000


print(
    f'The network capacity is: {Max_bandwidth} bps\nThe current usage is: {current_usage} bps\nThe current availability is : {remaining} bps\nThe new applications requirements are: {new_app_req} bps\nThe bandwidth available if the new application is installed will be: {bandwidth_available} Mbps  '
)

