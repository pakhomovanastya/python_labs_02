class Student:
    def __init__(self, full_name, group, course, gpa):
            if not full_name or not full_name.strip():
                raise ValueError("имя пустое")
            self._full_name = full_name.strip()
            
            if not group or not group.strip():
                raise ValueError("группа пустая")
            self._group = group.strip()
            
            if not isinstance(course, int) or course < 1 or course > 6:
                raise ValueError("курс вне 1–6")
            self._course = course

            if not isinstance(gpa, (int, float)) or gpa < 2.0 or gpa > 5.0:
                raise ValueError("gpa вне 2.0–5.0")
            self._gpa = float(gpa)
    
    @property
    def full_name(self):
        return self._full_name
    
    @property
    def group(self):
        return self._group
    
    @property
    def course(self):
        return self._course
    
    @property
    def gpa(self):
        return self._gpa
    
    def promote(self):
        if self._course >= 6:
            raise ValueError("уже последний курс")
        self._course += 1
    
    def update_gpa(self, new_gpa):
        if new_gpa < 2.0 or new_gpa > 5.0:
            raise ValueError("gpa вне 2.0–5.0")
        self._gpa = float(new_gpa)
    
    def __str__(self):
        parts = self._full_name.split()
        if len(parts) >= 2:
            surname = parts[0]
            initials = ''.join(p[0].upper() + '.' for p in parts[1:])
            short_name = f"{surname} {initials}"
        else:
            short_name = self._full_name
        
        return f"{short_name} ({self._group}, курс {self._course}, GPA {self._gpa})"
   
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self._full_name == other._full_name and self._group == other._group


# для проверки 
s = Student('Иванов Иван Иванович', 'БИВТ-25-5', 2, 4.5)
print(s)
s.promote()
print(s.course)
s.update_gpa(4.8)
print(s.gpa)

try:
    Student('', 'БИВТ-25-5', 2, 4.5)
except ValueError as e:
    print(f"ошибка: {e}")

try:
    Student('Петров', 'БИВТ-25-5', 7, 4.5)
except ValueError as e:
    print(f"ошибка: {e}")

try:
    s.update_gpa(5.5)
except ValueError as e:
    print(f"ошибка: {e}")