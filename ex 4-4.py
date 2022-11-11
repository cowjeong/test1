a = int(input('1에서 10 사이의 정수를 입력하세요: '))
if (a >= 0) :
    if(a == 0) :
      print('입력한 정수는 0임')
    else :
      print('입력한 정수는 %d이고 양수임' % a)
else :
    print('입력한 정수는 %d이고 음수임' % a)
  