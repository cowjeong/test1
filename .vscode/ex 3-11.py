a = int(input('숫자를 입력하세요: '))
print()
print('a = ', a, ":", bin(a))
print('---- < left shift > -----')
a = a << 1 # * 2
print('a << 1 = ', a, ":", bin(a))
a = a << 2 # * 4
print('a << 2 = ', a, ":", bin(a))
a = a << 3 # 2 ** 3
print('a << 3 = ', a, bin(a))
print()
print('---- < right shift > ----')
a = a >> 1 # / 2
print('a >> 1 = ', a, ":", bin(a))
a = a >> 2 # / 2
print('a >> 2 = ', a, ":", bin(a))
a = a >> 3 # / 2
print('a >> 3 = ', a, ":", bin(a))