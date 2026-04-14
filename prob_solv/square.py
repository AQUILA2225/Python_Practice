# Area of a Square
# Formula -> side * side OR side ** 2

side = float(input("Enter the Side: "))
area = side ** 2
print(f"Area of a Square is: {area}")

# Using Functions (Better Programming Practice)


def calculate_area(side):
    return side ** 2


side = float(input("Enter Side: "))
area = calculate_area(side)
print(f"Area of a Square is: {area}")
