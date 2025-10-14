isDirty = True
while isDirty == True:
    wash_again = input("Continue Washing the Clothes? (Y/N) ---> ").lower()

    if wash_again == 'y':
        print("Washing...")
        continue
    else:
        print("Stopping...")
        break
