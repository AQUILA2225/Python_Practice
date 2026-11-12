# Area of a Rectanle
# Formula -> length * width/breadth

# input() -> takes inputs from the user for the variables length and width, it stores values as string
# float() -> converts string values into a decimal Values
# calculates area of rectangle and stores the result in the variable area
# than prints the result and the the f-string formatting(f"") allows the user to insert variables directly inside {}

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print(f"Area of a Rectanle: {area}")

# other way 

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# print("Area of the rectangle is:", length * width)

# Using a Function(Better Programming Practice)


def calculate_area(length, width):
    return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = calculate_area(length * width)

print(f"Area of a Rectangle: {area}")
