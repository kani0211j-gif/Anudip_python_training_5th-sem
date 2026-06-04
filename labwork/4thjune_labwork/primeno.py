num = int(input("Enter Number: "))

i = 1
count = 0

print("Factors:", end=" ")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
        count += 1
    i += 1

print()

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
