#Goal: Start a countdown starting from the number provided by the User, Which prints "Liftoff!" When finished

print("We should countdown for something Special!")
countdown = eval(input("Please enter a number and we will start a countdown! ---> "))

for loop in range(countdown,0,-1):
    print(loop)

print("We Have Lifted off!")
