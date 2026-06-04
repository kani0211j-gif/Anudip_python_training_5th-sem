# To calculate area nd perimeter of rectangle 
length = float(input("enter the length"))
if (length<=0):
    exit("length must be positive")
#--------------------------------------
breadth = float(input("enter the breadth"))
if (breadth<=0):
    exit("breadth must be positive")
#-------------------------------------------
area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of Rectangle =", area)
print("Perimeter of Rectangle =", perimeter)
