class PythonSchool:
    def __init__(self, name, email, phone):
        self.name = name  
        self.email = email
        self.phone = phone
        
    def printStudent(self):
        print("이름: ", self.name)
        print("이메일: ", self.email)
        print("전화번호: ", self.phone)

    def __del__(self):
        print(self.name, "객체가 소멸되었습니다.")
    def __repr__(self):
        return self.name 
    
student1 = PythonSchool("Hong kildong", "hong1234@emai.net", "010-1234-5678")
student1.printStudent()
print(student1) #repr return 값인 self.name이 출력됨
del student1 