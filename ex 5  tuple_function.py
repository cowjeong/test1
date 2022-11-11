# 튜플의 함수와 매소드
'''
#count
print('# count #')
a=(1,2,3,2,4,2,3,4,2)
print('a=',a)
print('a.count(2)=',a.count(2)) #튜플 내에서 요소 2의 갯수 반환
print()
'''
#index
print('# index #')
a=(1,4,3,2)
b=('s','t','r')
print('a=',a)
print('b=',b)
print('a.index(4)=',a.index(4)) #튜플 a에서 4의 인덱스값 반환
print('b.index(r)=',b.index('r')) #투플 b에서 요소 r의 인덱스값 반환
#print('a.index(0)=',a.index(0)) #튜플 a에서 요소 0의 인덱스값 반환
print()



#len
print('# len #')
print('a=',a)
print('len(a)=',len(a)) #튜플의 전체 길이를 반환

#
a=(1,4,3,2)
print('max(a)=',max(a))  #튜플의 최대값을 반환

#min
print('min(a)=',min(a)) #튜플의 최소값을 반환

#sum
print('sum(a)=',sum(a)) #튜플의 요소를 모두 더한 값을 반환
