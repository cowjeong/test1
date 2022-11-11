def add_m(*args):
    result = 0
    for i in args:
        result = result + i
    return result

r1 = add_m(1, 2, 3)
print('r1 = ', r1)

r2 = add_m(1, 2, 3, 4 )
print('r2 = ', r2)

r3 = add_m(1,2,3,4,5,6)
print('r3 = ', r3)