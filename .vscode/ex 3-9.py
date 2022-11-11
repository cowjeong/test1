year = int(input('연도를 입력하세요: '))
print(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))