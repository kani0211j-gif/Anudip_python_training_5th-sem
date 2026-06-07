#online store record orders
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
print("--- 1. E-Commerce Order Analysis ---")

# 1. Display all products costing more than 1000
print("Products costing more than 1000:")
for item in orders:
    name = item[0]
    price = item[1]
    if price > 1000:
        print( name, ":", price)
        
  # 2. Find the most expensive product
expensive_product = orders[0]
for item in orders:
    if item[1] > expensive_product[1]:
        expensive_product = item
print("\nMost expensive product:", expensive_product[0], "Price:", expensive_product[1]) 
 
 # 3. Calculate the total order value
total_order_value = 0
for item in orders:
    total_order_value = total_order_value + item[1]
print("Total order value:", total_order_value)

# 4. Count products costing below 1000
cheap_products_count = 0
for item in orders:
    if item[1] < 1000:
        cheap_products_count = cheap_products_count + 1
print("Count of products below 1000:", cheap_products_count)
print("\n")   
