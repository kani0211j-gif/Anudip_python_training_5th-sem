salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# show employees earning above 60000
print("--- High Earners ---")
for emp, sal in salary.items():
    if sal > 60000:
        print(emp, ":", sal)

# count employees earning below 40000
low_salary_count = 0
for sal in salary.values():
    if sal < 40000:
        low_salary_count += 1
print("\nEmployees earning below 40,000:", low_salary_count)

# find highest paid employee
highest_paid_emp = ""
max_salary = 0
for emp, sal in salary.items():
    if sal > max_salary:
        max_salary = sal
        highest_paid_emp = emp
print("\nHighest paid employee:", highest_paid_emp, "Salary:", max_salary)

# list employees eligible for bonus
bonus_list = []
for emp, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp)
print("\nEligible for bonus:", bonus_list)

# find the average salary
total_sal = 0
for sal in salary.values():
    total_sal += sal
avg_salary = total_sal / len(salary)
print("\nAverage salary:", avg_salary)

