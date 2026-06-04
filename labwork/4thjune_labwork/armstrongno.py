num = int(input("Enter Number: "))

temp = num
sum1 = 0

while temp > 0:
    digit = temp % 10
    sum1 += digit * digit * digit
    temp = temp // 10

if sum1 == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

