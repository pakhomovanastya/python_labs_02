from .collection import StudentCollection
from lib.student import Student

def print_list_students(students):
    for st in students:
        print(st)

student1 = Student("Иванов", "Иван", 18, 2, 4.2)
student2 = Student("Прудникова", "Анна", 17, 1, 3)
student3 = Student("Петров", "Егор", 20, 6, 3.8)
student4 = Student("Сидорова", "Мария", 19, 2, 4.5)
student5 = Student("Иванов", "Петр", 22, 4, 4.0)
student6 = Student("Смирнов", "Алексей", 18, 6, 2)

print("> Добавление студентов в коллекцию")
student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)

print("\nсотрировка по фамилии")
student_collection.sort_by_surname()
student_collection.print_coll()

print("\nсотрировка по имени")
student_collection.sort_by_name()
student_collection.print_coll()

print("\nсотрировка по курсу")
student_collection.sort_by_curse()
student_collection.print_coll()

print("\nстуденты с 6-го курса")
def filter_last_curse(student):
    return student.curse == 6
last_curse = list(filter(filter_last_curse, student_collection))

print_list_students(last_curse)

print("\nсписок средногго блла студентов")
gpa = list(map(lambda st: st.gpa, student_collection))
print(gpa)

print("\nиспользование фабрики функций (лучшие студенты)")
def make_gpa_filter(min_gpa):
    def filter_min_gpa(st):
        return st.gpa > min_gpa
    return filter_min_gpa

f = make_gpa_filter(4)
list_better_gpa = list(filter(f, student_collection))
print_list_students(list_better_gpa)
    

print("\nфильтрация по совершеннолетним")
list_st_age = student_collection.filter_by(key = lambda st: st.age >= 18)
print_list_students(list_st_age)

print("\nфильтрация по совершеннолетним (через функцию)")
def filter_by_age(student):
    return student.age >= 18
list_st_age2 = student_collection.filter_by(key = filter_by_age)
print_list_students(list_st_age2)


