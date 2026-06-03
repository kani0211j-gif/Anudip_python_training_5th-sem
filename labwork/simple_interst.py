#to calculate simple interest 
principal = float(input("Enter Principal Amount : "))

# validate principal
if(principal <= 0):
    exit("Principal Amount must be positive")

# ---------------------------------------------

rate = float(input("Enter Rate of Interest : "))

# validate rate
if(rate <= 0):
    exit("Rate of Interest must be positive")

# ---------------------------------------------

time = float(input("Enter Time : "))

# validate time
if(time <= 0):
    exit("Time must be positive")

# ---------------------------------------------

si = (principal * rate * time) / 100

print("Simple Interest =", si)


