a =int(input('-10에서 10 사이의 정수를 입력하세요: '))
if (a > 10) :
    print('입력한 정수는 %d이고 10보다 큼' % a)
elif(a > 0) :
    print('입력한 정수는 %d이고 양수임' % a)
elif( a == 0) :
    print('입력한 정수는 0임')
elif( a < -10) :
    print('입력한 정수는 %d이고 -10보다 작음' % a)
else :
    print('입력한 정수는 %d이고 음수임' % a)