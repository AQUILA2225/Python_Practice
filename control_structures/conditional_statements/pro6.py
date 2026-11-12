# 6. Find the smallest number between two numbers.
# Using if-elif-else

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))

if n1<n2:
    print(f"{n1} is smallest")
elif n1<n2:
    print(f"{n2} is smallest")
else:
    print("Both are equal")

# Using min() funtion

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))

if n1==n2:
    print("Both are equal")
else:
    print(min(n1,n2))

# Using Ternary Operator

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
print("Both are equal" if n1==n2 else f"{n1} is smallest" if n1<n2 else f"{n2} is smallest")