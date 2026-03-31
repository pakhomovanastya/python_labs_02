from lib.student import Student
from .models import BachelorStudent, MasterStudent, PhDStudent
from .base import StudentCollection

student1 = BachelorStudent("Petrov", "Nikita", 20, 3, 4, 5, 2)
student2 = MasterStudent("Ivanov", "Maxim", 23, 1, 4.5, "ВШЭ", 4.2)
student3 = PhDStudent("Nilitin", "Oleg", 28, 2, 5, "Космические технологии", 4)

print(student1)
print(student2)
print(student3)

print("---проверки на поступление")
try:
    if student1.cheak_gpa_certificate():
        print(f"{student1.surname} зачислин на Бакалавриат")
except ValueError as e:
    print(e)

try:
    if student2.chek_gpa_bachelor():
        print(f"{student2.surname} зачислин на Магистратутру")
except ValueError as e:
    print(e)


try:
    if student3.chek_count_publikations():
        print(f"{student3.surname} зачислен в Аспирантуру")
except ValueError as e:
    print(e)

student1.not_active() #метод делаем его не активным из базового класса

print("---проверка типа студента")
if isinstance(student2, Student):
    print(f"{student2.surname} - является студентом")
else:
    print(f"{student2.surname} - не является студентом")

print("---стипендия для студентов")
print(student1.to_collect_money())
print(student2.to_collect_money())
print(student3.to_collect_money())

print("---создание коллекции")
student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
for st in student_collection:
    print(f"{st},\n {st.to_collect_money()}")

print("---получение активных")
for st in student_collection.get_active():
    print(st)

print("---фильтрация по бакалаврам")
for st in student_collection.get_by_type(BachelorStudent):
    print(st)

