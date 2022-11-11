score = int(input('점수를 입력하세요 : '))
if (score >= 95) and (score <= 100) :
    grade = 'A+'
elif score >= 90 :
    grade = 'A'
elif score >= 85 :
    grade = 'B+'
elif score >= 80:
    grade = 'B'
elif score >= 75:
    grade = 'C+'   
elif score >= 70 :
    grade = 'C'
elif score >= 65:
    grade = 'D+'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if score > 100 or score < 0 :
    print('점수는 0에서 100까지 입력해야합니다')
print('{0}학점은 "{1}" 학점입니다.'.format(score, grade))