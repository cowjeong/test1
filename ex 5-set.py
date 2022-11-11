'''
# 집합

set1={1,2,3,4,2,3,4,5,3,4,5,6,7,7,7,7,7}
print('set1=',set1)
#list1=['국어','영어','수학','영어','국어']
#print('list=',list1)
#print('set(list)=',set(list1))
#print(set1[0])
print()

#add
print('# add #')
set1.add(8)        #집합 set1에 원소 8을 추가 
print('set1=',set1)  
print()

#update
print('# update #')
set1.update([9,10]) #집합 set1에 원소 9,10을 추가
print('set1=',set1)
print()

#remove
print('# remove #')
set1.remove(7)          #집합 set1에서 원소 7을 삭제
print('set1=',set1)
#set1.remove(7)         #집합 set1에 삭제하라는 원소 7이 없으면 오류 발생
#print('set1=',set1)    
print()

# discard
print('# discard #')
set1.discard(7)            #집합 set1에서 원소 7을 삭제
print('set1=',set1)
print()

# clear
#print('# clear #')
#set1.clear()
#print('set1=',set1)
#print('set1=',set1.clear())
#print()

# in
print('# in #')
print('5 in set1 =', 5 in set1)
print('11 int set1=',11 in set1)


# set
print('# set #')
set1=set('python world') #문자열을 집합 set1으로 
print('str1=',set1)
print()

# range 
print('# range #')
set1=set(range(10))  #연속적인 숫자로 집합 set1을
print('set1=',set1)
print()
'''

# 집합의 연산자 - |, &, -
print('<집합의 연산자>')
set1={0,1,2,3,4,5}
set2={4,5,7,8,2,1}
print('# 합집합 #')
print('set1=',set1)
print('set2=',set2)
print('set1 | set2=',set1 | set2)
print('set.union(set1, set2)=',set.union(set1, set2))
print('\n# 교집합 #')
print('set1 & set2 =', set.intersection(set1, set2))
print('set.intersection(set1, set2)=',set.intersection(set1, set2))
print('\n# 차집합 #') 
print('set1-set2=',set1-set2)
print('set.difference(set1, set2)=',set.difference(set1, set2))
print('set2-set1=',set2-set1)
print('set.difference(set2, set1)=',set.difference(set2, set1))
print('\n # XOR연산 #')
print('set1 ^ set2 =', set1 ^set2)
print('set.symmetric_difference(set1, set2)=',set.symmetric_difference(set1, set2))