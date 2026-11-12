# CHeck even or odd

# num = int(input("Enter number to check even or odd"))


# def check_even_odd(x):
#     if x % 2 == 0:
#         print(x, "it is even")
#     else:
#         print(x, "it is odd")

    
# check_even_odd(num)


# num1 = int(input("Enter number 1 :"))
# num2 = int(input("Enter number 2:"))


# def check_even_odd(x, y):
#     print("Total no of even numbers in the range")
#     totalEvenSum = 0
#     totalOddSum = 0
#     for i in range(x, y+1):
#         if i % 2 == 0:
#             print(i)
#             totalEvenSum += i
#         else:
#             print(i)
#             totalOddSum += i

#     print(totalEvenSum, "totalevensum")
    
    
# check_even_odd(num1, num2)

# Find number div by 5 not by 10

# num = int(input("Enter number"))

# def divBy5notby10(a):
#     if a % 5 == 0 and a % 10 != 0:
#         print(a, "is divisible by 5 but not by 10")
#     elif a % 10 == 0:
#         print(a, "is divisible by 10")
#     else:
#         print(a, "not div by 10" )
        
# divBy5notby10(num)

# find factors of a num

num1 = int(input("Enter a number1"))

def findfactors(x):
    factors = []
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            factors. append(i)
            print(i, "is factor for", x)
            count += 1  
    print(factors)
    print(count)

findfactors(num1)

#factorial

num = int(input("Enter number:"))
def fact(x):
    fact = 1
    for i in range(x, 0, -1):
        fact = fact * i
        print(i)
    print(f"The factorial of {i} : ", fact)

fact(num)