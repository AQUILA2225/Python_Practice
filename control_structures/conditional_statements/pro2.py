# 2. Check whether a number is even or odd.
# Using Modulus operator

n = int(input("Enter a number:"))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Using Bitwise AND operator

n1 = int(input("Enter a number:"))
if (n1 & 1) == 0:
    print("Even")
else:
    print("Odd")

# Using Ternary operator
n = int(input("Enter a number:"))
print("Even" if n%2==0 else "Odd")

