import random

print("********************\n\nWelcome to the Gambling Game!\n\n********************")
print("How Do You Play? Simple, Guess The number I'm Thinking of from 1-10!")

random_value = random.randint(1,10)
tries = 0
variable = True

name = input("Now Enter Your Name, My Dear Guest! ---> ")

while variable == True:
    num = eval(input("Now Enter the Number You're Going to Guess! ---> "))
    tries += 1
    if num == random_value:
        print("Hey, Congratulations! You Guessed Correctly!")
        break
    else:
        print("Nope! Try Again!")
        continue

print(f"Nice One {name}!, You Guessed Correctly!, It took you {tries} tries!")
