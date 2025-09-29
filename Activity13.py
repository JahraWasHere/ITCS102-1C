#Ask User to input 10 numbers - Done
#Get the summation of all numbers provided - Done

sum = 0
for loop in range(1,11,1):
    print(loop)
    number = eval(input("Please enter a number! ---> "))
    sum += number
print("\n\tThe Sum of all the numbers provided is ", sum)
