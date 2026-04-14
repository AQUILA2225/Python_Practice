# Area of Circle
# Formula: pi*r*r(r(radius) square)
# Value of pi is 3.14

# input() -> takes input from the user and input stores as string
# float() -> converts the string into a decimal number
# The given value stored in the variable called radius
# Than calculates the area of the circle by using formula and with given radius
# the result is stored in variable called area
# Than prints the result and the the f-string formatting(f"") allows the user to insert variables directly inside {}

radius = float(input("Enter the radius of the circle:"))
area = 3.14 * radius * radius
print(f"Area of the Circle is:{area}")

# IMPROVEMENT of program 
# Python has a built-in value for π in the math module
# So we can write the program in this way also
# math.pi gives more accurate value

import math 
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
# area = math.pi * radius * radius
# area = 3.14 * radius ** 2
print(f"Area of the circle is: {area}")
# print("Area of the circle is:", area)

# Using a Function(Better Programming Practice)
# 1. Python reads the function definition, here python does not execute the function 
# it only creates the function and stores it in memory 
# Python executes the input statement, here input() displays the message and user enters the values
# than input is stored as string, float() converts it into a decimal number
# than the value is stored in variable r
# than python calls the function calculate_area(r)
# the value os r is passed to the function, so inside the function (radius=r)
# than Function executes, inside the function(return 3.14 * radius * radius)
# the keyword "return" send the result back to the caller
# Print statement executes 


def calculate_area(radius):
    return 3.14 * radius * radius


r = float(input("Enter radius: "))
area = calculate_area(r)
print(f"Area of the circle is: {area}")
