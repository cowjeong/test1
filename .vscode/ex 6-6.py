def add_print(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add_print(1, 9)
hap = add_print(3, 4)
print(hap) #hap에는 리턴되는 값이 없으므로 none이 출력된다