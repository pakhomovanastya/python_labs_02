from typing import TypeVar, Generic

T = TypeVar("T")

class TypeCollection(Generic[T]):
    
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)
    
