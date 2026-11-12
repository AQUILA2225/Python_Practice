# 10. Check whether a person is a child, teenager, or adult based on age.
# Using if-elif-else

age = int(input())
if age<13:
    print("Child")
elif age <=19:
    print("Teenager")
else:
    print("Adult")

# Using Explicit Ranges
age = int(input())
if 0<= age <=12:
    print("CHild")
elif 13<= age <=19:
    print("Teenager")
else:
    print("Adult")

# With Input Validation
age = int(input())
if age < 0:
    print("Invalid Age")
elif age < 13:
    print("Child")
elif age <=19:
    print("Teenager")
else:
    print("Adult")
