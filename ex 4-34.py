while True:
    num = int(input('정수를 입력하시오(0은 종료) :'))
    if not num :
        break         #반복문을 탈출합니다
    if num < 0:
        print('양의 정수를 입력하시오 \n')
        continue      #반복문의 처음으로 갑니다
    count = 0 #약수의 개수를 세어줄 변수
    for i in range(1, num+1):
        if num % i == 0: #나누어지면 약수
         print('{0:5}'.format(i), end=' ')
         count += 1
    print()
    print('{0}의 약수의 개수는 {1}개 입니다.\n'.format(num, count))