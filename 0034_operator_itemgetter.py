from operator import itemgetter, attrgetter
students = [
    ('jane', 22, 'A'), ('dave', 32, 'B'), ('sally', 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(result)

result = sorted(students, key=itemgetter(2))
print(result)



class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B')
]

result = sorted(students, key=attrgetter('age'))
for item in result:
    print(f'name: {item.name} age: {item.age} grage: {item.grade}')