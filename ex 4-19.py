score = [90, 25, 67, 45, 80]
number = 0
for s in score:
    number = number + 1
    if s>= 60:
        print("%d반 학생의 점수는 %d이며 합격입니다." % (number, s))
    else:
        print("%d번의 학생의 점수는 %d이며 불합격입니다." % (number, s))
        