from lib.student import Student
from .models import BachelorStudent, MasterStudent, PhDStudent
from .base import StudentCollection

# Создание объектов разных типов
student1 = BachelorStudent("Petrov", "Nikita", 20, 3, 4, 5, 2)
student2 = MasterStudent("Ivanov", "Maxim", 23, 1, 4.5, "ВШЭ", 4.2)
student3 = PhDStudent("Nilitin", "Oleg", 28, 2, 5, "Космические технологии", 4)

print("\n--- Объекты разных типов")
print(f"  {student1.surname} {student1.surname}, {student1.curse}")
print(f"  {student2.surname} {student2.surname}, {student2.curse}")
print(f"  {student3.surname} {student3.surname}, {student3.curse}")

#Сценарий 1: Проверка условий поступления
print("\n-----Сценарий 1: проверка на поступление-----")
print("\n> Проверка бакалавра:")
try:
    if student1.cheak_gpa_certificate():
        print(f"- {student1.surname} зачислен на Бакалавриат")
except ValueError as e:
    print(e)

print("\n> Проверка магистра:")
try:
    if student2.chek_gpa_bachelor():
        print(f"- {student2.surname} зачислен в Магистратутру")
except ValueError as e:
    print(e)

print("\n> Проверка аспиранта:")
try:
    if student3.chek_count_publikations():
        print(f"- {student3.surname} зачислен в Аспирантуру")
except ValueError as e:
    print(e)

# Изменение состояния (отчисление)
student1.not_active() #метод делаем его не активным из базового класса
print(f"\n> Статус студента {student1.surname}: {'отчислен' if not student1.is_active else 'активен'}")


print("\n-----Сценарий 2: проверка типов и полиморфизм-----")
print(">Проверка типа через isinstance():")
if isinstance(student2, Student):
    print(f"- {student2.surname} - является студентом")
else:
    print(f"- {student2.surname} - не является студентом")

print("\n> Полиморфизм: расчёт стипендии для разных типов студентов")
print(f"- {student1.surname} бакалавр: {student1.to_collect_money()} руб.")
print(f"- {student2.surname} магистр: {student2.to_collect_money()} руб.")
print(f"- {student3.surname} аспирант: {student3.to_collect_money()} руб.")



print("\n-----Сценарий 3: работа с коллекцией-----")
student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)

print("> Все студенты в коллекции:")
for st in student_collection:
    print(f"- {st.surname}: стипендия: {st.to_collect_money()} руб.")

print("\n> Фильтрация: только активные студенты")
active_list = student_collection.get_active()
if active_list:
    for st in active_list:
        print(f"- {st.surname} ({type(st).__name__})")
else:
    print("- Активных студентов нет")

print("\n> Фильтрация по типу: только бакалавры")
bachelors = student_collection.get_by_type(BachelorStudent)
if bachelors:
    for st in bachelors:
        print(f"- {st.surname}")
else:
    print("- Бакалавров нет")