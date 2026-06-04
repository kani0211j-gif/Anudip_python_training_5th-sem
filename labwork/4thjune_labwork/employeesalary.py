# Accept employee name
name = input("Enter Employee Name: ")

# Accept basic salary
basic_salary = float(input("Enter Basic Salary: ₹"))

# Validate salary
if basic_salary <= 0:
    print("Invalid Salary! Salary must be positive.")

else:

    # Calculate HRA (20% of Basic Salary)
    hra = basic_salary * 20 / 100

    # Calculate DA (10% of Basic Salary)
    da = basic_salary * 10 / 100

    # Calculate PF Deduction (12% of Basic Salary)
    pf = basic_salary * 12 / 100

    # Calculate Gross Salary
    gross_salary = basic_salary + hra + da

    # Calculate Net Salary
    net_salary = gross_salary - pf

    # Display Salary Details
    print("\n========== EMPLOYEE PAYROLL ==========")
    print("Employee Name :", name)
    print("Basic Salary  : ₹", basic_salary)
    print("HRA (20%)     : ₹", hra)
    print("DA (10%)      : ₹", da)
    print("PF (12%)      : ₹", pf)
    print("Gross Salary  : ₹", gross_salary)
    print("Net Salary    : ₹", net_salary)

    # Determine Employee Grade
    if net_salary > 50000:
        print("Grade         : Senior Grade")

    elif net_salary > 30000:
        print("Grade         : Mid Grade")

    else:
        print("Grade         : Junior Grade")

