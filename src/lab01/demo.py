from random import randint
from model import Student

# Создаём объекты
student1 = Student("Иванов", "Иван", 19, 2, 2.7)
student2 = Student("Петров", "Петр", 20, 3, 3.2)
student3 = Student("Сидорова", "Анна", 18, 1, 4.8)
student4 = Student("Иванов", "Иван", 19, 2, 2.7)

print("\n> Три экземпляра класса Student с разными параметрами")
print(student1) #вызывает __str__
print(student2)
print(student3)
print("--вызываем __repr__--")
print(repr(student3)) #вызывает __repr__


print("\n> Сравнение объектов, где вызываем __eq__")
if student1 == student2: #вызывает __eq__
    print(f"--{student1.surname} и {student2.surname} один и тот же студент")
else:
    print(f"-{student1.surname} и {student2.surname} разные студенты")

if student1 == student4: #вызывает __eq__
    print(f"-{student1.surname} и {student4.surname} один и тот же студент")
else:
    print(f"-{student1.surname} и {student4.surname} разные студенты")


print('\n> Обработка ошибок: фамилия передана как число')
try:
    student4 = Student(16, "Анна", 18, 1, 4.8)
except (ValueError, TypeError) as e:
    print(f"Студент не создался, потому что: {e}\n")

print('\n> Обработка ошибок: пустая фамилия')
student3.surname="Петрова"
try:
    student3.surname="" 
except (ValueError, TypeError) as e:
    print(f"Не удалось записать фамилию, потому что: {e}\n")


print("> Демонстрация атрибутов класса")
print(f"-Максимальный возраст (через класс):{Student.max_age}") #через класс
print(f"-Максимальный возраст (через экземпляр):{student1.max_age}") #через экземпляр


print("\n> Сценарий 1: Попытка перевода на следующий курс с проверкой GPA")
for i in range(4):
    try:
        if student2.chek_to_next_curse():
            student2.to_next_course()
            # Демонстрация сеттера с валидацией
            new_gpa = randint(3, 5)
            print(f"-Устанавливаем новый GPA: {new_gpa}")
            student2.gpa = new_gpa
            print(f"-Студент переведён на {student2.curse} курс, новый балл: {student2.gpa}\n")
        else:
            print(f"-Студент не может быть переведён (текущий GPA: {student2.gpa})")
    except ValueError as e:
        print(f"Ошибка: {e}")

    
print("\n> Сценарий 2: Попытка перевода студента с низким GPA")
print(f"-Студент: {student1}")
if student1.chek_to_next_curse():
    student1.to_next_course()
    print(f"-Студент {student1.surname} переведён на курс {student1.curse}\n")
else:
    print(f"-Студент {student1.surname} не прошёл проверку по среднему баллу {student1.gpa}")


print("\n> Сценарий 3: Демонстрация логического состояния (неактивный студент)")
print(f"-Исходное состояние: {student3.surname} активен")
student3.not_active()  # Изменение состояния
print(f"-После вызова not_active(): {student3.surname} неактивен(а)")
try:
    if student3.chek_to_next_curse():
        student3.to_next_course()
    else:
        print(f"-Студент {student3.surname} не может быть переведён (причина: неактивен)")
except ValueError as e:
    print(f"Ошибка при попытке перевода: {e}")


print("\n> Сценарий 4: Демонстрация изменения состояния обратно в активное")
print(f"-До активации: {student3}")
student3.active()  # Изменение состояния обратно
print(f"-После активации: {student3}")
if student3.chek_to_next_curse():
    student3.to_next_course()
    print(f"-Активный студент {student3.surname} может быть переведён")
else:
    print(f"-Студент {student3.surname} не прошёл проверку")


print("\n> Сценарий 5: Демонстрация работы метода to_collect_money()")
print(f"-Стипендия студента {student1.surname}: {student1.to_collect_money()} руб., так как его GPA {student1.gpa}")
print(f"-Стипендия студента {student2.surname}: {student2.to_collect_money()} руб., так как его GPA {student2.gpa}")
print(f"-Стипендия студента {student3.surname}: {student3.to_collect_money()} руб., так как его GPA {student3.gpa}")


print("\n> Сценарий 6: Демонстрация валидации через setter")
try:
    print("-Попытка установить GPA = 5.5 (выходит за пределы 0-5)")
    student2.gpa = 5.5
except ValueError as e:
    print(f"Ошибка валидации: {e}\n")

try:
    print("-Попытка установить возраст = 70 (выходит за пределы 16-60)")
    student2.age = 70
except ValueError as e:
    print(f"Ошибка валидации: {e}\n")

try:
    print("-Попытка установить курс = 7 (выходит за пределы 1-6)")
    student2.curse = 7
except ValueError as e:
    print(f"Ошибка валидации: {e}\n")
