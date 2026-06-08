'''
----------------------------------------------------
Problem Statement: E-Commerce Product Sales Analysis

sales = {
 "Laptop": 15,
 "Mouse": 45,
 "Keyboard": 32,
 "Monitor": 12,
 "Headphones": 28,
 "Printer": 8,
 "Webcam": 20,
 "Speaker": 18,
 "Tablet": 10,
 "Router": 25
}

Tasks
1. Display products sold more than 20 times.
2. Find the best-selling product.
3. Find the least-selling product.
4. Calculate total products sold.
5. Create a list of products requiring promotion (sales < 15).
6. Count products having sales between 10 and 30.
----------------------------------------------------
'''

# creating a dictionary to store product sales data
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

#--------------------------------------------------
# to display products sold more than 20 times
print("Products Sold More Than 20 Times :")

for product in sales:
    if sales[product] > 20:
        print(product)

#--------------------------------------------------
# to find the best-selling product

dict_items = list(sales.items())

best_product = dict_items[0][0]
best_sales = dict_items[0][1]

for item in dict_items:
    if item[1] > best_sales:
        best_product = item[0]
        best_sales = item[1]

print("Best Selling Product :", best_product, "(", best_sales, ")")

#--------------------------------------------------
# to find the least-selling product

least_product = dict_items[0][0]
least_sales = dict_items[0][1]

for item in dict_items:
    if item[1] < least_sales:
        least_product = item[0]
        least_sales = item[1]

print("Least Selling Product :", least_product, "(", least_sales, ")")

#--------------------------------------------------
# to calculate total products sold

total_sales = 0

for value in sales.values():
    total_sales = total_sales + value

print("Total Units Sold :", total_sales)

#--------------------------------------------------
# to create a list of products requiring promotion

promotion_products = []

for product in sales:
    if sales[product] < 15:
        promotion_products.append(product)

print("Products Requiring Promotion :")
print(promotion_products)

#--------------------------------------------------
# to count products having sales between 10 and 30

count = 0

for value in sales.values():
    if value >= 10 and value <= 30:
        count = count + 1

print("Products Having Sales Between 10 and 30 :", count)

#--------------------------------------------------
#output will be
'''
Products Sold More Than 20 Times :
Mouse
Keyboard
Headphones
Router
Best Selling Product : Mouse ( 45 )
Least Selling Product : Printer ( 8 )
Total Units Sold : 213
Products Requiring Promotion :
['Monitor', 'Printer', 'Tablet']
Products Having Sales Between 10 and 30 : 7
'''
