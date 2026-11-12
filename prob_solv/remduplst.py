lst = [1, 2, 2, 3, 4, 3, 5]
new_list = []

for num in lst:
    if num not in new_list:
        new_list.append(num)

print("List without duplicates:", new_list)