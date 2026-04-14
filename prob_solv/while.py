# revse a number using while looop
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)

# Reverse + Sum of eben and odd
num = int(input("Enter number: "))
rev = 0
even_sum = 0
odd_sum = 0

while num > 0:
    digit = num % 10
    
    rev = rev * 10 + digit
    
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    
    num = num // 10

print("Reversed:", rev)
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

# nums from 1 to 100 and div by 5
i = 1
while i <= 100:
    if i % 5 == 0:
        print(i, end=" ")
    i += 1
