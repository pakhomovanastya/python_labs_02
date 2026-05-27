
class OutOfRangeException(Exception):
    "Значение вне допустимого диапазона"
    def __init__(self, message):
        super().__init__(message)

class NotFoundException(Exception):
    """Исключение: объект не найден в коллекции"""
    def __init__(self, message):
        super().__init__(message)

class NotCorrectData(Exception):
    "Некорректный ввод данных"
    def __init__(self, message):
        super().__init__(message)