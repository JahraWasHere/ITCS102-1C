#Goal: Create a multiplication table up to 10 with the number provided by the User

number = eval(input("Please Enter a number here and i will make a multiplication table of up to 10 with it! ---> "))

for loop in range(1,11,1):
    num = number * loop
    print(number,"x",loop,"=", num)

print("\nThis is the multiplication table for",number,"!")
