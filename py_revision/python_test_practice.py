# Q1
sum = 0
for i in range(1, 6):
    if i % 2 == 0:
        sum += i
print(sum)

# Q2
# ps

# sum of even and odd
even = 0
odd = 0

for i in range(1, 11):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("Even sum:", even)
print("Odd sum:", odd)

# count vowels in a string 
text = input("Enter string: ")
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels:", count)

# count vowels and consonents in a given string 

text = input("Enter string: ")
count_vowels = 0
count_cons = 0
vowels = "aeiouAEIOU"
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            count_vowels += 1
        else:
            count_cons += 1

print("Vowels:", count_vowels)
print("Consonants:", count_cons)