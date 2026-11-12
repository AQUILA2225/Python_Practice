# 3. Check whether a person is eligible to vote (18 years or older).

# Using if-else

age = int(input("enter age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

# Using if-elif-else (input validation)

age = int(input("Enter age:"))
if age<=0:
    print("Invalid age")
elif age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
