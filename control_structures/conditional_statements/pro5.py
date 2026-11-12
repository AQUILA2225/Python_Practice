# 5. Find the greater number between two numbers.
# Using if-elif-else

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))

if n1>n2:
    print(f"{n1} is greater")
elif n1<n2:
    print(f"{n2} is greater")
else:
    print("Both are equal")

# Using max() funtion

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))

if n1==n2:
    print("Both are equal")
else:
    print(max(n1,n2))

# Using Ternary Operator

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
print("Both are equal" if n1==n2 else f"{n1} is greater" if n1>n2 else f"{n2} is greater")