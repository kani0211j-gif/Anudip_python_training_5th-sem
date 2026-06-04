num = int(input("Enter Number: "))

temp = num
sum1 = 0

while temp > 0:

    digit = temp % 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i += 1

    sum1 += fact
    temp = temp // 10

if sum1 == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")

