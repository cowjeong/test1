a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_lambda = list(map(lambda x: str(x) if x % 2 ==0 else x,a))
print(f'a = {a}')
print('a_lambda = ', a_lambda)

b_lambda = list(map(lambda x: str(x) if x == 1 else float(x) if x ==2 else x + 10, a))
print('b_lambda=', b_lambda)

def f(x) :
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

c_lambda = list(map(f, a))
print('c_lambda=', c_lambda)