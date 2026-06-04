# Repeat until student scores 40 or more marks
while True:

    # Take marks as input
    marks = int(input("Enter Marks: "))

    # Check whether student has passed
    if marks >= 40:
        print("Result: Pass")

        # Display success message
        print("\nCongratulations! You have cleared the assessment.")
        break

    # Execute when marks are less than 40
    else:
        print("Result: Fail")
        print()

