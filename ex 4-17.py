for i in range(1, 10):
    guguLine =""
    for k in range(2, 10):
        guguLine += str("%dX%d=%2d  " % (k, i, k*i))
    print(guguLine)