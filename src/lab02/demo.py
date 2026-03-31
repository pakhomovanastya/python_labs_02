from .collection import StudentCollection
from ..lib.student import Student

student1 = Student("Иванов", "Иван", 18, 2, 4.2)
student2 = Student("Прудникова", "Анна", 17, 1, 3)
student3 = Student("Петров", "Егор", 20, 3, 3.8)
student4 = Student("Сидорова", "Мария", 19, 2, 4.5)
student5 = Student("Иванов", "Петр", 22, 4, 4.0)
student6 = Student("Смирнов", "Алексей", 18, 1, 2)

print("> добавление студентов в коллекцию")
student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)
print(student_collection)

print("\n> коллекция после удаления студента")
student_collection.remove(student2)
print(student_collection)

print("\n> поиск студента по фамилии")
find_ivanov = student_collection.find_by_surname("Иванов")
for ivan in find_ivanov:
    print(f"{ivan.surname} {ivan.name}, курс {ivan.curse}")
print("\n> поиск студента по курсу")
find_cours2 = student_collection.find_by_course(2)
for course in find_cours2:
    print(f"{course.surname} {course.name}, курс {course.curse}")


print(f"\n> количество студентов в коллекции {len(student_collection)}:")
for student in student_collection:
    print(student)


try:
    student_collection.add(student1)
except ValueError as e:
    print(e)

#1 сценарий
print("\n---сценарий 1: отчисление студента и фильтрация---")
#отчисляем последнего студента
last_student = student_collection[len(student_collection)-1]
print(f"1) отчисляем студента: {last_student.surname} {last_student.name}")
last_student.not_active()
#получаем коллекцию только активных студентов
activ_st = student_collection.get_active()
print(f"2) активных студентов осталось: {len(activ_st)}")
print("3) список активных студентов:")
for student in activ_st:
    print(f"{student.surname} {student.name}, курс {student.curse}")

#2 сценарий
print("\n---сценарий 2: сортировка студентов---")
print("1) сортировка по фамилии")
activ_st.sort(key=lambda st: st.surname)
for student in activ_st:
    print(f"{student.surname} {student.name}, курс {student.curse}")

print("2)сортировка по курсу")
activ_st.sort(key=lambda st: st.curse)
for student in activ_st:
    print(f"{student.surname} {student.name}, курс {student.curse}")

#3 сценарий
print('\n---сценарий три')
print("1) достаем первого студента")
st1 = student_collection[0]
print(st1)
print("2) делаем его неактивным")
st1.not_active()
print(st1.is_active)
print("3) получаем всех активных студентов")
activ_students = student_collection.get_active()
print(activ_students)