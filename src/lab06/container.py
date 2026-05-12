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
    
