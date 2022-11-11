#reduce()를 사용하지 않는 경우
product1 = 1
list = [1, 2, 3,4]
for num in list :
    product1 = product1 * num
print('product1 = ', product1)

#reduce()를 사용하는 경우
#리스트에 있는 원소들을 누적적으로 함수에 적용한 후 반환
from functools import reduce
product2 = reduce((lambda x, y: x * y),[1, 2, 3, 4])
print('product2 = ', product2)