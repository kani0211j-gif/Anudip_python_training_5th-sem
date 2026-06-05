#creating of list 
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Empty lists and variables
passed = []
merit = []
failed_count = 0

# Assume first element as highest and lowest
highest = marks[0]
lowest = marks[0]

# Traverse the list
for mark in marks:

    # Passed students
    if mark >= 40:
        passed.append(mark)
    else:
        failed_count = failed_count + 1

    # Highest marks
    if mark > highest:
        highest = mark

    # Lowest marks
    if mark < lowest:
        lowest = mark

    # Merit list
    if mark > 75:
        merit.append(mark)

# Display results
print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)