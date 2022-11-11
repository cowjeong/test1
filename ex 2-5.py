str9 = ' Computer Security '
#print(str9.replace('security', '보안'))
#print(str9.replace('t', 'T'))
#print(str9)
#print(str9.strip())
#print(str9.lstrip())
#print(str9.rstrip())
#print(str9.split())
#print(str9.splitlines())
#str10 = 'www.sungkyul.ac.kr'
#print(str10.split('.'))
#poem = '''우리들은 모두
#무엇이 되고 싶다.
#너는 나에게 나는 너에게
#잊혀지지 않는 하나의 눈짓이 되고 싶다'''
#print(poem.splitlines())
#print("$".join(str9))
#print(str9.isalpha())
#print(str9.isnumeric())
#print(str9.isalnum())
#a = '123'
#print(a.isalpha())
#print(a.isnumeric())
#print(a.isalnum())
#str11 = 'Department of {}'
#print(str11.format('Computer'))
#str12 = 'Department of {}  {}'
#print(str12.format('Computer', 'Engineering'))
#str13 = 'hello, {0} {1}'
#print(str13.format('Computer', 'Engineering'))
#str14 = 'hello, {str1} {str2}'
#print(str14.format(str1='컴퓨터', str2='공학과'))
str15 = 'Department of {:20}'
print(str15.format('Engineering') + '/')
str15 = 'Department of {:<20}'
#차지하는 공간내 왼쪽 정렬
print(str15.format('Engineering') + '/')
str15 = 'Department of {:>20}'
#차지하는 공간내 오른쪽 정렬
print(str15.format('Engineering') + '/')
str15 = 'Department of {:^20}'
#차지하는 공간내 가운데 정렬
print(str15.format('Engineering') + '/')
#차지하는 공간내 다른 문자열로 채움
str15 = 'Department of {:@<20}'
print(str15.format('Engineering') + '/')
str15 = 'Department of {:#>20}'
print(str15.format('Engineering') + '/')
str15 = 'Department of {:$^20}'
print(str15.format('Engineering') + '/')