name = input("Hello! What's your Name? --> ")
print("\n====================\n\nWelcome To The Odd Number Selector!\n\n====================\n")

var = True
sum = 0
odd = ""

while var == True:
    num = eval(input("Please Enter an Odd Number Here! ---> "))
    if num %2 == 1:
        print("Odd Number Detected!")
        sum += num
        odd += str(num) + " "
        continue
    elif num == 0:
        print("Stopping!")
        break
    else: 
        if num %2 == 0:
            print("Even Number Detected!")
            continue
        else:
            print("Invalid Number!")
            continue


print(f"Hello{name}The Sum of all Odd Numbers is {sum}!")
print(f"The Odd numbers included the following! ---> {odd}")
