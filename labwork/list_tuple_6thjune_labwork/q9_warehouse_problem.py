# Given data
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")]
# 1. Display failed product IDs
print("Failed Product IDs:")
for record in products:
    product_id = record[0]
    quality_status = record[1]
    if quality_status == "Fail":
        print("- Product ID:", product_id)

# 2. Count passed and failed products
passed_counter = 0
failed_counter = 0
for record in products:
    if record[1] == "Pass":
        passed_counter = passed_counter + 1
    else:
        failed_counter = failed_counter + 1

print("\nTotal Passed Products Count:", passed_counter)
print("Total Failed Products Count:", failed_counter)

# 3. Calculate pass percentage
total_products_inspected = len(products)
overall_pass_percentage = (passed_counter / total_products_inspected) * 100
print("Overall Pass Percentage:", overall_pass_percentage, "%")

# 4. Stop checking if 3 failures are found
print("\nExecuting inspection system check loop...")
critical_failure_tracker = 0
for record in products:
    print("Checking Product ID:", record[0], "| Status:", record[1])
    if record[1] == "Fail":
        critical_failure_tracker = critical_failure_tracker + 1
    
    if critical_failure_tracker == 3:
        print("System Alert: 3 failure conditions met. Terminating inspection process.")
        break
print("\n")

