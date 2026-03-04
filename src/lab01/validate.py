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
