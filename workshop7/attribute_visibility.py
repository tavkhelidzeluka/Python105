class Student:
    def __init__(self, name: str) -> None:
        # public
        self.name = name
        # private
        # self.__gpa = 0
        # protected 
        self._gpa = 0
    
    def gpa(self) -> float:
        # getter
        return self._gpa

    def set_gpa(self, gpa: float) -> None:
        # setter
        if not (0 <= gpa <= 4):
            raise ValueError("GPA Must be in between 0 and 4")
        self._gpa = gpa
            
class Derived(Student):
    def print(self):
        print(self._gpa)
 
s1 = Derived("Nick")

# Don't do this
# s1.__gpa = 25
# s1.__gpa = 700
# print(s1._gpa)

s1.set_gpa(2.5)
print(s1.gpa())

s1.print()


