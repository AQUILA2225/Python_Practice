# 9. Check whether a number is a multiple of 10.
# Using Modulus Operator

num = int(input("Enter a number"))

if num % 10 == 0:
    print(f"{num} is multiple of 10")
else:
    print(f"{num} is not multiple of 10")


# Using Ternary Operator
num = int(input())
print("Yes" if num % 10 == 0 else "No")

# Using Boolean Expression
num = int(input())

result = num % 10 ==0
if result:
    print("Yes")
else:
    print("NO")
