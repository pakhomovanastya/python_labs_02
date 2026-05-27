import json

def save(collection, filepath: str) -> None:
    """Сохранить коллекцию в JSON-файл."""
    #превращаем студентов в список словарей
    data = []
    for student in collection.get_all():
        student_dict = {"surname": student.surname,
                        "name": student.name,
                        "age": student.age,
                        "curse": student.curse,
                        "gpa": student.gpa,
                        "is_active": student.is_active}
        data.append(student_dict)

    #записываем в JSON файл
    #ensure_ascii=False для русских букв, indent=2 форматирование с отступами
    #"w" создаём файл или перезаписываем существующий
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load(filepath: str) -> list:
    """Загрузить объекты из JSON-файла."""
    try:
        with open (filepath, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return data