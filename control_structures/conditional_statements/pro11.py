# 11. Check whether a year is a leap year.

# Using Combined Condition
year = int(input())
if year % 400 ==0 or (year % 4==0 and year % 100 !=0):
    print("it is leap year")
else:
    print("It is not leap year")

# Using nested if else    
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("NOt a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")       
    



