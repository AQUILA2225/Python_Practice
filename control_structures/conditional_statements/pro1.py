# 1. Check whether a number is positive or negative.
# using if-elif-else

num = int(input("Enter a number:"))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is Zero")

# Using nested-if

n = int(input("Enter a number:"))
if n>0:
    if n==0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
    
# Using Ternary operator

n1 = int(input("Enter a number"))
print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

