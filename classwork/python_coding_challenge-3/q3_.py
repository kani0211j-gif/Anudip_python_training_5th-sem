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
# to count the usage of frequency of each coupons
coupon_frequency = {}
filev = open('coupons.txt','r')
# to check the file-------------------------------------------------------
if not filev:
    print("file doesnt exist")
    for line in filev:
        coupon = line.strip()
        if coupon in coupon_frequency:
            coupon_frequency += 1 
        else:
            coupon_frequency = 1 
print("coupon frequency  is : ",coupon_frequency)
#----------------------------------------------------------------------------
# to create a set of unique words
#_----------------------------------------------------------------------
# to display the most frequently used coupon



        
        
    

