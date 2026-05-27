from lab01.validate import validate_name, validate_gpa, validate_age, validate_curse
from typing import TypeVar, Generic, Callable, Optional, Protocol, Iterator

T = TypeVar("T") # любой тип
R = TypeVar('R') # тип результата map

class TypeCollection(Generic[T]):
    """обобщённая коллекция для хранения объектов любого типа T"""
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)
    
# методы на 4
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """найти первый элемент, удовлетворяющий условию
        возвращает элемент или None"""
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """отфильтровать элементы по условию
        возвращает список подходящих элементов"""
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> list[R]:
        """
        преобразовать каждый элемент с помощью функции
        возвращает список результатов (тип R может отличаться от T)"""
        return [transform(item) for item in self._items]
    
    def __str__(self) -> str:
        """строковое представление коллекции"""
        result = ""
        for st in self._items:
            result += str(st) + "\n"
        return result
    
    def __len__(self) -> int:
        """возвращает количество студентов в коллекции"""
        return len(self._items)
    
    def __iter__(self) -> Iterator[T]:
        """для обхода коллекции в цикле"""
        return iter(self._items)
    
    def __getitem__(self, index) -> T:
        """получение по индексу"""
        return self._items[index]

# протоколы
class Displayable(Protocol):
    """протокол (объект, который можно отобразить в виде строки)"""
    def display(self) -> str:
        """вернуть строковое представление объекта"""
        ...

class Scorable(Protocol):
    """протокол (объект, который имеет числовой рейтинг)"""
    def score(self) -> float:
        """вернуть числовую оценку объекта"""
        ...

# типовые переменные с ограничениями (для использования в аннотациях)
D = TypeVar('D', bound=Displayable) #объекты с методом display()
S = TypeVar('S', bound=Scorable)  #объекты с методом score()

class Student:
    """представляет студента с его персональными данными и успеваемостью"""
    min_gpa = 1
    max_gpa = 5

    min_age = 14
    max_age = 100

    min_curse = 1
    max_curse = 6

    min_bal_to_next_curse = 3

    def __init__(self, surname: str, name: str, age: int, curse: int, gpa: float) -> None:
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
    def surname(self) -> str:
        return self.__surname
    @surname.setter
    def surname(self, value: str):
        self.__surname = validate_name(value, "Фамилия")

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        self.__name = validate_name(value, "Имя")

    @property
    def age(self) -> int:
        return self.__age
    @age.setter
    def age(self, value: int):
        self.__age = validate_age(value, self.min_age, self.max_age)
    
    @property
    def curse(self) -> int:
        return self.__curse
    @curse.setter
    def curse(self, value: int):
        self.__curse = validate_curse(value, self.min_curse, self.max_curse)

    @property
    def gpa(self) -> float:
        return self.__gpa
    @gpa.setter
    def gpa(self, value: float):
        self.__gpa = validate_gpa(value, self.min_gpa, self.max_gpa)

    @property
    def is_active(self):
        return self.__is_active
    
    @classmethod
    def from_json(cls, data):
        obj = cls(data["surname"],
                   data["name"],
                   data["age"],
                   data["curse"],
                   data["gpa"])
        if not data["is_active"]:
            obj.not_active()
        return obj
    



    def __str__(self) -> str:
        return f"Фамилия Имя {self.__surname} {self.__name}, возраст {self.__age}\n курс: {self.__curse}, ср. балл: {self.__gpa:.2f}."
    def __repr__(self) -> str:
        return f"__surname {self.__surname}, __name {self.__name}, __age {self.__age}, __curse {self.__curse}, __gpa {self.__gpa}."
    def __eq__(self, student2) -> bool:
        return (self.__surname==student2.__surname and 
                self.__name==student2.__name and 
                self.__age==student2.__age and
                self.__curse == student2.__curse)
        

    #бизнесс-методы
    #можно ли перейти на следующий курс по сред баллу
    def chek_to_next_curse(self) -> bool:
        """проверка возможности перевода на следующий курс по среднему баллу"""
        if not self.__is_active:
            raise ValueError("не хватате баллов для перехода на следующий курс")
        if self.__gpa >= self.min_bal_to_next_curse:
            return True
        return False
    

    def to_next_course(self) -> str:
        """БИЗНЕС-МЕТОД 1: перевод на следующий курс (изменение состояния)"""
        if not self.__is_active:
            raise ValueError("нельзя перевести отчисленного студента")
        if self.__curse >= self.max_curse:
            raise ValueError("Студент уже на последнем курсе")
        self.__curse += 1
        return f"cтудент переведен на {self.__curse} курс"
    
    def to_collect_money(self) -> int:
        """БИЗНЕС-МЕТОД 2: расчёт стипендии"""
        if not self.__is_active:
            return 0
        if self.__gpa >= 4.5:
            return 5000
        elif self.__gpa >= 3.5:
            return 3000
        else:
            return 0
    
    
    def not_active(self):
        self.__is_active = False
    
    def active(self):
        """Активировать студента"""
        self.__is_active = True

    def display(self) -> str:
        """метод возвращает строковое представление для Displayable Protocol"""
        return (f"Студент: {self.surname} {self.name}, {self.age} лет, "
            f"{self.curse} курс, GPA: {self.gpa}, ")
    
    def score(self) -> float:
        """метод возвращает числовой рейтинг студента (для Scorable Protocol)"""
        return self.gpa