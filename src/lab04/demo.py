from .models import *
#TypeError: Can't instantiate abstract class BachelorStudent without an implementation 
#for abstract methods 'admiss_university', 'pass_exam'
#ошибка если нет реализации метода

def admiss_in_univercity(students: list[Admissible]):
    for student in students:
        student.admiss_university()

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

print(student1)
print(student2)
print(student3)

student1.admiss_university()
student2.admiss_university()
student3.admiss_university()

student1.pass_exam("математика")
student1.pass_exam("физика")

student2.pass_exam('математика')
student2.pass_exam('физика')
student2.pass_exam('информатика')

student3.pass_exam('математика')

list_student = [student4,student5,student6]
admiss_in_univercity(list_student)


pass_math(student4)
pass_math(student5)
try:
    pass_math(5)
except TypeError as e:
    print(e)
    


