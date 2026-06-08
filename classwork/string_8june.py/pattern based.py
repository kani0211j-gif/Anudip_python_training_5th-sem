'''to ask tothe user tho input number of rows  and then display pattern
i.e, n = 5
*
**
***
****
*****
----------------------------------------------
'''
rows = int(input("Enter the number of rows: "))
if(rows<=0):
    exit("Invalid number of rows")
#to display pattern
for i in range(1, rows+1):
    print("*"*i)

