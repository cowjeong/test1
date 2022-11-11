score = int(input('점수를 입력하세요 : '))
if score >= 90 :
    grade = 'A'
elif score >= 80:
    grade = 'B'   
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if score == 100 :
    grade += '+'
elif score > 60 :
    if (score % 10 >= 5) :
        grade += '+'
print('{0}학점은 "{1}" 학점입니다.'.format(score, grade))