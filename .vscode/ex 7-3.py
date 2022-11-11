class student:
    def __init__(self, name, email, phone):
        self.name = name  
        self.email = email
        self.phone = phone

    def to_print(self):
        return "{}\t{}\t{}".format( 
            self.name,
            self.email,
            self.phone )

students = [ 
    student("홍길동", "hong1234@email.net", "010-1234-5678"),
    student("김철수", "kim1234@email.net", "010- 3456-7890"),
    student("홍길동", "hong1234@email.net","010-2345-6789"),
    student("김철수", "kim1234@email.net", "010- 4567-7890")
]
print("이름", "email","phone", sep='\t\t')
print('-' * 50)

for student in students:
    print(student.to_print())