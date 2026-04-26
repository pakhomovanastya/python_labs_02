class Animal:
    def __init__(self, name: str, age: int):
        if not name:
            raise ValueError("Имя не может быть пустым")
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self._name}, {self._age} лет"


class Cat(Animal):
    def __init__(self, name: str, age: int, indoor: bool):
        super().__init__(name, age)
        self._indoor = indoor

    def speak(self):
        return "Мяу!"

    def is_indoor(self):
        return "домашняя" if self._indoor else "уличная"


cat1 = Cat("тёма", 3, True)
cat2 = Cat("буся", 2, False)

print(cat1)
print(cat1.speak())
print(cat1.is_indoor())
print(cat2.is_indoor())