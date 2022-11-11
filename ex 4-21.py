score = [25, 90, 67, 45, 80]
number = 0
for s in score:
    number = number + 1
    if s >= 60:
        print('%d번 학생 축하합니다. 합격입니다.' % number)
        break