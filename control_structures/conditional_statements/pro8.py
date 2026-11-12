# 8.Check whether a student has passed (marks ≥ 35).
# Using if else

marks = int(input())
if marks>=35:
    print("pass")
else:
    print("fail")

# Using Ternary Operator

marks = int(input())
print("Pass" if marks >= 35 else "Fail")