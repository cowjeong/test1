list = ['a', 'b', 'c']
with open('list.text', 'w') as f:
    f.write(list)       #에러 발생 리스트 안에 문자가 문자열이어야 함