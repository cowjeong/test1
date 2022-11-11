a = int(input('첫번째 수를 입력하세요: '))
b = int(input('두번쨰 수를 입력하세요: '))
print('-' * 30)
print('두 개의 숫자를 교환하기\n')
print('a={0}, b={1}'.format(a,b))
print('-' * 30)
print('임시변수를 사용하는 방법\n')
temp = a
a = b
b = temp
print('a={0}, b={1}'.format(a,b))
print('-' * 30)
print('^(xor) 연산자를 이용하는 방법\n')
print('a = ', a, ":", bin(a))
print('b = ', b, ":", bin(b), '\n')
a = a ^ b 
print('a = a ^ b = ', a, ":", bin(a))
b = a ^ b
print('b = a ^ b = ', b,":", bin(b))
a = a ^ b
print('a = a ^ b = ', a, ":", bin(a), '\n')
print('a={0}, b={1}'.format(a,b))