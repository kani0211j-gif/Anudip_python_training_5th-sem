# Sample Data
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# To Display products with stock less than 10
print("--- Products with stock less than 10 ---")
for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

# To Count products having stock more than 50
count_above_50 = 0
for stock in inventory.values():
    if stock > 50:
        count_above_50 += 1
print("\nProducts with stock > 50:", count_above_50)

# To Find the product with the minimum stock
min_product = ""
min_stock = 999999  # Start with a large number to compare
for product, stock in inventory.items():
    if stock < min_stock:
        min_stock = stock
        min_product = product
print("\nProduct with minimum stock:", min_product, "(Stock:", min_stock, ")")

# To Create a list of products that require restocking (stock < 20)
restock_list = []
for product, stock in inventory.items():
    if stock < 20:
        restock_list.append(product)
print("\nProducts requiring restock:", restock_list)

# To Calculate the total inventory count
total_items = 0
for stock in inventory.values():
    total_items += stock
print("\nTotal items in inventory:", total_items)

