class student:
    def __init__(self, name):
        self.name = name

student1 = student("홍길동")
student2 = student("김철수")
print("인스턴스 student1의 이름 = ", student1.name)
print("인스턴스 student2의 이름 = ", student2.name)

print("인스턴스 student1의 타입 = ", type(student1))
print("인스턴스 student2의 타입 = ", type(student2))

student3 = student("김소정")
print("인스턴스 student3의 이름 = ", student3.name)
print("인스턴스 student3의 타입 = ", type(student3))