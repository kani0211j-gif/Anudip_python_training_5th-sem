#creating a list of inventory 
#to check available,out of stock and restock required as well as healthy stock in list 
stock=[ 25,5,0,12,3,18,0,30]
#count for out of stock
#count for available stock
out_of_stock=0
available_product=0
#creating list for restock nd healthy stock
restock_Required = []
healthy_stock=[]
#creating loop for traversing
for item in stock:
    #checking for out of stock 
    if item==0:
       out_of_stock+=1
    # checking for available stock
    else:
       available_product+=1
     # Restocking required
    if item < 10:
        restock_Required.append(item)
     # Healthy stock
    if item >= 15:
        healthy_stock.append(item)
# Display results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_Required)
print("Available Products:", available_product)
print("Healthy Stock:", healthy_stock)


