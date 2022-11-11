sum_even = 0             #짝수의 합
sum_odd = 0               #홀수의 합
for n in range (1, 101) : #1부터 100까지의 반복
    if n % 2 == 0:        #n이 짝수인 경우,
      sum_even += n
    else :                #n이 홀수인 경우,
        sum_odd += n
print('짝수의 합 = ', sum_even)
print('홀수의 합 = ', sum_odd)