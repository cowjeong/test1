def add(n, m) :
    return n + m
print('add함수:', add(2, 5))

#람다함수로 작성 
print('lambda함수:', (lambda n, m: n + m)(2, 5))

#라다함수는 매개변수를 여러개 가질 수 있지만 반환값은 한개만 