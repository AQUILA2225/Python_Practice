# Given a string "hello", write a Python program using a for loop to reverse the string.

st = input("Enter the string to reverse:")
rev = ""
for ch in st:
    rev = ch + rev
print("Reverse String", rev)
        