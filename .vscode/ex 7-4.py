class PythonSchool:
    def __init__(self, name, email, phone):
        self.name = name  
        self.email = email
        self.phone = phone
    def printStud(self):
        print("이름: ", self.name)
        print("이메일: ", self.email)
        print("전화번호: ", self.phone)

    def __del__(self):
        print(self.name, "객체가 소멸되었습니다.")

student1 = PythonSchool("Hong kildong", "hong1234@emai.net", "010-1234-5678")
print(type(student1))
student1.printStud()
del student1 
# student1.printStud() 에러 발생 