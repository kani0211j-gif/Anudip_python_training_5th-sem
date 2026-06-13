'''Problem 3: E-Commerce Coupon Fraud Detection
Problem Statement
A file named coupons.txt contains coupon usage records.
SAVE50
WELCOME20
SAVE50
FESTIVE10
SAVE50
WELCOME20
NEWUSER
FESTIVE10
SAVE50
NEWUSER
Tasks
1. Count the usage frequency of each coupon.
2. Identify coupons used more than 3 times.
3. Create a set of unique coupons.
4. Display the most frequently used coupon.
5. Save suspicious coupon records into fraud_report.txt.
Sample Output
Coupon Usage Frequency:
SAVE50 : 4
WELCOME20 : 2
FESTIVE10 : 2
NEWUSER : 2
Suspicious Coupons:
SAVE50
Unique Coupons:
{'SAVE50', 'WELCOME20', 'FESTIVE10', 'NEWUSER'}
Most Frequently Used Coupon:
SAVE50
Fraud Report Generated Successfully'''
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# open the file

filev = open("coupons.txt","r")
if not filev:
    print("error in opening the file")

content = filev.readlines()

filev.close()

#----------------------------------------------------------------------------------
# count frequency of each coupon

coupon_freq = {}

for line in content:

    coupon = line.strip()

    if coupon in coupon_freq:
        coupon_freq[coupon] += 1

    else:
        coupon_freq[coupon] = 1

print("Coupon Usage Frequency :")

for coupon in coupon_freq:
    print(coupon,":",coupon_freq[coupon])

#----------------------------------------------------------------------------------
# identify suspicious coupons (used more than 3 times)

suspicious = []

for coupon in coupon_freq:

    if coupon_freq[coupon] > 3:
        suspicious.append(coupon)

print("\nSuspicious Coupons :")

for coupon in suspicious:
    print(coupon)

#----------------------------------------------------------------------------------
# create set of unique coupons

unique_coupons = set()

for line in content:
    unique_coupons.add(line.strip())

print("\nUnique Coupons :")
print(unique_coupons)

#----------------------------------------------------------------------------------
# find most frequently used coupon

max_coupon = ""
max_count = 0

for coupon in coupon_freq:

    if coupon_freq[coupon] > max_count:
        max_count = coupon_freq[coupon]
        max_coupon = coupon

print("\nMost Frequently Used Coupon :")
print(max_coupon)

#----------------------------------------------------------------------------------
# save suspicious coupons in fraud report

filev = open("fraud_report.txt","w")

for coupon in suspicious:
    filev.write(coupon + "\n")

filev.close()

print("\nFraud Report Generated Successfully")
#---------------------------------------------------------------------------
#output will be 
'''Coupon Usage Frequency :
SAVE50 : 4
WELCOME20 : 2
FESTIVE10 : 2
NEWUSER : 2

Suspicious Coupons :
SAVE50

Unique Coupons :
{'SAVE50', 'FESTIVE10', 'NEWUSER', 'WELCOME20'}

Most Frequently Used Coupon :
SAVE50

Fraud Report Generated Successfully'''



        
        
    

