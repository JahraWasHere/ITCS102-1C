#Goal: Enter the factorial of the number the user has provided

number = eval(input("Please enter a Number Here! ---> "))
factorial = 1

for loop in range(number, 0, -1):
    factorial *= loop

print("The factorial of this number is", factorial)
