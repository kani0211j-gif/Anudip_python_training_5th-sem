''' E-Commerce Inventory & Sales Dashboard
Problem Statement
An online store wants to manage products and sales.
Example Structure
products = {
 "P101": {
 "name": "Laptop",
 "price": 55000,
 "stock": 12,
 "sold": 25
 }
}
Maintain records of at least 30 products.
Requirements
1. Display all products.
2. Add a new product.
3. Update stock after sales.
4. Find out-of-stock products.
5. Find products with stock less than 5.
6. Calculate total inventory value.
7. Find best-selling product.
8. Find least-selling product.
9. Calculate total revenue generated.
10. Generate a low-stock report.
11. Display products whose sales exceed the average sales.
12. Create a dictionary of products eligible for promotion (sales < 10).
Challenge
Generate a complete business report'''
#------------------------------------------------------------
#its a menu driven program
products = {
 "P101": { "name": "Laptop", "price": 55000,"stock": 12,"sold": 25},
    "P102": { "name": "Smartphone", "price": 20000,"stock": 30,"sold": 50},
    "P103": { "name": "Tablet", "price": 15000,"stock": 8,"sold": 15},
    "P104": { "name": "Headphones", "price": 5000,"stock": 20,"sold": 40},
    "P105": { "name": "Smartwatch", "price": 10000,"stock": 5,"sold": 10},
    "P106": { "name": "Camera", "price": 25000,"stock": 10,"sold": 20},
    "P107": { "name": "Printer", "price": 8000,"stock": 15,"sold": 30},
    "P108": { "name": "Monitor", "price": 12000,"stock": 7,"sold": 18},
    "P109": { "name": "Keyboard", "price": 2000,"stock": 25,"sold": 60},
    "P110": { "name": "Mouse", "price": 1500,"stock": 30,"sold": 70},
    "P111": { "name": "External Hard Drive", "price": 6000,"stock": 12,"sold": 22},
    "P112": { "name": "USB Flash Drive", "price": 1000,"stock": 50,"sold": 100},
    "P113": { "name": "Router", "price": 4000,"stock": 18,"sold": 35},
    "P114": { "name": "Speakers", "price": 3000,"stock": 10,"sold": 25},
    "P115": { "name": "Microphone", "price": 3500,"stock": 8,"sold": 15},
    "P116": { "name": "Webcam", "price": 4500,"stock": 5,"sold": 12},
    "P117": { "name": "Projector", "price": 20000,"stock": 3,"sold": 8},
    "P118": { "name": "Gaming Console", "price": 30000,"stock": 6,"sold": 18},
    "P119": { "name": "VR Headset", "price": 35000,"stock": 4,"sold": 10},
    "P120": { "name": "Smart Home Hub", "price": 8000,"stock": 20,"sold": 40},
    "P121": { "name": "Fitness Tracker", "price": 5000,"stock": 15,"sold": 30},
    "P122": { "name": "E-Reader", "price": 12000,"stock": 10,"sold": 25},
    "P123": { "name": "Portable Charger", "price": 2500,"stock": 30,"sold": 60},
    "P124": { "name": "Bluetooth Adapter", "price": 1500,"stock": 20,"sold": 45},
    "P125": { "name": "Smart Light Bulb", "price": 2000,"stock": 25,"sold": 50},
    "P126": { "name": "Smart Thermostat", "price": 10000,"stock": 5,"sold": 12},
    "P127": { "name": "Smart Door Lock", "price": 15000,"stock": 8,"sold": 18},
    "P128": { "name": "Smart Security Camera", "price": 12000,"stock": 10,"sold": 22},
    "P129": { "name": "Smart Smoke Detector", "price": 8000,"stock": 12,"sold": 30},
    "P130": { "name": "Smart Plug", "price": 2000,"stock": 20,"sold": 40}}
#-----------------------------------------------------------------------------------------------
# to maintain the menu driven program
#--------------------------------------------------------------------------------------------
while True:
    print("\nMenu:")
    print("1. Display all products")
    print("2. Add a new product")
    print("3. Update stock after sales")
    print("4. Find out-of-stock products")
    print("5. Find products with stock less than 5")
    print("6. Calculate total inventory value")
    print("7. Find best-selling product")
    print("8. Find least-selling product")
    print("9. Calculate total revenue generated")
    print("10. Generate a low-stock report")
    print("11. Display products whose sales exceed the average sales")
    print("12. Create a dictionary of products eligible for promotion (sales < 10)")
    print("13. Business Report")
    print("14. Exit")
    #-----------------------------------------------------------------------------------------
    #to take input from the user
    choice = input("Enter your choice (1-13): ")
    #-----------------------------------------------------------------------------------------
    # to display all products
    if choice == '1':
        print("\nAll Products:")
        for pid in products:
            print(pid, ":", products[pid])
    #-----------------------------------------------------------------------------------------
    # to add a new product
    elif choice == '2':
        pid = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        sold = int(input("Enter product sold quantity: "))
        products[pid] = {"name": name, "price": price, "stock": stock, "sold": sold}
        print("Product added successfully.")
    #-----------------------------------------------------------------------------------------
    # to update stock after sales
    elif choice == '3':
        pid = input("enter product id: ")
        quantity = int(input("Enter quantity sold: "))
        if pid in products:
            if products[pid]["stock"] >= quantity:
                products[pid]["stock"] -= quantity
                products[pid]["sold"] += quantity
                print("Stock updated successfully.")
            else:
                print("Insufficient stock.")
        else:
            print("Product not found.")
    #----------------------------------------------------------------------------------------
    # to find out-of-stock products
    elif choice == '4': 
        print("\nOut-of-Stock Products:")
        for pid in products:
            if products[pid]["stock"]==0:
                print(pid, ":", products[pid])
    #----------------------------------------------------------------------------------------
    # to find products with stock less than 5
    elif choice == '5':
        print("\nProducts with Stock Less than 5:")
        for pid in products:
            if products[pid]["stock"] < 5:
                print(pid, ":", products[pid])
    #----------------------------------------------------------------------------------------
    # to calculate total inventory value
    elif choice =='6':
        total_value =0
        for pid in products:
            total_value += products[pid]["price"] * products[pid]["stock"]
        print("Total Inventory Value:", total_value)
    #----------------------------------------------------------------------------------------
    # to find best-selling product
    elif choice == '7':
        items = list(products.items())
        best_id = items[0][0]
        best_sold = items[0][1]["sold"]
        for pid in products:
            if products[pid]["sold"] > best_sold:
                best_id = pid
                best_sold = products[pid]["sold"]
        print("Best-Selling Product:", best_id, ":", products[best_id])
    #----------------------------------------------------------------------------------------
    # to find least-selling product
    elif choice == '8':
        items = list(products.items())
        least_id = items[0][0]
        least_sold = items[0][1]["sold"]
        for pid in products:
            if products[pid]["sold"] < least_sold:
                least_id = pid
                least_sold = products[pid]["sold"]
        print("Least-Selling Product:", least_id, ":", products[least_id])
    #----------------------------------------------------------------------------------------
    # to calculate total revenue generated
    elif choice == '9':
        total_revenue = 0
        for pid in products:
            total_revenue += products[pid]["price"] * products[pid]["sold"]
        print("Total Revenue Generated:", total_revenue)
    #----------------------------------------------------------------------------------------
    # to generate a low-stock report
    elif choice == '10':
        print("\nLow-Stock Report:")
        for pid in products:
            if products[pid]["stock"] < 5:
                print(pid, ":", products[pid])
    #----------------------------------------------------------------------------------------
    # to display products whose sales exceed the average sales
    elif choice == '11':
        total_sold = 0
        for pid in products:
            total_sold += products[pid]["sold"]
        average_sold = total_sold / len(products)
        print("\nProducts with Sales Exceeding Average Sales:")
        for pid in products:
            if products[pid]["sold"] > average_sold:
                print(pid, ":", products[pid])
    #----------------------------------------------------------------------------------------
    # to create a dictionary of products eligible for promotion (sales < 10)
    elif choice == '12':
        promotion_products = {} # empty dictionary to store products eligible for promotion(62 bytes)
        for pid in products:
            if products[pid]["sold"] < 10:
                promotion_products[pid] = products[pid]
        print("\nProducts Eligible for Promotion:")
        for pid in promotion_products:
            print(pid, ":", promotion_products[pid])
    #----------------------------------------------------------------------------------------
    elif choice == '13':

         low_stock_count = 0

         for pid in products:
             if products[pid]["stock"] < 5:
                low_stock_count += 1

         promotion_count = 0

         for pid in products:
             if products[pid]["sold"] < 10:
                promotion_count += 1
         total_value =0
         
         for pid in products:
             total_value += products[pid]["price"] * products[pid]["stock"]
         total_revenue = 0
         for pid in products:
             total_revenue += products[pid]["price"] * products[pid]["sold"]
         print("Total Revenue Generated:", total_revenue)
#---------------------------------------------------------------------
         print("\n========== BUSINESS REPORT ==========")

         print("Total Products :", len(products))

         print("Inventory Value :", total_value)

         print("Total Revenue :", total_revenue)
         print("Low Stock Products :", low_stock_count)

         print("Promotion Products :", promotion_count)

         print("=====================================") 
    elif choice == '14':
         print("Exiting...")
         break

