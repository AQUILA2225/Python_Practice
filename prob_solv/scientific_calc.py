import math 

print("Scientific Calculator")
print("1. Square Root")
print("2. Power")
print("3. Log")
print("4. Sin")
print("5. Cos")
print("6. Tan")
print("7. Factorial")

while True:
    def  square(n):
        result = math.sqrt(n)
        print(f"Square of {n} is ", result)
    
    def power(m,n):
        result = math.pow(m,n)
        print(f"Power of {m,n} is", result)
    
    def log(n):
        result = math.log(n)
        print(result)

    def sin(n):
        result = math.sin(math.radians(n))
        print(result)
    
    def cos(n):
        result = math.cos(math.radians(n))
        print(result)

    def tan(n):
        result = math.tan(math.radians(n))   
        print(result)
    
    def fact(n):
        result = math.factorial(n)
        print(result)

    ch = int(input("Enter your choice:"))

    if ch == 1:
        n = int(input("Enter number:"))
        square(n)

    elif ch == 2:
        m = int(input("Enter value of m:"))
        n = int(input("Enter value of n"))
        power(m,n)

    elif ch == 3:
        n = int(input("Enter number:"))
        log(n)
    
    elif ch == 4:
        n = int(input("Enter angle in degrees:"))
        sin(n)

    elif ch == 5:
        n = int(input("Enter angle in degrees:"))
        cos(n)

    elif ch == 6:
        n = int(input("Enter angle in degrees:"))
        tan(n)

    elif ch == 7:
        n = int(input("Enter number:"))
        fact(n)
    elif ch == 8:
        print("Existing Calculator....")
        break
    else:
        print("Invalid Choice!!!")