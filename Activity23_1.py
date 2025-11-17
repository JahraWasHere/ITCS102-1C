def greet(name):
    print(f"Hello {name}! Nice to meet you!")

def greetings(name, loc, age):
    print(f"Hello {name}! From {loc}, Aged {age}")

def Return(number):
    sum = 0
    for x in range(1, number+1, 1):
        sum += x
    return sum

def Factorial(number):
    factorial = 1
    for x in range(number,0,-1):
        factorial *= x
    return factorial

def triangle(size):
    for x in range(1,size,1):
        for a in range(size,x,-1):
            print(" ",end=" ")
        for b in range(x,0,-1):
            print("*",end=" ")
        for c in range(x,0+1,-1):
            print("*",end=" ")
        print()
    return
