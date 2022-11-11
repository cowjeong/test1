import random as rd  
print(rd.random())  #0 이상 1 미만의 실수 반환 
print(rd.randint(1, 6))  #1 이상 6 이하의 임의의 정수를 반환
print(rd.randrange(1, 6))  #1 이상 6 미만의 임의의 정수를 반환
numlist = [10, 20, 30, 40, 50]
rd.shuffle(numlist)      #numlist의 원소를 임의로 섞음
print(numlist)
print(rd.choice(numlist))  #numlist의 원소 중에서 임의의 하나를 고름
print(rd.sample(numlist, 3))  #numlist의 원소 중에서 임의로 3개를 고름