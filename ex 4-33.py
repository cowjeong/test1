while True:
    num = int(input('점수를 입력하세요(음수는 종료) : '))
    if num < 0 :
        break 
    if num > 100 :
        print('올바른 점수가 아닙니다.\n 0~100사이의 점수를 입력하세요\n')
        continue #반복문의 처음으로 가라!!

    #학점구하기
    if num >= 90:
        grade = 'A'
    elif num >= 80 :
        grade = 'B'
    elif num >= 70 :
        grade = 'C'
    elif num >= 60 :
        grade = 'D'
    else :
        grade = 'F'
    if num == 100:
        grade += '+' #grade = grade + '-' -> A+
    elif num > 60 :
        if (num % 10 >= 5) :
            grade += '+'
    print('{0}점의 학점은"{1}"입니다\n'.format(num, grade))