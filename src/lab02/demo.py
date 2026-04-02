from .collection import StudentCollection
from lib.student import Student

student1 = Student("Иванов", "Иван", 18, 2, 4.2)
student2 = Student("Прудникова", "Анна", 17, 1, 3)
student3 = Student("Петров", "Егор", 20, 3, 3.8)
student4 = Student("Сидорова", "Мария", 19, 2, 4.5)
student5 = Student("Иванов", "Петр", 22, 4, 4.0)
student6 = Student("Смирнов", "Алексей", 18, 1, 2)

print("> Добавление студентов в коллекцию")
student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)
for st in student_collection:
    print(f"   {st.surname} {st.name}, курс {st.curse}")
print(f"Добавлено {len(student_collection)} студентов")


print("\n> Коллекция после удаления студента")
print(f"Удаляем: {student2.surname} {student2.name}, курс {student2.curse}")
student_collection.remove(student2)
for st in student_collection:
    print(f"   {st.surname} {st.name}, курс {st.curse}")
print(f"В коллекции осталось {len(student_collection)} студентов")

print("\n> Поиск студента по фамилии 'Иванов'")
find_ivanov = student_collection.find_by_surname("Иванов")
for ivan in find_ivanov:
    print(f"   {ivan.surname} {ivan.name}, курс {ivan.curse}")
print("\n> Поиск студента по курсу (2 курс)")
find_cours2 = student_collection.find_by_course(2)
for course in find_cours2:
    print(f"   {course.surname} {course.name}, курс {course.curse}")


print("\n > Обход коллекции с помощью iterator")
print(f"Всего студентов: {len(student_collection)}")
for i, student in enumerate(student_collection, 1):
    print(f"  {i}. {student.surname} {student.name}, {student.curse} курс, GPA: {student.gpa}")

print("\n> Проверка ошибки на добавление дубликата")
try:
    student_collection.add(student1)
    print("Ошибка: дубликат был добавлен!")
except ValueError as e:
    print(f"Дубликат не добавлен так как: {e}")


#1 сценарий
print("\n---Сценарий 1: отчисление студента и фильтрация активных студентов")
#отчисляем последнего студента
last_student = student_collection[len(student_collection)-1]
print(f"1) Отчисляем студента: {last_student.surname} {last_student.name}")
last_student.not_active()
print(f"   Статус студента: {'отчислен' if not last_student.is_active else 'активен'}")

#получаем коллекцию только активных студентов
active_students = student_collection.get_active()
print(f"\n2) Активных студентов осталось: {len(active_students)} из {len(student_collection)}")

print("\n3) Список активных студентов:")
for student in active_students:
    print(f"   {student.surname} {student.name}, курс {student.curse}")



#2 сценарий
print("\n---Сценарий 2: сортировка коллекции")
print("1) Сортировка по фамилии (алфавитный порядок):")
active_students.sort(key=lambda st: st.surname)
for student in active_students:
    print(f"   {student.surname} {student.name}, курс {student.curse}")

print("\n2) Сортировка по курсу (от 1 до 6):")
active_students.sort(key=lambda st: st.curse)
for student in active_students:
    print(f"   {student.surname} {student.name}, курс {student.curse}")

print("\n3) Сортировка по среднему баллу (от высокого к низкому):")
active_students.sort(key=lambda st: -st.gpa)
for student in active_students:
    print(f"   {student.surname} {student.name}, курс {student.curse}")



#3 сценарий
print("\n---Сценарий 3: Индексация и изменение состояния")
print(f"1) Доступ к первому студенту через индекс [0]:")
first_student = student_collection[0]
print(f"   {first_student.surname} {first_student.name}, статус: {'активен' if first_student.is_active else 'отчислен'}")

print(f"\n2) Изменяем статус студента на 'отчислен':")
first_student.not_active()
print(f"   {first_student.surname} {first_student.name}, статус: {'активен' if first_student.is_active else 'отчислен'}")

print(f"\n3) Получаем обновленный список активных студентов:")
activ_students = student_collection.get_active()
print(f"Активных студентов: {len(activ_students)}")
for student in activ_students:
    print(f"   {student.surname} {student.name}, {student.curse} курс")