lab1/model.py
---
Атрибуты класса и закрытые атрибуты экземпляра
<img width="932" height="612" alt="Атрибуты класса" src="https://github.com/user-attachments/assets/36f1933d-3d94-4b5f-bf39-62ea340b1d66" />
---
Декоратор @property и метод-сеттер (setter)
<img width="667" height="821" alt="image" src="https://github.com/user-attachments/assets/8ec0d3cc-93c1-4a5d-964d-0033a0adbbca" />
---
Магические методы
>__str__ определяет строковое представление объекта для пользователей
>__repr__ определяет "официальное" строковое представление объекта
>__eq__ Это магический метод для перегрузки оператора равенства ==.\n Определяет логику сравнения двух объектов. Должен возвращать True или False.
<img width="1417" height="285" alt="Магические методы" src="https://github.com/user-attachments/assets/97cb7546-5607-4c9a-82ab-b3bde86b0c2b" />

Методы валидации
>validate_name
>>Проверка типа: должно быть строкой (isinstance(name, str))
>>Проверка на пустую строку: длина не может быть 0
>
>validate_gpa
>>Проверка типа: должно быть float или int
>>Проверка диапазона: от min_gpa до max_gpa (атрибуты класса)
>
>validate_age
>>Проверка типа: должно быть int
>>Проверка диапазона: строго больше min_age и строго меньше max_age
>
>validate_curse
>>Проверка типа: должно быть int
>>Проверка диапазона: от min_curse до max_curse
<img width="996" height="750" alt="Методы валидации" src="https://github.com/user-attachments/assets/acf76e19-dde2-49e7-9a38-7e884072b935" />

Бизнес-методы
>chek_to_next_curse
>проверяет, может ли студент перейти на следующий курс на основе среднего балла.
>>Если студент неактивен — исключение (хотя сообщение об ошибке не соответствует условию)
>>Если средний балл >= минимального для перехода (атрибут класса) — возвращает True, иначе — возвращает False
>
>to_next_course
>выполняет перевод студента на следующий курс (изменяет состояние объекта).
>>Если студент неактивен — исключение
>>Если студент уже на последнем курсе (max_curse) — исключение
>>Иначе — увеличивает номер курса на 1
<img width="945" height="671" alt="бизнесс-методы" src="https://github.com/user-attachments/assets/c3a88b3c-fbbd-4834-942b-477ceebe722e" />

model.py
---
```python
from validate import validate_name, validate_gpa, validate_age, validate_curse

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
```

vallidate.py
---
```python
def validate_name(name: str, field_name: str) -> str:
    if not isinstance(name, str):
        raise TypeError(f"{field_name} должна быть строкой, получен {type(name).__name__}")
    if len(name) == 0:
        raise ValueError(f"{field_name} не может быть пустой")
    return name

def validate_gpa(gpa, min_gpa: float, max_gpa: float) -> float:
    if not (type(gpa) ==float or type(gpa) ==int):
        raise TypeError(f"Средний балл должен быть числом, получен {type(gpa).__name__}")
    if min_gpa <= gpa <= max_gpa:
        return float(gpa)
    raise ValueError(f"Средний балл должен быть от {min_gpa} до {max_gpa}")

def validate_age(age: int, min_age: int, max_age: int) -> int:
    if not type(age) ==int:
        raise TypeError(f"Возраст должен быть целым числом, получен {type(age).__name__}")
    if min_age <= age <= max_age:
        return int(age)
    raise ValueError(f"Возраст должен быть от {min_age} до {max_age}")

def validate_curse(curse: int, min_curse: int, max_curse: int) -> int:
    if type(curse)!=int:
        raise TypeError(f"Курс должен быть целым числом, получен {type(curse).__name__}")
    if min_curse <= curse <= max_curse:
        return curse
    raise ValueError(f"Курс должен быть от {min_curse} до {max_curse}")

```

lab1/demo.py
---
```python
from random import randint
from model import Student


student1 = Student("Иванов", "Иван", 19, 2, 2.7)
student2 = Student("Петров", "Петр", 20, 3, 3.2)
student3 = Student("Сидорова", "Анна", 18, 1, 4.8)
student4 = Student("Иванов", "Иван", 19, 2, 2.7)

print("\n> три экземпляра класса Student с разными параметрами")
print(student1) #вызывает __str__
print(student2)
print(student3)
print(repr(student3)) #вызывает __repr__


print("\n> Сравнение объектов")
if student1 == student2: #вызывает __eq__
    print(f"один и тот же студент")
else:
    print(f"разные студенты")

if student1 == student4: #вызывает __eq__
    print(f"один и тот же студент")
else:
    print(f"разные студенты")


print('\n> Обработка ошибок фамилия передана как число')
try:
    student4 = Student(16, "Анна", 18, 1, 4.8)
except (ValueError, TypeError) as e:
    print(f"студнт не создался, потому что {e}\n")

print('\n> Обработка ошибок фамилия пустая')
student3.surname="Петрова"
try:
    student3.surname="" 
except (ValueError, TypeError) as e:
    print(f"не удалость записать фамилию, потому что {e}\n")


print("> Демонстрация атрибутов класса")
print(f"максимальный возраст {Student.max_age}") #через класс
print(f"максимальный возраст {student1.max_age}") #через экземпляр


print("\n> первый сценарий работы")
for i in range(4):
    try:
        if student2.chek_to_next_curse():
            student2.to_next_course()
            student2.gpa = randint(3, 5)
            print(f"студент переведён на {student2.curse} курс, новый балл: {student2.gpa}")
        else:
            print(f"студент не может быть переведён (балл: {student2.gpa})")
            break
    except ValueError as e:
        print(f"Ошибка {e}")

    
print("\n> второй сценарий работы")
if student1.chek_to_next_curse():
    student1.to_next_course()
    print(f"студент {student1.surname} переведён на курс {student1.curse}")
else:
    print(f"студент {student1.surname} не прошёл прверку по среднему баллу {student1.gpa}")

    
print('\n> третий сценарий работы')
student3.not_active()
try:
    if student3.chek_to_next_curse():
        student3.to_next_course()
    else:
        print(f"студент {student3.surname} не может быть переведён (причина: неактивен)")
except ValueError as e:
    print(f"Ошибка при попытке перевода: {e}")
```
вывод 
---
<img width="861" height="858" alt="валидация demo py " src="https://github.com/user-attachments/assets/945becb1-256a-4bec-b5c0-c0fa171d7873" />
