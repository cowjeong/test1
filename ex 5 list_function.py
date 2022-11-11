'''
#append
print('# append #')
a=[1,2,3]
a.append(4)     #리스트  a의 뒤에 요소 4를 추가
print(a)
a.append([5,6])   #리스트 a의 뒤에 리스트 [5,6]을 추가 
print(a)
print()

#clear
print('# clear #')
print(a)
a.clear()
print(a)
print()

#copy
print('# copy #')
a=[1,2,3,2,3,4,2,3,4,2]
b=a.copy()          #리스트 a의 복사본을 b에 할당
print(b)
print()

c=list(a)       #리스트 a의 내용을 변수 c에 할당
print(c)
d=a            #리스트 a를 변수 d에 할당
print(d)
print()

# count
print('# count #')
a=[1,2,3,2,4,2,3,4,2]
print(a.count(2))   #리스트 a에 요소 2의 갯수를 반환
print()

# del 
print('# del #')
a=[1,2,3,4,5,6,7,8,9,10]
del a[1]           #리스트 a의 1번째 요소를 삭제
print(a)
del a[4:8]            #리스트 a의 4번째부터 7번째 요소 삭제
print(a)
print()

# extend
print('# extend #')
a=[1,4,3,2]
b=['s','t','r']
a.extend(b)
print(a)
print()

# index
print('# index #')
a=[1,4,3,2]
b=['s','t','r']
print(a.index(4))      #리스트 a의 요소 중 4의 인덱스값 반환
print(b.index('r'))   #리스트 b의 요소 중 r의 인덱스값 반환
#print(a.index(0))    #리스트 a의 요소 중 0의 인덱스값 반환 -->값 오류 발생
print()

#insert
print('# insert #')
a=[1,2,3]
print(a)
a.insert(1,4)   #리스트 a의 1번째 위치에 요소 4를 삽입
print(a) 
a.insert(3,5)  #리스트 a의 3번째 위치에 요소 5를 삽입
print(a)
print()

# pop
print('# pop #')
a=[1,2,3,4]
print(a.pop())   #리스트 a의 마지막 요소 반환 후 리스트에서 삭제 
print(a)
print(a.pop(1))  #리스트 a의 1번째 요소 반환 후 리스트에서 삭제
print(a)
print()

# remove
print('# remove #')
a=[1,2,3,4,1,2,3,4]
b=['s','t','r','s','t','r']
a.remove(4)    #리스트 a에서 첫번째로 나오는 4를 리스트에서 삭제
b.remove('r')  #리스트 b에서 첫번째로 나오는 r을 리스트에서 삭제
print(a)
print(b)
#a.remove(9)  #리스트 a에서 첫번째로 나오는 9를 리스트에서 삭제-->값 오류
print()

print('#del와 index로 remove 효과')
a=[1,2,3,4,5,6,7]
print(a)
del a[a.index(3)]  #a.index(3)--> 2, del a[2]
print(a)  

# reverse
print('# reverse #')
a=[1,4,3,2]
b=['s','t','r']
print(a)
a.reverse()   #리스트 a의 요소를 역순으로 정렬
print(a)
print(b)
b.reverse()   #리스트b의요소를 역순으로 정렬
print(b)
print()

#sort
print('# sort #')
a=[1,4,3,2]
b=['s','t','r']
print(a)
a.sort()   #리스트 a의 요소를 오름차순으로 정렬
print(a)
print(b)
b.sort()  #리스트 b의 요소를 오름차순으로 정렬
print(b)
print()

# 내림차순으로 정렬
a.sort(reverse=True)
print(a)
print()

#정렬하여 복사
a=[1,4,3,2]
c=sorted(a)
print('a=',a)
print('c=',c)
print()

#문자열을 리스트로 만든 후 요소의 길이 순으로 정렬
a='나는 파이썬 프로그래밍을 잘할 수 있다'
a=a.split()
print(a)
a.sort(key=len)  #리스트 a의 요소를 길이 순으로 오름차순 정렬
print(a)
print()

#리스트에서 sort()를 적용하려면 요소의 자료형이 같아야 함
a=[2020,3.14,True,'문자열']
a.sort()
print(a)
'''
a=[1,4,3,2]
print(3 in[1,4,3,2])
print(3 in a)
print(5 in a)
print(5 not in a)
