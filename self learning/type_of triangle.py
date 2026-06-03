side1 = float(input("Enter first side : "))

# validate side1
if(side1 <= 0):
    exit("Side must be positive")

# ---------------------------------------------

side2 = float(input("Enter second side : "))

# validate side2
if(side2 <= 0):
    exit("Side must be positive")

# ---------------------------------------------

side3 = float(input("Enter third side : "))

# validate side3
if(side3 <= 0):
    exit("Side must be positive")

# ---------------------------------------------

# verifying triangle formation
if(side1 + side2 > side3 and
   side1 + side3 > side2 and
   side2 + side3 > side1):
# triangle is formed 
   if (side1==side2==side3):
       print("it is an equilateral triangle")
   elif(side1==side2 or side2==side3 or side1==side3):
       print("it is an isosceles triangle")
   else:
       print("it is an scalene triangle")
else:
    print("Above sides do not form a triangle")

