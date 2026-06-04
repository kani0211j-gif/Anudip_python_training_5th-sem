num = int(input("Enter Number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
#----------------------------
print("Reverse:", rev)

if rev == num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

