string = input("Enter any string")
result = ""

for ch in string:
    if ch not in result:
        result += ch

print("String without duplicates:", result)