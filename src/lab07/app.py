from .models import TypeCollection, Student
from .exceptions import OutOfRangeException, NotFoundException, NotCorrectData
from .storage import save
from pathlib import Path


class StudentApp:
    """Приложение для управления студентами"""

    def __init__(self):
        """Инициализация создание коллекции и загрузка данных"""
        self.collection: TypeCollection[Student] = TypeCollection()

    def add (self, st_name, st_surname, st_age, st_gpa, st_curse):
        """Добавить студента в коллекцию"""
        st = Student(st_surname, st_name, st_age, st_curse, st_gpa) 
        self.collection.add(st)

    #метод для 7лабы для оценки на 5
    def add_all(self, students_data: list) -> None:
        """Добавить несколько студентов из списка словарей"""
        for data in students_data:
            obj = Student.from_json(data)
            self.collection.add(obj)  

    def save_coll_to_json(self) -> None:
        """Сохранить коллекцию в JSON файл"""
        #Path(__file__)	Превращает строку пути в специальный объект Path
        #.resolve()	Превращает относительный путь в абсолютный (полный)
        #.parents[1] Поднимается на 1 уровень вверх по папкам
        BASE_DIR = Path(__file__).resolve().parents[1]
        DATA_DIR = BASE_DIR / "data"
        
        if not DATA_DIR.exists():
            DATA_DIR.mkdir(parents=True)
        
        DATA_FILE = DATA_DIR / "students.json"
        save(self.collection, DATA_FILE)
    
    def list_st(self):
        """Вернуть список всех студентов"""
        return self.collection.get_all()
    
    def find_st(self, st_surname):
        """Найти студента по фамилии"""
        st_find = self.collection.find(lambda st: st.surname == st_surname)
        if not st_find:
            raise NotFoundException(f"Студент с фамилией '{st_surname}' не найден")
        return st_find
    
    def find_st_n(self, st_name):
        """Найти студента по имени"""
        st_find = self.collection.find(lambda st: st.name == st_name)
        if not st_find:
            raise NotFoundException(f"Студент с именем '{st_name}' не найден")
        return st_find
    
    def find_st_c(self, st_curse):
        """Найти студента по курсу"""
        st_find = self.collection.filter(lambda st: st.curse == st_curse)
        if not st_find:
            raise NotFoundException(f"Студент по курсу '{st_curse}' не найден")
        return st_find
    
    def remove_by_index(self, index):
        """Удалить студента по индексу"""
        if 0 > index or index >= len(self.collection):
            raise OutOfRangeException("Неправильный индекс студена")
        self.collection.remove(self.collection[index])

    def sort_collection(self, sort_type: str) -> list:
        """Вернуть отсортированную коллекцию (без изменения исходной)"""
        if sort_type == "surname":
            return sorted(self.collection.get_all(), key=lambda st: st.surname)
        elif sort_type == "name":
            return sorted(self.collection.get_all(), key=lambda st: st.name)
        elif sort_type == "curse":
            return sorted(self.collection.get_all(), key=lambda st: st.curse)
        elif sort_type == "gpa":
            return sorted(self.collection.get_all(), key=lambda st: st.gpa, reverse=True)
        else:
            return self.collection.get_all()

    def get_collection_size(self) -> int:
        """Вернуть количество студентов в коллекции"""
        return len(self.collection)