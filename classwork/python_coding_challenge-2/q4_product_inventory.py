'''Problem Statement
An online store maintains stock quantities of products.
Sample Data
inventory = {
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
1. Display products with stock below 15 units.
2. Find the product with maximum stock.
3. Find the product with minimum stock.
4. Calculate total stock available.
5. Create a list of products requiring restocking (<10 units).
Sample Output
Products with Stock Below 15:
Monitor
Printer
Tablet
Highest Stock Product:
Mouse (45 units)
Lowest Stock Product:
Printer (8 units)
Total Stock Available: 213
Products Requiring Restocking:
[Monitor, Printer, Tablet] '''
#-----------------------------------------------------------------------------
inventory = {
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
#to display products with stock below 15 units
#------------------------------------------------------------------------------
print("products with stock below 15 units: ")
for product, stock in inventory.items():
    if stock < 15:
        print(product)
#-------------------------------------------------------------------------------
# to find the product with maximum stock 
dict_items = list(inventory.items())
max_stock_product = dict_items[0][0]
max_stock = dict_items[0][1]
for item in dict_items:
    if item[1] > max_stock:
        max_stock_product = item[0]
        max_stock = item[1]
print("product with maximum stock: ",max_stock_product,"(",max_stock,"units)")
#--------------------------------------------------------------------------------
# to find the product with minimum stock
min_stock_product = dict_items[0][0]
min_stock = dict_items[0][1]
for item in dict_items:
    if item[1] < min_stock:
        min_stock_product = item[0]
        min_stock = item[1]
print("product with minimum stock : ",min_stock_product,"(",min_stock,"units)")
#--------------------------------------------------------------------------------
#to calculate total stock available 
total_stock = 0
for stock in inventory.values():
    total_stock += stock
print("total stock available : ",total_stock)
#--------------------------------------------------------------------------------
# to create a list of products requiring restocking (<10 units)
restock_products = []
for product, stock in inventory.items():
    if stock < 10:
       restock_products.append(product)
print("products requiring restocking: ",restock_products)
#-------------------------------------------------------------------------------
#output will be 
'''products with stock below 15 units: 
Monitor
Printer
Tablet
product with maximum stock:  Mouse ( 45 units)
product with minimum stock :  Printer ( 8 units)
total stock available :  213
products requiring restocking:  ['Printer']'''
