# print name and age using print()
name = "Aquila"
age = 20
print("Name:", name)
print("Age:", age)

# swaping two numbers using variables
x = 1
y = 2

x, y = y, x
print("x =", x)
print("y =", y)

# Formatted string
name = "Aquila"
age = 21
city = "Hyderabad"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# taking user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum =", sum)

# variables and their data types, and type()
a = 10      # int
b = 5.5     # float
c = 2 + 3j # complex
d = False    # boolean
e = "Python" # string

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

# convert int to float
num = input("Enter a number: ")
if num.isdigit():
    num = float(num)
    print("Converted to float:", num, type(num))
else:
    print("Not a number")

# swapping 3 numbers
x = 5
y = 10
z = 15
x, y, z = z, x, y
print("x =", x, "y =", y, "z =", z)

# div by 3 and 5
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")
    
# largest of three nums
a = 12
b = 25
c = 7
d = 30

if a > b and a > c and a > d:
    largest = a
elif b > c and b > d:
    largest = b
elif c > d:
    largest = c
else:
    largest = d
    
print("Largest number is:", largest)

# to find weather a number is pos, neg, or zero
num = -5
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# check a char in vowel or not
ch = 'e'
if ch in 'aeiouAEIOU':
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")

# grades of a student
marks = 82

if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
else:
    grade = 'F'

print("Grade:", grade)

# num is positive and even: nested if
num = 12
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive but Odd")
else:
    print("Negative number or Zero")

# print nums from 10 to 1 in rev using for loop
for i in range(10, 0, -1):
    print(i)

# sum of first 50 natural numbers using for loop
sum = 0
for i in range(1, 51):
    sum += i
print("Sum =", sum)

# multiples of 5 btw 1 to 100
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")

# fact of a num using for loop
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


# fibonacci series
n1, n2 = 0, 1
print(n1, n2, end=" ")
for i in range(8):
    n3 = n1 + n2
    print(n3, end=" ")
    n1, n2 = n2, n3

# rev string 
text = "Python"
rev = ""
for char in text:
    rev = char + rev
print("Reversed string:", rev)

# count evens and odds in a given list of numbers
numbers = [1,2,3,4,5,6,7,8]
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, "Odd:", odd)

# print prime numbers btw 1 to 50
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

# sum of squares of numbers from 1 to 10
sum_squares = 0
for i in range(1, 11):
    sum_squares += i**2
print("Sum of squares:", sum_squares)

# list of squares using for loop
squares = []
for i in range(1, 11):
    squares.append(i**2)
print("Squares List", squares)
        
# div by 3 or 5 but not both
for i in range(1, 51):
    if (i % 3 == 0) != (i % 5 == 0):
        print(i, end=" ")
