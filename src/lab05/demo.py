from .collection import StudentCollection
from lib.student import Student
from .strategies import *


student1 = Student("Иванов", "Иван", 18, 2, 4.2)
student2 = Student("Прудникова", "Анна", 17, 1, 3)
student3 = Student("Петров", "Егор", 20, 6, 3.8)
student4 = Student("Сидорова", "Мария", 19, 2, 4.5)
student5 = Student("Иванов", "Петр", 22, 4, 4.0)
student6 = Student("Смирнов", "Алексей", 18, 6, 2)

student_collection = StudentCollection()
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)



print("\n---Сценарий 1: сортировка коллекции---")

print("\n1) сотрировка по фамилии (алфавитный порядок)")
sort_surname = student_collection.sort_by_surname()
sort_surname.print_coll()

print("\n2)сотрировка по имени (алфавитный порядок)")
sort_name = student_collection.sort_by_name()
sort_name.print_coll()

print("\n3) сотрировка по курсу (от 1 до 6)")
sort_curse = student_collection.sort_by_curse()
sort_curse.print_coll()

print("\n4) Сортировка по среднему баллу")
sort_gpa = student_collection.sort_by_gpa()
sort_gpa.print_coll()


print("\n---Сценарий 2: фильтрация коллекции предикатами---")

print("\n1) студенты с 6-го курса (фильтр и именованную функцию)")
last_curse = list(filter(filter_last_curse, student_collection))
print_list_students(last_curse)

print("\n2) студенты с 1-го курса (фильтр filter_first_curse)")
first_curse = list(filter(filter_first_curse, student_collection))
print_list_students(first_curse)

print("\n3) фильтрация по совершеннолетним (через lambda)")
coll_st_age = student_collection.filter_by(key = lambda st: st.age >= 18)
print_list_students(coll_st_age)

print("\n4) фильтрация по совершеннолетним (через функцию filter_by_age)")
coll_st_age2 = student_collection.filter_by(key = filter_by_age)
print_list_students(coll_st_age2)


print("\n---Сценарий 3: map, lambda и фабрика функций---")

print("\n1) список средногго балла студентов (через map и lambda)")
gpa_list = list(map(lambda st: st.gpa, student_collection))
print(f"> GPA: {gpa_list}")

print("\n2) лучшие студенты (GPA > 4) через фабрику функций")
gpa_filter = make_gpa_filter(4)
best_students = list(filter(gpa_filter, student_collection))
print_list_students(best_students)
    

print("\n---Сценарий 4: паттерн стратегия через callable-объекты---\n   Цепочки операций над коллекцией")

print("\n> Стратегия 1")
print("- Цепочка: фильтр(6 курс) → сортировка(по фамилии) → стратегия(о курсе)")
resurlt = student_collection.filter_by(filter_last_curse).sort_by_surname().apply(StrategyByCurse())
print_list_students(resurlt)

print("\n> Стратегия 2")
print("- Цепочка с другой стратегией (StrategyByName)")
resalt02 = student_collection.filter_by(filter_last_curse).sort_by_surname().apply(StrategyByName())
print_list_students(resalt02)

print("\n> Стратегия 3")
print("- Стратегия StrategyByGPA (информация о GPA):")
resalt03 = student_collection.apply(StrategyByGPA())
print_list_students(resalt03)
