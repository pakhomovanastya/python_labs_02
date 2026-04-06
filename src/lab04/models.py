from .interfaces import *
from lib.validate import validate_name, validate_gpa, validate_age, validate_curse

class Student(PassableExam, Admissible):
    """представляет студента с его персональными данными и успеваемостью"""
    min_gpa = 1
    max_gpa = 5

    min_age = 14
    max_age = 100

    min_curse = 1
    max_curse = 6

    min_bal_to_next_curse = 3

    def __init__(self, surname: str, name: str, age: int, curse: int, gpa: float):
        self.__surname = None
        self.__name = None
        self.__age = None #создаём закрытое поле
        self.__curse = None
        self.__gpa = None

        self.surname = surname #вызываем сеттер на surname
        self.name = name
        self.age = age
        self.curse = curse
        self.gpa = gpa
        self.__is_active = True # состояние студента (активен/отчислен)

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, value):
        self.__surname = validate_name(value, "Фамилия")

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = validate_name(value, "Имя")

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = validate_age(value, self.min_age, self.max_age)
    
    @property
    def curse(self):
        return self.__curse
    @curse.setter
    def curse(self, value):
        self.__curse = validate_curse(value, self.min_curse, self.max_curse)

    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, value):
        self.__gpa = validate_gpa(value, self.min_gpa, self.max_gpa)

    @property
    def is_active(self):
        return self.__is_active



    def __str__(self):
        return f"Фамилия Имя {self.__surname} {self.__name}, возраст {self.__age}\n курс: {self.__curse}, ср. балл: {self.__gpa:.2f}."
    def __repr__(self):
        return f"__surname {self.__surname}, __name {self.__name}, __age {self.__age}, __curse {self.__curse}, __gpa {self.__gpa}."
    def __eq__(self, student2):
        return (self.__surname==student2.__surname and 
                self.__name==student2.__name and 
                self.__age==student2.__age and
                self.__curse == student2.__curse)
        

    #бизнесс-методы
    #можно ли перейти на следующий курс по сред баллу
    def chek_to_next_curse(self):
        """проверка возможности перевода на следующий курс по среднему баллу"""
        if not self.__is_active:
            raise ValueError("не хватате баллов для перехода на следующий курс")
        if self.__gpa >= self.min_bal_to_next_curse:
            return True
        return False
    

    def to_next_course(self):
        """БИЗНЕС-МЕТОД 1: перевод на следующий курс (изменение состояния)"""
        if not self.__is_active:
            raise ValueError("нельзя перевести отчисленного студента")
        if self.__curse >= self.max_curse:
            raise ValueError("Студент уже на последнем курсе")
        self.__curse += 1
        return f"cтудент переведен на {self.__curse} курс"
    
    def to_collect_money(self):
        """БИЗНЕС-МЕТОД 2: расчёт стипендии"""
        if not self.__is_active:
            return 0
        if self.__gpa >= 4.5:
            return 5000
        elif self.__gpa >= 3.5:
            return 3000
        else:
            return 0
        
    def pass_exam(self, subject):
        print(f"{self.surname} {self.name} сдаёт {subject} экзамен")
    
    def not_active(self):
        self.__is_active = False


class BachelorStudent(Student):

    def __init__(self, surname: str, name: str, age: int, curse: int, 
                 gpa: float, gpa_certificate: float, curse_start: int):
        super().__init__(surname, name, age, curse, gpa)

        self.__gpa_certificate = gpa_certificate #аттеатсат
        self.__curse_start = curse_start


    def cheak_gpa_certificate(self):
        if self.__gpa_certificate < 3:
            raise ValueError("Низкий балл аттестата")
        return self.__curse_start
    
    def to_collect_money(self):
        if not self.is_active:
            return 0
        if self.__gpa_certificate >= 4.5 and self.gpa > 4:
            return 3000
        elif self.__gpa_certificate >= 3.5 and self.gpa > 3:
            return 1000
        else:
            return 0

    def admiss_university(self):
        cuerse = self.cheak_gpa_certificate()
        if cuerse == 1:
            print("сдаём математику и физику")
        else:
            print("сдаём математику")


    
    def __str__(self):
        return f"Бакалавр: {super().__str__()}\nбалл аттестата: {self.__gpa_certificate}, начальный курс: {self.__curse_start}"

class MasterStudent(Student):
    def __init__(self, surname: str, name: str, age: int, curse: int, 
                 gpa: float, finished_universiti: str, gpa_bachelor: float):
        super().__init__(surname, name, age, curse, gpa)
    
        self.__finished_universiti = finished_universiti
        self.__gpa_bachelor = gpa_bachelor

    def chek_gpa_bachelor(self):
        if self.__gpa_bachelor < 4:
            raise ValueError("Низкий балл бакалавра")
        return self.curse
    
    def to_collect_money(self):
        if not self.is_active:
            return 0
        if self.__gpa_bachelor >= 4.5 and self.gpa > 4:
            return 5000
        elif self.__gpa_bachelor >= 3.5 and self.gpa > 3:
            return 3000
        else:
            return 0
        
    def admiss_university(self):
        cuerse = self.chek_gpa_bachelor()
        if cuerse == 1:
            print("сдаём математику, физику, информатику")
        else:
            print("сдаём математику, информатику")
    
    def __str__(self):
        return (f"Магистр: {super().__str__()}\nвуз: {self.__finished_universiti}, GPA бакалавра: {self.__gpa_bachelor}")



class PhDStudent(Student, DefendableDissertation):
    def __init__(self, surname: str, name: str, age: int, curse: int, 
                 gpa: float, research_fild: str, count_publikations: int):
        super().__init__(surname, name, age, curse, gpa)

        self.__research_fild = research_fild #область исследования
        self.__count_publikations = count_publikations
        

    def chek_count_publikations(self):
        if self.__count_publikations < 2:
            raise ValueError("Не хвататет колличество публикаций")
        return self.curse
    
    def to_collect_money(self):
        if not self.is_active:
            return 0
        if self.__count_publikations >= 20 and self.gpa > 4:
            return 10000
        elif self.__count_publikations >= 10 and self.gpa > 3:
            return 5000
        else:
            return 0

    def admiss_university(self):
        if self.__count_publikations > 2:
            print("сдаём математику")
        else:
            print("сдаём математику, физику, информатику")

    def pass_exam(self, subject):
        print(f"{self.surname} {self.name} сдаёт научную работу по {subject}")

    def defend_dissertation(self):
        print(f'{self.surname} {self.name}, {self.__count_publikations}: защищает диссертацию')

    def __str__(self):
        return (f"Аспирант: {super().__str__()}\nобласть исследований: {self.__research_fild}, публикации: {self.__count_publikations}")
    
#todo добавить метод поиска по типу

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
    
    def get_by_type(self, cls):
        new_collection = StudentCollection()
        for student in self._students:
            if type(student) == cls:
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
    