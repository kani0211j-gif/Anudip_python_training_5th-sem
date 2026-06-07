prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

cheap_items_count = 0
expensive_item = ""
highest_price = 0
total_shop_value = 0

premium_items = []
budget_range_items = []

# single loop to scan all pricing requirements
for item, price in prices.items():
    # 1. total shop valuation
    total_shop_value += price
    
    # 2. check premium items (> 5000)
    if price > 5000:
        premium_items.append(f"{item} : {price}")
        
    # 3. count items costing less than 3000
    if price < 3000:
        cheap_items_count += 1
        
    # 4. find most expensive item
    if price > highest_price:
        highest_price = price
        expensive_item = item
        
    # 5. filter budget range (2000 to 10000)
    if price >= 2000 and price <= 10000:
        budget_range_items.append(item)

print("--- Items above 5000 ---")
for prod in premium_items:
    print(prod)

print("\nItems under 3000:", cheap_items_count)
print(f"Most expensive item: {expensive_item} costing {highest_price}")
print("Items between 2000 and 10000:", budget_range_items)
print("Total shop value:", total_shop_value)

