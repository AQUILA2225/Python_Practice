# Execution flow:
# 1. User enters values of num1 and num2
# 2. Than python interpreter evaluates or checks the condition:
# a.if the condition is TRUE -> the if block executes.
# b.if the condition is FALSE -> the else block executes.

num1 = float(input("Enter the value/dividend of num1:"))
num2 = float(input("Enter the value/divisor of num2:"))

if num2 == 0:
    print("Error: Division by Zero is not allowed")
else:
    division = num1/num2
    print(f"Division Result:{division}")
