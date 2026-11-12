# 4. Check whether a number is divisible by 5.
# Using modulus operator

n = int(input("Enter a number:"))
if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

# Using Last digit property

n = int(input("Enter a number"))
last_digit = abs(n)%10
if last_digit == 0 or last_digit == 5:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

# Using Ternary Operator

n = int(input("Enter a number:"))
print("Divisible by 5" if n%5 == 0 else "Not divisible by 5")