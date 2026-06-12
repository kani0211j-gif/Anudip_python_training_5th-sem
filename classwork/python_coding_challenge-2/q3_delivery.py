''' Food Delivery Performance Dashboard
Problem Statement
Delivery times (in minutes) for different orders are recorded below:
Sample Data
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
Tasks
1. Find the fastest delivery time.
2. Find the slowest delivery time.
3. Calculate the average delivery time.
4. Display delayed orders (>45 minutes).
5. Categorize deliveries:
o Fast (≤30 minutes)
o Normal (31–45 minutes)
o Delayed (>45 minutes)
Sample Output
Fastest Delivery: 18 minutes
Slowest Delivery: 80 minutes
Average Delivery Time: 40.8 minutes
Delayed Orders:
[60, 80, 55]
Fast Deliveries: 4
Normal Deliveries: 3
Delayed Deliveries: 3'''
#------------------------------------------------------------------------------
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
#to find the fastest delivery time 
fastest_delivery = 0
for time in delivery_times:
    if time > fastest_delivery:
        fastest_delivery = time
print("fastest delivery time: ",fastest_delivery)
#--------------------------------------------------------------------------------
# to find the slowest delivery time 
slowest_delivery = delivery_times[0]
for time in delivery_times:
    if time < slowest_delivery:
        slowest_delivery = time
print("slowest delivery time: ",slowest_delivery)
#--------------------------------------------------------------------------------
# to calculate the average delivery time 
total_time = 0 
for time in delivery_times:
    total_time += time
average_time = total_time / len(delivery_times)
print("average delivery time: ",average_time)
#--------------------------------------------------------------------------------
#to display delayed orders (>45 minutes)
delayed_orders = []
for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)
print("delayed orders: ",delayed_orders)
#-------------------------------------------------------------------------------
#to categorize deliveries
fast_deliveries = 0 
norma_deliveries = 0 
delayed_deliveries = 0 
for time in delivery_times:
    if time <= 30:
        fast_deliveries += 1
    elif time > 30 and time <= 45:
        norma_deliveries += 1
    else:
        delayed_deliveries += 1
print("fast deliveries: : ",fast_deliveries)
print("normal deliveries: ",norma_deliveries)
print("delayed deliveries: : ",delayed_deliveries)
#-----------------------------------------------------------------------------
#output will be 
'''fastest delivery time:  80
slowest delivery time:  18
average delivery time:  40.8
delayed orders:  [60, 80, 55]
fast deliveries: :  4
normal deliveries:  3
delayed deliveries: :  3'''