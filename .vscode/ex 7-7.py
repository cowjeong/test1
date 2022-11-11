class Stdunt:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return self.name != other.name
    def __gt__(self, other):
        return self.name > other.name 
    def __ge__(self, other):
        return self.name >= other.name
    def __lt__(self, other):
        return self.name < other.name
    def __le__(self, other):
        return self.name <= other.name

student = Stdunt("김철수", 23)

print(student == student)
print(student != student)
print(student > student)
print(student >= student)
print(student < student)
print(student <= student)