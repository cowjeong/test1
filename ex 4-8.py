pocket = []
pocket.append(input('주머니에 있는 것은?(money, card, ...) : ')) 
if 'money' in pocket :
    print('택시 타고 가자~~~')
elif 'card' in pocket :
    print('모범택시 타고 가자^^')
else :
    print('걸어가야겠다 : ')
#print('포켓 안에 무엇이 들어 있을까요?', pocket)