# main.py
# 2D Geometry Calculator

from geometry import *

# -----------------------------------
# Main Program
# -----------------------------------

while True:

    # Figure Menu
    print("\n===== Figure Menu =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    figure = int(input("Enter your choice: "))

    # Exit Option
    if figure == 4:
        print("Thank You for Using the Application")
        break

    # -----------------------------------
    # Circle
    # -----------------------------------
    elif figure == 1:

        radius = float(input("Enter Radius: "))

        if radius <= 0:
            print("Radius must be positive")
            continue

        while True:

            print("\n===== Operation Menu =====")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            operation = int(input("Enter your choice: "))

            if operation == 1:
                area = circle_area(radius)
                print("Area of Circle =", round(area, 2))

            elif operation == 2:
                perimeter = circle_perimeter(radius)
                print("Perimeter of Circle =", round(perimeter, 2))

            elif operation == 3:
                break

            else:
                print("Invalid Choice")

            choice = input("Do you want another operation on same figure? (Y/N): ")

            if choice.upper() != "Y":
                break

    # -----------------------------------
    # Square
    # -----------------------------------
    elif figure == 2:

        side = float(input("Enter Side: "))

        if side <= 0:
            print("Side must be positive")
            continue

        while True:

            print("\n===== Operation Menu =====")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            operation = int(input("Enter your choice: "))

            if operation == 1:
                area = square_area(side)
                print("Area of Square =", area)

            elif operation == 2:
                perimeter = square_perimeter(side)
                print("Perimeter of Square =", perimeter)

            elif operation == 3:
                break

            else:
                print("Invalid Choice")

            choice = input("Do you want another operation on same figure? (Y/N): ")

            if choice.upper() != "Y":
                break

    # -----------------------------------
    # Rectangle
    # -----------------------------------
    elif figure == 3:

        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))

        if length <= 0 or breadth <= 0:
            print("Length and Breadth must be positive")
            continue

        while True:

            print("\n===== Operation Menu =====")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            operation = int(input("Enter your choice: "))

            if operation == 1:
                area = rectangle_area(length, breadth)
                print("Area of Rectangle =", area)

            elif operation == 2:
                perimeter = rectangle_perimeter(length, breadth)
                print("Perimeter of Rectangle =", perimeter)

            elif operation == 3:
                break

            else:
                print("Invalid Choice")

            choice = input("Do you want another operation on same figure? (Y/N): ")

            if choice.upper() != "Y":
                break

    else:
        print("Invalid Figure Choice")

    # -----------------------------------
    # Continue Program
    # -----------------------------------

    continue_choice = input("\nDo you want to continue using application? (Y/N): ")

    if continue_choice.upper() != "Y":
        print("Thank You for Using the Application")
        break