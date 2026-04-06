from abc import ABC, abstractmethod

class PassableExam(ABC):
    @abstractmethod
    def pass_exam(self, subject): #сдаёи экзамен
        pass

class Admissible(ABC):
    @abstractmethod
    def admiss_university(self): #поступаем в университет
        pass

class DefendableDissertation(ABC): #защита диссертации
    @abstractmethod
    def defend_dissertation(self):
        pass


