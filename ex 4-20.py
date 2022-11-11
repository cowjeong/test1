score = [90, 25, 67, 45, 80]
number = 0
for s in score:
    number = number + 1
    if s < 60:
        continue
    print("%d번의 학생 %d점으로 합격입니다. 축하합니다" % (number, s))