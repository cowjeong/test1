x = int(input('숫자를 입력하세요 :'))
for i in range(1, x+1):
    if not( i % 5 == 0):
        print(i, end = ' ')
print()     