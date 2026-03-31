from lib.student import Student

class BachelorStudent(Student):

    def __init__(self, surname: str, name: str, age: int, curse: int, 
                 gpa: float, gpa_certificate: float, curse_start: int):
        super().__init__(surname, name, age, curse, gpa)

        self.__gpa_certificate = gpa_certificate #аттеатсат
        self.__curse_start = curse_start

    def cheak_gpa_certificate(self):
        if self.__gpa_certificate < 3:
            raise ValueError("Низкий балл аттестата")
        return self.__curse_start
    
    def to_collect_money(self):
        if not self.is_active:
            return 0
        if self.__gpa_certificate >= 4.5 and self.gpa > 4:
            return 3000
        elif self.__gpa_certificate >= 3.5 and self.gpa > 3:
            return 1000
        else:
            return 0
    
    def __str__(self):
        return f"Бакалавр: {super().__str__()}, {self.__gpa_certificate}, {self.__curse_start}"

class MasterStudent(Student):
    def __init__(self, surname: str, name: str, age: int, curse: int, 
                 gpa: float, finished_universiti: str, gpa_bachelor: float):
        super().__init__(surname, name, age, curse, gpa)
    
        self.__finished_universiti = finished_universiti
        self.__gpa_bachelor = gpa_bachelor

    def chek_gpa_bachelor(self):
        if self.__gpa_bachelor < 4:
            raise ValueError("Низкий балл бакалавра")
        return self.curse
    
    def to_collect_money(self):
        if not self.is_active:
            return 0
        if self.__gpa_bachelor >= 4.5 and self.gpa > 4:
            return 5000
        elif self.__gpa_bachelor >= 3.5 and self.gpa > 3:
            return 3000
        else:
            return 0
    
    def __str__(self):
        return f"Магистр: {super().__str__()}, {self.__finished_universiti}, {self.__gpa_bachelor}"



class PhDStudent(Student):
    def __init__(self, surname: str, name: str, age: int, curse: int, 
                 gpa: float, research_fild: str, count_publikations: int):
        super().__init__(surname, name, age, curse, gpa)

        self.__research_fild = research_fild #область исследования
        self.__count_publikations = count_publikations
        

    def chek_count_publikations(self):
        if self.__count_publikations < 2:
            raise ValueError("Не хвататет колличество публикаций")
        return self.curse
    
    def to_collect_money(self):
        if not self.is_active:
            return 0
        if self.__count_publikations >= 20 and self.gpa > 4:
            return 10000
        elif self.__count_publikations >= 10 and self.gpa > 3:
            return 5000
        else:
            return 0

    def __str__(self):
        return f"Аспирант: {super().__str__()}, {self.__research_fild}, {self.__count_publikations}"
    
    
