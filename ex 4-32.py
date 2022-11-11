hap, a, b =0, 0, 0
while True :
    a = int(input("첫번째 수를 입력하세요(0을 입력하면 종료 :"))
    if a == 0 :
        break 
    b = int(input("두번째 수를 입력하세요 : "))
    hap = a + b
    print("%d + %d = %d" % (a, b, hap))

print("0을 입력해 반복문을 탈출했습니다")