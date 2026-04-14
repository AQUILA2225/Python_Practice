g1 = 10
g2 = 20
g3 = 30


def func1():
    a = 1   
    b = 2

    print("Inside func1:")
    print("Local variables:", a, b)

    print("Accessing globals:", g1, g2, g3)

    # print(x, y)  # from func2 -> not accessible


def func2():
    x = 100  
    y = 200

    print("\nInside func2:")
    print("Local variables:", x, y)

    print("Accessing globals:", g1, g2, g3)

    # print(a, b)


def func3():
    p = 1000 
    q = 2000

    print("\nInside func3:")
    print("Local variables:", p, q)

    print("Accessing globals:", g1, g2, g3)

    # print(x, y)


func1()
func2()
func3()


x = 100   # Global variable
def show_global():
    print("Inside function:", x)
show_global()
print("Outside function:", x)

def show_local():
    y = 50   # Local variable
    print("Inside function:", y)

show_local()
# print(y)  

def outer():
    z = 200   # Enclosed variable

    def inner():
        print("Inside inner function:", z)

    inner()

outer()