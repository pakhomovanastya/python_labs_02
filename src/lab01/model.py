from .validate import validate_name, validate_gpa, validate_age, validate_curse

class Student:
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
        """перевод на следующий курс (изменение состояния)"""
        if not self.__is_active:
            raise ValueError("нельзя перевести отчисленного студента")
        if self.__curse >= self.max_curse:
            raise ValueError("Студент уже на последнем курсе")
        self.__curse += 1
        return f"cтудент переведен на {self.__curse} курс"
    
    
    def not_active(self):
        self.__is_active = False