#튜플의 + 연산#
T1=(2,5,7)
T2=(3,5,9)
T3=T1 + T2
print(T3)
T3=T2+T1
print(T3)
T3+=(11,13)
print(T3)

#튜플의 * 연산 #
T1=(2,5,7)
print(T1)
print(T1*2)

#튜플의 비교 연산 #
T1=(2,5,7)
T2=(2,5,6)
print(T1==T2)
print(T1<T2)
print(T1>T2)