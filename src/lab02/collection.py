from lib.student import Student
class StudentCollection:
    """коллекция для хранения и управления объектами Student"""
    def __init__(self):
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
        if 0 <= index < len(self._students):
            return self._students.pop(index)
        raise IndexError(f"индекс не попадает в диапазон от 0 до {len(self._students)}")

    def get_all(self):
        """возвращяет список студентов"""
        return self._students
    
    def sort(self, key):
        """сортировка по параметру (по ключу)"""
        self._students.sort(key=key)

    def sort_by_name(self):
        """сортировка по имении (вызываем верхний метод с лямбдой)"""
        self.sort(key=lambda st: st.name)
    
    def sort_by_surname(self):
        """сортировка по имении (вызываем верхний метод с лямбдой)"""
        self.sort(key=lambda st: st.surname)
    
    def sort_by_curse(self):
        """сортировка по курсу (вызываем верхний метод с лямбдой)"""
        self.sort(key=lambda st: st.curse)
    
    def sort_by_gpa(self):
        """сортировка по среднему баллу (вызываем верхний метод с лямбдой)"""
        self.sort(key=lambda st: st.gpa)
    

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
    

    def get_active(self):
        """возвращяем новую коллекцию активных студентов"""
        new_collection = StudentCollection()
        for student in self._students:
            if student.is_active:
                new_collection.add(student)
        return new_collection
    
    
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
    

    


    
    