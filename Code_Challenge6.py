odd_number = 0
for loop in range(1,11,1):
    numbers = eval(input("Please Enter your Numbers Here! ---> "))
    if numbers % 2 != 0:
        odd_number += numbers
    
print("The sum of all the odd numbers that you have inserted is", odd_number)
