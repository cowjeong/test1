from functools import reduce #reduce()함수를 쓸 땐 정의 해줘야함
def cube(y) :
    return y * y * y

g = lambda x: x * x * x
print('print(g(7)) = ', g(7))
print('print(cube(5)) = ', cube(5))

#lambda()함수와 함께 사용한 filter()함수
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print('li = ', li)
final_list_filter = list(filter(lambda x: (x % 2 != 0),li))
print('print(final_list_filter) =', final_list_filter)

#lambda()함수와 함께 사용한 map()함수
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list_map = list(map(lambda x: x*2, li))
print('print(final_list_map) = ', final_list_map)

#lambda()함수와 함께 사용한 reduce()함수
li = [5, 8, 10, 20 , 50, 100]
sum = reduce((lambda x, y: x + y), li)
print('print(sum)=', sum)

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print('print(product) = ', product)

string = reduce(lambda x, y: y + x, 'abcde')
print('print(string)= ', string)