# geometry.py
# Module for Geometry Calculations

# -----------------------------------
# Circle Functions
# -----------------------------------

# Function to calculate area of circle
def circle_area(radius):
    return 3.14 * radius * radius

# Function to calculate perimeter of circle
def circle_perimeter(radius):
    return 2 * 3.14 * radius


# -----------------------------------
# Square Functions
# -----------------------------------

# Function to calculate area of square
def square_area(side):
    return side * side

# Function to calculate perimeter of square
def square_perimeter(side):
    return 4 * side


# -----------------------------------
# Rectangle Functions
# -----------------------------------

# Function to calculate area of rectangle
def rectangle_area(length, breadth):
    return length * breadth

# Function to calculate perimeter of rectangle
def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

