class Registration:
    regi_num = 0
    def __init__(self, name):
        self.name = name 
        Registration.regi_num += 1
    def __del__(self):
        Registration.regi_num -= 1

student1 = Registration("홍길동")
student2 = Registration("김철수")

print(student1.name)
print(student2.name)
print(Registration.regi_num) #책에는 빠져있는 문장
del student1
print("수강신청 철회한 학생이 발생한 이후의 등록학생 수: ", (Registration.regi_num))