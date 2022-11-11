# 딕셔너리의 함수와 매소드
'''
#del
print('# del #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'05/01','major':'컴퓨터공학'}
print('dic1=',dic1)
del(dic1['phone'])    #dic1의 phone의 값을 삭제
print('dic1=',dic1)
del dic1['name']     #dic1의 name의 값을 삭제
print('dic1=',dic1)
print() 

# pop
print('# pop #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'05/01','major':'컴퓨터공학'}
print('dic1=',dic1)
print("dic1.pop('name')=",dic1.pop('name'))   #dic1의 name의 값을 반환하고 삭제
print('dic1=',dic1)
print()

#popitem
print('# popitem #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'03-01','major':'컴퓨터공학'}
print('dic1=',dic1)
print('dic1.popitem()=',dic1.popitem())  #dic의 마지막 키-값 쌍을 반환하고 삭제
print('dic1.popitem()=',dic1.popitem())
print('dic1=',dic1)


#keys
print('# keys #')
print('dic1.keys()=',dic1.keys()) #딕셔너리의 key만을 모아서 dict_keys 객체를 반환
print()

# values
print('# values #')
print('dic1.values()=',dic1.values())  #딕셔너리의 value만을 모아서 dict_value 객체를 반환
print()

# items
print('# item #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'03-01','major':'컴퓨터공학'}
print('dic1.items()=',dic1.items())  #딕셔너리의 key의 value 쌍을 튜플로 묶은 값을 dict_items 객체로 반환
print()

# len
print('# len #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'03-01','major':'컴퓨터공학'}
print('len(dic1)=',len(dic1)) #딕셔너리 dic1의 키 개수(길이)를 반환
print()

# clear
print('# clear #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'03-01','major':'컴퓨터공학'}
dic1.clear()
print('dic1.clear=',dic1.clear()) #딕셔너리 dic1의 모든 요소를 삭제
print()

# get
print('# get #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'03-01','major':'컴퓨터공학'}
print("dic1.get('major')=",dic1.get('major')) #'major' key에 대응하는 value를 반환
print("dic1['major']=",dic1['major'])
print("dic1.get('grade')=",dic1.get('grade')) #'grade' key가 존재하지 않으므로 'None' 반환
#print("dic1['grade']=",dic1['grade'])        #'grade' key가 존재하지 않으므로 keyError 발생
print()
'''
# update
print('# update #')
dic1={'name':'홍길동','phone':'010-1234-5678','birth':'03-01','major':'컴퓨터공학'}
print('dic1=',dic1)
dic1.update({'name':'김청수','birth':'01/01','grade':'1','address':'Seoul'})
print('업데이트된 dic1=',dic1)
dic1.update(name='김영희',birth='12/25',grade='4')
print('업데이트된 dic1=',dic1)
print()

#pretty print, pprint()
from pprint import pprint as pp
pp(dic1)