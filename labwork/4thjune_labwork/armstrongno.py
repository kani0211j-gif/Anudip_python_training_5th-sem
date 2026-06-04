num = int(input("Enter Number: "))

digits = len(str(num))

temp = num
sum1 = 0

while temp > 0:
    digit = temp % 10
    sum1 = sum1 + (digit ** digits)
    temp = temp // 10

if sum1 == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")