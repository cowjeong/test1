'''
# 튜플 #

T1=()
print('T1=',T1)

T2_i=(1)
print('T2_i=',T2_i)

T2=(1,)
print('T2=',T2)

print('type(T2=',type(T2))

print('type(T2_i=',type(T2_i))

T3=(1,2,3)
print('T3=',T3)

T4=4,5,6
print('T4=',T4)

T5=('a','b',('ab','cd'))
print('T5=',T5)
T6=T3+T4
print('T6=',T6)

#튜플은 요소 삭제 불가
#del T1[0]

#튜플과 리스트의 상호변환
tuple1=(1,2,3,4)
list1=list(tuple1)
list1.append(5)
print('tuple1=',tuple1)
print('list1=',list1)
tuple1=tuple(list1)
print('tuple1=',tuple1)
'''
#튜플과 리스트를 이요한 여러개의 변수를 한 번에 생성
a, b, c =[1, 2, 3]
a1, b1, c1=(11, 12, 13)
print('a=',a)
print('b=',b)
print('c=',c)
print('a1=',a1)
print('b1=',b1)
print('c1=',c1)