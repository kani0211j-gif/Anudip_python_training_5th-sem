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
# to open the file
filev = open('login_logs.txt','r')
#to check if file open or not 
if not filev:
    print("error in opening the file")
content = filev.readlines()
filev.close()
#----------------------------------------------------------------------------
#to check failed nd successful count 
failed_count = 0
success_count = 0
for line in content:
    data = line.split(',')
    if data[1]=="success":
        success_count += 1
    else:
        failed_count += 1
print("no. of failure : ",failed_count)
print("no of success count : ", success_count)
#-------------------------------------------------------------------------
# user more than 2 failed attempt 
failure_count = {}
for line in content:
    data = line.split(',')
    if data[1]=="failed":
        if data[0] in failure_count:
            failure_count[data[0]] += 1
        else:
            failure_count[data[0]] = 1
#--------------------------------------------------------------------------        
# to create frequency dictionary 




      



    
    
    
    


