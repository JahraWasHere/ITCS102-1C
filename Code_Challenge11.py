print("\t\t   *", end=" ")
for loop in range(1,11,1):
    for x in range(11,loop,-1):
        print(" ", end= " ")
    for y in range(1,loop,1):
        print("*", end= " ")
    for z in range(1,loop,1):
        print("*", end= " ")
    print()
