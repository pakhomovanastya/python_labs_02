from .models import *
#TypeError: Can't instantiate abstract class BachelorStudent without an implementation 
#for abstract methods 'admiss_university', 'pass_exam'
#ошибка если нет реализации метода

def admiss_in_univercity(students: list[Admissible]):
    for student in students:
        student.admiss_university()

#проверка что не является другим типом, тогда сдаём математику
def pass_math(student: PassableExam):
    if not isinstance(student, PassableExam):
        raise TypeError ("студент не может сдать экзамен")
    student.pass_exam("математика")


student1 = BachelorStudent("Petrov", "Nikita", 20, 3, 4, 5, 2)
student2 = MasterStudent("Ivanov", "Maxim", 23, 1, 4.5, "ВШЭ", 4.2)
student3 = PhDStudent("Nilitin", "Oleg", 28, 2, 5, "Космические технологии", 4)
student4 = BachelorStudent("Sidoriv", "Ivan", 19, 2, 4.5, 4.3, 1)
student5 = MasterStudent("Ptudnikov", "Sergey", 22, 2, 4.1, "МГУ", 4.4)
student6 = PhDStudent("Petrova", "Olga", 25, 2, 4.3, "История и философия", 2)

print("\n---Сценарий 1: данные о студентах и методы интерфейсов---")
print('>Данные о студенте')
print(student1)
print(student2)
print(student3)

print("\n> Поступление в университет (Admissible.admiss_university):")
student1.admiss_university()
student2.admiss_university()
student3.admiss_university()


print("\n> Сдача экзаменов (PassableExam.pass_exam):")
print("---Бакалавр:")
student1.pass_exam("- математика")
student1.pass_exam("- физика")

print("---Магистр:")
student2.pass_exam("- математика")
student2.pass_exam("- физика")
student2.pass_exam("- информатика")

print("---Аспирант (переопределённый pass_exam):")
student3.pass_exam("- математике")

print("\n---Сценарий 2: полиморфизм через интерфейсы---")
list_student = [student4,student5,student6]
admiss_in_univercity(list_student)

print("\n> Сдача математики через pass_math")
pass_math(student4)
pass_math(student5)

print("\n> Попытка передать в pass_math не студента")
try:
    pass_math(5)
except TypeError as e:
    print(f"Ошибка: {e}")


print("\n> Проверка isinstance для интерфейсов:")
print(f"- student4 (бакалавр): {isinstance(student4, PassableExam)}")
print(f"- student5 (магистр): {isinstance(student5, Admissible)}")
print(f"- student6 (аспирант): {isinstance(student6, DefendableDissertation)}")


print("\n---Сценарий 3: коллекция и фильтрация по интерфейсу---")
student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)


print("\n> Фильтрация по типу (только бакалавры):")
list_bachelor = student_collection.get_by_type(BachelorStudent)
for st in list_bachelor:
    print(f"{st.surname} {st.name}")


print("\n> Фильтрация по интерфейсу DefendableDissertation (аспиранты):")
list_pass_dissertation = student_collection.get_student_dissertation()
for st in list_pass_dissertation:
    print(f"{st.surname} {st.name}")


print("\n> Список сдающих диссертацию")
for student in list_pass_dissertation:
    print(student)

