for loop in range(1,10,1):
    for x in range(10,loop ,-1):
        print(" ",end= " ")
    for y in range(loop, 0, -1):
        print(y, end= " ")
    for z in range(2, loop +1):
        print(z, end= " ")
    print()
