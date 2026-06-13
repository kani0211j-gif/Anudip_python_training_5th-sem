''' 1: Cyber Security Login Audit System
Problem Statement
A file named login_logs.txt contains user login attempts in the following format:
username,status
anuj,Success
rahul,Failed
anuj,Failed
priya,Failed
rahul,Failed
neha,Success
anuj,Failed
karan,Failed
rahul,Success
priya,Failed
Tasks
1. Count successful and failed login attempts.
2. Identify users with more than 2 failed attempts.
3. Create a dictionary storing the number of failures per user.
4. Create a set of users who logged in successfully.
5. Display users whose accounts should be reviewed.
Sample Output
Successful Login Attempts: 3
Failed Login Attempts: 7
Failure Count per User:
anuj : 2
rahul : 2
priya : 2
karan : 1
Users with Successful Logins:
{'anuj', 'neha', 'rahul'}
Accounts Requiring Review:
None'''
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# to open the file
filev = open('login_logs.txt','r')

# to check if file open or not
if not filev:
    print("error in opening the file")

content = filev.readlines()
filev.close()

# remove heading
content = content[1:]

#--------------------------------------------------------------------------------------
# to check failed and successful count

failed_count = 0
success_count = 0

for line in content:
    data = line.strip().split(',')

    if data[1] == "Success":
        success_count += 1
    else:
        failed_count += 1

print("Successful Login Attempts :", success_count)
print("Failed Login Attempts :", failed_count)

#--------------------------------------------------------------------------------------
# to create failure count dictionary

failure_count = {}

for line in content:
    data = line.strip().split(',')

    if data[1] == "Failed":

        if data[0] in failure_count:
            failure_count[data[0]] += 1

        else:
            failure_count[data[0]] = 1

print("\nFailure Count per User :")

for user in failure_count:
    print(user,":",failure_count[user])

#--------------------------------------------------------------------------------------
# to create set of successful users

success_users = set()

for line in content:
    data = line.strip().split(',')

    if data[1] == "Success":
        success_users.add(data[0])

print("\nUsers with Successful Logins :")
print(success_users)
#---------------------------------------------------------------------#--------------------------------------------------------------------------------------
# users whose accounts should be reviewed

review_users = []

for user in failure_count:

    if failure_count[user] > 2:
        review_users.append(user)

print("\nAccounts Requiring Review :")

if len(review_users) == 0:
    print("None")

else:
    for user in review_users:
        print(user)
#---------------------------------------------------------------------------
#output will be
'''#output will be
Successful Login Attempts : 2
Failed Login Attempts : 7

Failure Count per User :
rahul : 2
anuj : 2
priya : 2
karan : 1

Users with Successful Logins :
{'rahul', 'neha'}

Accounts Requiring Review :
None'''



      



    
    
    
    


