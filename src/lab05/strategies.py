class StrategyByName:
    """Стратегия: форматированный вывод информации о студенте по имени"""
    def __call__(self, student):
        """Применить стратегию к студенту, объект Student,
        возвращяет строку с именем студента"""
        return f"Студент {student.name}"

class StrategyByGPA:
    """Стратегия: форматированный вывод с информацией о среднем балле"""
    def __call__(self, student):
        """Применить стратегию к студенту, объект Student,
        возвращяет информацию о студенте и его GPA"""
        if student.gpa > 2.5:
            return f"Студент {student.surname} {student.name} - сред. балл {student.gpa}"
        return f"Студент {student.surname} {student.name} на грани отчислениея, так как его сред. балл {student.gpa}"

class StrategyByCurse:
    """Стратегия: форматированный вывод с информацией о курсе обучения"""
    def __call__(self, student):
        """Применить стратегию к студенту, объект Student,
        возвращяет информацию о студенте и его курсе"""
        if student.curse == 6:
            return f"Студент {student.surname} {student.name} на последнем курсе {student.curse}"
        return f"Студент {student.surname} {student.name} учится на {student.curse} курсе"
    
def print_list_students(students):
    """вывод списка студентов"""
    for i, st in enumerate(students, 1):
        print(f"  {i}. {st}")

def filter_last_curse(student):
    """Фильтр студенты последнего (6) курса,
    возвращяет True если студент на 6 курсе"""
    return student.curse == 6

def filter_first_curse(student):
    """Фильтр студенты первого курса,
    возвращяет True если студент на 1 курсе"""
    return student.curse == 1

def filter_by_age(student):
    """Фильтр совершеннолетние студенты (18+ лет),
    возвращяет True если студенту 18 лет или больше"""
    return student.age >= 18

def make_gpa_filter(min_gpa):
    """Фабрика функций создаёт фильтр по минимальному GPA.
    min_gpa: Минимальное значение среднего балла
    возвращяет функцию-предикат для фильтрации студентов"""
    def filter_min_gpa(st):
        return st.gpa > min_gpa
    return filter_min_gpa
