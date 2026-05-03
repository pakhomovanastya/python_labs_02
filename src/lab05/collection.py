from lib.student import Student

class StudentCollection:
    """коллекция для хранения и управления объектами Student"""
    def __init__(self):
        """инициализация пустой коллекции"""
        self._students = []

    def _check_type(self, student):
        """проверка типа добавляемого объекта"""
        if not isinstance(student, Student):
            raise TypeError(f"Ожидается объект Student, получен {type(student)}")
        
    #методы
    def add(self, student):
        """добавить судента"""
        self._check_type(student)
        if student in self._students:
            raise ValueError("студент уже был добавлен")
        self._students.append(student)

    def remove(self, student):
        """удалить студента"""
        self._check_type(student)
        self._students.remove(student)

    def remove_at(self, index):
        """удалить студента по индексу и вернуть его"""
        if 0 <= index < len(self._students):
            return self._students.pop(index)
        raise IndexError(f"индекс не попадает в диапазон от 0 до {len(self._students)}")

    def get_all(self):
        """возвращяет список студентов"""
        return self._students
    
    #методы сортировки
    def sort_by(self, key):
        """универсальная сортировка по ключу
        key - функция, возвращающая значение для сравнения
        sort_by(lambda st: st.name)"""
        resalt = StudentCollection()
        sort_list = sorted(self._students, key=key)
        for st in sort_list:
            resalt.add(st)
        return resalt

    def sort_by_name(self):
        """сортировка по имении (вызываем верхний метод с лямбдой)"""
        return self.sort_by(key=lambda st: st.name)
        
    def sort_by_surname(self):
        """сортировка по имении (вызываем верхний метод с лямбдой)"""
        return self.sort_by(key=lambda st: st.surname)
    
    def sort_by_curse(self):
        """сортировка по курсу (вызываем верхний метод с лямбдой)"""
        return self.sort_by(key=lambda st: st.curse)
    
    def sort_by_gpa(self):
        """сортировка по среднему баллу (вызываем верхний метод с лямбдой)"""
        return self.sort_by(key=lambda st: st.gpa)
    
    #методы фильтрации
    def filter_by(self, key):
        """фильтрация коллекции по условию-предикату
        функция, возвращающая True/False для каждого студента
        результатом будет новая коллекция с отфильтрованными студентами"""
        resalt = StudentCollection()
        list_filter = list(filter(key, self))
        for st in list_filter:
            resalt.add(st)
        return resalt

    #методы поиска
    def find_by_surname(self, surname):
        """поиск по фамилии"""
        result_surname = []
        for st in self._students:
            if st.surname == surname:
                result_surname.append(st)
        return result_surname
    
    def find_by_course(self, course):
        """поиск по курсу"""
        result_course = []
        for c in self._students:
            if c.curse == course:
                result_course.append(c)
        return result_course
    
    #методы фильтрации по состоянию
    def get_active(self):
        """возвращяем новую коллекцию активных студентов"""
        new_collection = StudentCollection()
        for student in self._students:
            if student.is_active:
                new_collection.add(student)
        return new_collection
    

    def print_coll(self):
        """вывести всех студентов коллекции в консоль"""
        for st in self:
            print(st)

    def apply(self, func):
        """применить функцию ко всем студентам коллекции
        функция, принимающая студента и возвращающая результат -
        cписок результатов применения функции"""
        resalt = list()
        new_resalt = list(map(func, self._students))
        for st in new_resalt:
            resalt.append(st)
        return resalt

    
    def __str__(self):
        """строковое представление коллекции"""
        result = ""
        for st in self._students:
            result += str(st) + "\n"
        return result
    
    def __len__(self):
        """возвращает количество студентов в коллекции"""
        return len(self._students)
    
    def __iter__(self):
        """для обхода коллекции в цикле"""
        return iter(self._students)
    
    def __getitem__(self, index):
        """получение по индексу"""
        return self._students[index]
    
