#list of employee data 
employees = [
 ("Rahul", 35000),
 ("Priya", 55000),
 ("Amit", 42000),
 ("Neha", 65000)
]
#employees earning above 50000
for emp in employees :
    if emp[1]>500000:
        print("employees earning above ₹50,000",emp[0])
# 2. Find the highest-paid employee
highest_paid_employee = employees[0]
for emp in employees:
    if emp[1] > highest_paid_employee[1]:
        highest_paid_employee = emp
print("\nHighest-paid employee:", highest_paid_employee[0], "Salary:", highest_paid_employee[1])
# 3. Calculate total salary expenditure
total_salary_expenditure = 0
total_salary_expenditure = total_salary_expenditure + emp[1]
print("Total salary expenditure:", total_salary_expenditure)
# 4. Count employees earning below 40,000
below_40k_count = 0
for emp in employees:
    if emp[1] < 40000:
        below_40k_count = below_40k_count + 1
print("Number of employees earning below 40,000:", below_40k_count)
print("\n")
        
        


