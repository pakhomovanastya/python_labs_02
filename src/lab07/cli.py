from .app import StudentApp, NotFoundException, OutOfRangeException
from .exceptions import NotCorrectData
from .storage import load
from pathlib import Path

class UserInterface:
    """Класс для управления консольным интерфейсом"""

    def __init__(self):
        """Инициализация приложения"""
        self.__st_app = StudentApp()
    
    def __add (self):
        """Добавить нового студента"""
        try:
            st_name = input("Введите имя: ")
            st_surname = input("Введите фамилию: ")
            st_age = int(input("Введите возраст: "))
            st_gpa = float(input("Введите средний балл: "))
            st_curse = int(input("Введите курс на котором учится студент: "))
        except ValueError:
            raise NotCorrectData("Неккоректные данные")

        self.__st_app.add(st_name, st_surname, st_age, st_gpa, st_curse)

    def __print_all(self):
        """Вывод всех студентов"""
        st = self.__st_app.list_st()
        if not st:
            print("Пустая коллекция")
            return
        for i in range(len(st)):
            print(f"{i+1}. {st[i]}")
    
    def __find_by_surname(self):
        """Поиск студента по фамилии"""
        st = input("Введите фамилию для поиска: ")
        try:
            f_st = self.__st_app.find_st(st)
            print(f"Найден - {f_st} ")
        except NotFoundException as e:
            print(e)

    def __find_by_name(self):
        """Поиск студента по имени"""
        st = input("Введите имя для поиска: ")
        try:
            f_st = self.__st_app.find_st_n(st)
            print(f"- Найден: {f_st}")
        except NotFoundException as e:
            print(e)

    def __find_by_curse(self):
        """Поиск студентов по курсу"""
        st = input("Введите курс для поиска: ")
        try:
            f_st = self.__st_app.find_st_c(int(st))
            if not f_st:
                print("Студенты не найдены")
                return
            for i in range(len(f_st)):
                print(f"{f_st[i]}")
        except NotFoundException as e:
            print(e)
        except ValueError:
            print("Неккортектные данные")

    def __remuve_by_index(self):
        """Удаление студента по индексу"""
        self.__print_all()
        try:
            st = int(input("\nВведите номер для удаления студента: "))
            self.__st_app.remove_by_index(st-1)
        except OutOfRangeException as e:
            print(e)
        except ValueError:
            print("Неккоректные данные")

    def __sort_menu(self) -> None:
        """Меню сортировки"""
        self.__show_sub_menu_for_sort()
        choice = input("Выберите пункт: ").strip()
        sort_map = {"5.1": "surname",
                    "5.2": "name",
                    "5.3": "curse",
                    "5.4": "gpa"}
        
        if choice in sort_map:
            sorted_list = self.__st_app.sort_collection(sort_map[choice])
            if not sorted_list:
                print("Коллекция пуста")
                return
            for i, student in enumerate(sorted_list, 1):
                print(f"{i:2}. {student.display()}")
        elif choice == "5.0":
            return
        else:
            print("Некорректный пункт")

    def __list_to_collection(self, students_json: list) -> None:
        """Преобразование списка словарей в коллекцию"""
        if students_json:
            self.__st_app.add_all(students_json)


    def run(self) -> None:
        """Запуск основного цикла приложения"""
        # Путь к файлу данных
        #Path(__file__)	Превращает строку пути в специальный объект Path
        #.resolve()	Превращает относительный путь в абсолютный (полный)
        #.parents[1] Поднимается на 1 уровень вверх по папкам
        BASE_DIR = Path(__file__).resolve().parents[1]
        DATA_DIR = BASE_DIR / "data"
        DATA_FILE = DATA_DIR / "students.json"

        # Загрузка данных при старте
        if DATA_FILE.exists():
            students_data = load(DATA_FILE)
            self.__list_to_collection(students_data)
        else:
            print("Файл данных не найден. Будет создан новый при сохранении.")

        self.__show_menu()
        answer = input("Выберите пункт: ").strip()

        while answer != "0":
            try:
                if answer == "1":
                    try:
                        self.__add()
                    except NotCorrectData as e:
                        print(f"{e}")

                elif answer == "2":
                    self.__print_all()

                elif answer == "3":
                    self.__show_sub_menu_for_search()
                    self.__search()

                elif answer == "4":
                    self.__remuve_by_index()

                elif answer == "5":
                    self.__sort_menu()

                else:
                    print("Ошибка: неверный пункт меню")

            except Exception as e:
                print(f"Произошла ошибка: {e}")

            self.__show_menu()
            answer = input("Выберите пункт: ").strip()

        # Сохранение при выходе
        self.__st_app.save_coll_to_json()
    

    def __search(self):
        "Поиск студента"
        index = input("Введите пункт:   ")
        if index  == "3.1":
            self.__find_by_surname()

        elif index  == "3.2":
            self.__find_by_name()

        elif index == "3.3":
            self.__find_by_curse()

        elif index == "3.0":
            pass
        else:
            print("Неккоректный пункт")


    def __show_sub_menu_for_search(self):
        print("\n--- Поиск студентов ---\n"\
        "3.1 По фамилии\n" \
        "3.2 По имени\n" \
        "3.3 По курсу\n" \
        "3.0 Назад") 

    def __show_sub_menu_for_sort(self):
        print("\n--- Сортировка студентов ---\n"\
        "5.1 По фамилии\n" \
        "5.2 По имени\n" \
        "5.3 По курсу\n" \
        "5.4 По по GPA\n" \
        "5.0 Назад") 

        
    def __show_menu (self):
        print("\n---Главное меню---\n" \
        "1. Добавить студента\n" \
        "2. Список всех студентов\n" \
        "3. Найти студента\n" \
        "4. Удалить студента по номеру\n"\
        "5. Сортировать\n"\
        "0. Выход")
