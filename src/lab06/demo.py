from .container import TypeCollection
from lab01.model import Student

student1 = Student("Иванов", "Иван", 18, 2, 4.2)
student2 = Student("Прудникова", "Анна", 17, 1, 3)
student3 = Student("Петров", "Егор", 20, 6, 3.8)
student4 = Student("Сидорова", "Мария", 19, 2, 4.5)
student5 = Student("Иванов", "Петр", 22, 4, 4.0)
student6 = Student("Смирнов", "Алексей", 18, 6, 2)

print("> Добавление студентов в коллекцию")
student_collection: TypeCollection[Student] = TypeCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)

# try:
#     student_collection.add(1357)
# except:
#     print("TypeError")

all_st = student_collection.get_all()
for st in all_st:
    print(st)

