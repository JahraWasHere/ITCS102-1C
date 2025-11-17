from Activity23_1 import *

print("Hello! Welcome!")
name = input("What's your name? Dear Visitor ---> ")
loc = input("Where do you live? (City) ---> ")
age = input("How old are you? ---> ")
print(f"Hello {name}! Please Select from the options below!\nA - Greet Name\nB - Greet with Name, Location, Age\nC - Triangle\nD - Factorial\nE - Exit")

variable = True
while variable == True:
    choice = input("Please Select your choice ---> ")
    if choice.lower() == "e":
        print("Exiting Program!")
        break
    elif choice.lower() == "a":
        greet(name)
        continue
    elif choice.lower() == "b":
        greetings(name,loc,age)
        continue
    elif choice.lower() == "c":
        size = eval(input("How large do you want the tringle to be? (1-10) ---> "))
        if size < 11:   
            triangle(size)
        elif size == 67:
            print("Please get out of here")
        else:
            print("Bruh")
        continue
    elif choice.lower() == "d":
        number = eval(input("Please Enter a Number! ---> "))
        print(f"The Factorial of {number} is {Factorial(number)}")
        continue
    else:
        print("Bruh")
        continue
