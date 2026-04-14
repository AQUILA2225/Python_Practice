
# import random
# num = random.randint(1,100)
# x = 1
# while x<100:
#     x+=1
#     guess = int(input("Enter number:"))
#     if guess > num:
#         print("Too high")
#     elif guess < num:
#         print("Too low")
#     else:
#         print("Congragulations")
#         break


import random
num = random.randint(1,100)
while True:
    guess = int(input("Enter number:"))

    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too Low")
    else:
        print("Congragulations")
        break