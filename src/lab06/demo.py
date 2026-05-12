from .container import TypeCollection, Scorable, Displayable
from lab01.model import Student
from lab03.models import BachelorStudent, MasterStudent, PhDStudent


student_collection: TypeCollection[Student] = TypeCollection()

student1 = Student("Иванов", "Иван", 18, 2, 4.2)
student2 = Student("Прудникова", "Анна", 17, 1, 3)
student3 = Student("Петров", "Егор", 20, 6, 3.8)
student4 = Student("Сидорова", "Мария", 19, 2, 4.5)
student5 = Student("Иванов", "Петр", 22, 4, 4.0)
student6 = Student("Смирнов", "Алексей", 18, 6, 2)

#Добавление студентов в коллекцию
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)

displayable_coll: TypeCollection[Displayable] = TypeCollection()

scorable_coll: TypeCollection[Scorable] = TypeCollection()

bachelor = BachelorStudent("Соколов", "Дмитрий", 20, 2, 4.2, 4.5, 1)
master = MasterStudent("Козлова", "Елена", 24, 1, 4.7, "МГУ", 4.5)
phd = PhDStudent("Морозов", "Андрей", 28, 2, 4.9, "Искусственный интеллект", 15)

#Добавляем объекты разных типов
displayable_coll.add(student1)      # Student
displayable_coll.add(bachelor)      # BachelorStudent
displayable_coll.add(master)        # MasterStudent
displayable_coll.add(phd)  

scorable_coll.add(student1)      # Student (есть score())
scorable_coll.add(bachelor)      # BachelorStudent
scorable_coll.add(master)        # MasterStudent
scorable_coll.add(phd)           # PhDStudent


# try:
#     student_collection.add(1357)
# except:
#     print("TypeError")

print("\n---Сценарий 1: TypeCollection[Student] типизированная коллекция---")

print("\n> Список всех студентов:")
all_st = student_collection.get_all()
for st in all_st:
    print(f"- {st.surname} {st.name}, курс {st.curse}, GPA: {st.gpa}")

print(f"\n> Добавлено {len(all_st)} студентов")


print("\n---Сценарий 2: методы find, filter, map---")
#метод find
#поиск сущ студента
print("\n> Метод find")
found_st = student_collection.find(lambda st: st.surname == "Иванов")
if found_st:
    print(f"\n1) Найден студент: {found_st.surname} {found_st.name}")

#поиск не сущ студента 
not_found_st = student_collection.find(lambda st: st.surname == "Сидоров")
if not_found_st is None:
    print(f"\n2) Студент с такой фамилией не найден")
else:
    print(f"\n2) Найден студент: {not_found_st.surname} {not_found_st.name}")

#метод filter
#фильтр студентов с GPA > 4
print("\n> Метод filter")
good_students_gpa = student_collection.filter(lambda st: st.gpa > 4)
print(f"\n1) Студенты с GPA > 4")
for st in good_students_gpa:
    print(f"- студент {st.surname} {st.name}, его сред. балл: {st.gpa}")

#фильтр студентов 6-го курса
last_curse = student_collection.filter(lambda st: st.curse == 6)
print(f"\n2) Студенты 6-го курса")
for st in last_curse:
    print(f"- студент {st.surname} {st.name} учится на {st.curse} курсе")


print("\n> Метод map")
# map: Student -> str (фамилия и имя)
names: list[str] = student_collection.map(lambda st: f"{st.surname} {st.name}")
print("\n1)  Список ФИО (list[str]):")
for name in names:
    print(f"- {name}")

# map: Student float (только GPA)
gpa_list: list[float] = student_collection.map(lambda st: st.gpa)
print(f"\n2) Список GPA (list[float]):")
for gpa in gpa_list:
    print(f"- {gpa}")

print(f"\n---Сценарий 3: Protocol Displayable с display()---")
print("\n> Вызов метода display() для каждого объекта (полиморфизм через Protocol)3""")
for item in displayable_coll:
    print(f"- {item.display()}\n")

print("\n> Использование map с display():")
display_strings = displayable_coll.map(lambda st: st.display())
for st in display_strings:
    print(f"- {st}\n")


print("\n---Сценарий 4: Protocol Scorable — коллекция с числовым рейтингом---")
print("\n> Список оценок (score) всех студентов:")
scores = scorable_coll.map(lambda st: st.score())
for st, score in zip(scorable_coll, scores):
    print(f"- {st.surname} {st.name}: {score}")