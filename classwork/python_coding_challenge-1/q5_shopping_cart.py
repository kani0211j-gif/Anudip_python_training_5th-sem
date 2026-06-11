''': Online Shopping Cart Analyz
Problem Statement
The prices of products added to a shopping cart are stored below.
Sample Data
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
Tasks
1. Calculate the total cart value.
2. Find the most expensive and cheapest products.
3. Count products eligible for premium shipping (price > ₹1000).
4. Generate a discount list (products above ₹1500).
5. Calculate the average product price. '''
#--------------------------------------------------------
# to create a list 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
#initialize the total
total = 0
#------------------------------------
#to compare the values initialising the values
highest = cart[0]
lowest = cart[0]

premium = 0

discount_list = []
#--------------------------single (for loop) -----------------------
for price in cart:
     # to calculate total
    total += price
#--------------------------------------------------------------
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price
#---------------------------------------------------------------
#to display premium product
    if price > 1000:
        premium += 1
#----------------------------------------------------------------
#to display discount list
    if price > 1500:
        discount_list.append(price)
#----------------------------------------------------------
#to calculate average
average = total / len(cart)
#---------------------------------------------------------------
#to display output and values
print("Total Cart Value :", total)
print("Most Expensive Product :", highest)
print("Cheapest Product :", lowest)
print("Premium Shipping Eligible Products :", premium)
print("Discount Eligible Products :", discount_list)
print("Average Product Price :", average)
#---------------------------------------------------------------------------------------
#output will be
'''Total Cart Value : 11097
Most Expensive Product : 2500
Cheapest Product : 300
Premium Shipping Eligible Products : 4
Discount Eligible Products : [2500, 1800]
Average Product Price : 1109.7'''