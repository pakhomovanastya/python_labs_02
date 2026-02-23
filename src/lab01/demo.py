from random import randint
from model import Student
student1 = Student("Иванов", "Иван", 19, 2, 2.7)
student2 = Student("Петров", "Петр", 20, 3, 3.2)
student3 = Student("Сидорова", "Анна", 18, 1, 4.8)


print("\n> три экземпляра класса Student с разными параметрами")
print(student1) #вызывает __str__
print(student2)
print(student3)
print(repr(student3)) #вызывает __repr__


print("\n> Сравнение объектов")
if student1 == student2: #вызывает __eq__
    print(f"один и тот же студент")
else:
    print(f"разные студенты")


print('\n> Обработка ошибок фамилия передана как число')
try:
    student4 = Student(16, "Анна", 18, 1, 4.8)
except (ValueError, TypeError) as e:
    print(f"студнт не создался, потому что {e}\n")

print('\n> Обработка ошибок фамилия пустая')
student3.surname="Петрова"
try:
    student3.surname="" 
except (ValueError, TypeError) as e:
    print(f"не удалость записать фамилию, потому что {e}\n")


print("> Демонстрация атрибутов класса")
print(f"максимальный возраст {Student.max_age}") #через класс
print(f"максимальный возраст {student1.max_age}") #через экземпляр


print("\n> первый сценарий работы")
for i in range(3):
    if student2.chek_to_next_curse():
        student2.to_next_course()
        student2.gpa=randint(3, 5)
try:
    if student2.chek_to_next_curse():
        student2.to_next_course()
except ValueError as e:
    print(f"{e}")
    
print("\n> второй сценарий работы")
if student1.chek_to_next_curse():
    student1.to_next_course()
else:
    print(f"студент {student1.surname} не прошёл прверку по среднему баллу {student1.gpa}")

    
print('\n> третий сценарий работы')
student3.not_active()
try:
    if student3.chek_to_next_curse():
        student3.to_next_course()
except ValueError as e:
    print(f"студент {student3.surname} оказался не активный ")
