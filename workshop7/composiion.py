class Address:
    def __init__(self, city: str, street: str, zip: int) -> None:
        self.street = street
        self.city = city 
        self.zip = zip
    
    def __str__(self) -> str:
        return f'{self.city}, {self.street}, {self.zip}'

class Person:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address


class Student(Person):
    def __init__(self, university: str, *args) -> None:
        super().__init__(*args)
        self.university = university
        # self.name = "From Student"
    
    def study(self) -> None:
        print(f"{self.name} is Studying")

class Employee(Person):
    def __init__(self, salary: int, *args) -> None:
        super().__init__(*args)
        self.salary = salary
        # self.name = "From Employee"
    
    def __str__(self) -> str:
        return f'Name: {self.name}\nSalary: {self.get_salary()}\nAddress: {self.address}'

    def get_salary(self) -> float:
        return self.salary

    def work(self) -> None:
        print(f"{self.name} is Working")


class HourlyEmployee(Employee):
    def __init__(self, hours: int, *args) -> None:
        super().__init__(*args)
        self.hours = hours

    def get_salary(self) -> float:
        return super().get_salary() * self.hours


class FixedEmployee(Employee):
    pass

class CommissionEmployee(FixedEmployee):
    def __init__(self, commission: int, *args) -> None:
        super().__init__(*args)
        self.commission = commission

    def get_salary(self) -> float:
        return super().get_salary() + self.commission


class StudentEmployee(Student, Employee):
    def __init__(self, university: str, salary: float, name: str, address: Address) -> None:
        # Student.__init__()
        super().__init__(university, salary, name, address)
        
        
    def get_salary(self) -> float:
        return self.salary / 2

# mike: Employee = FixedEmployee(5000, "Mike", Address("New York", "Manhattan", 21657))   
# e2: Employee = CommissionEmployee(25, 2500, "Nick", Address("New York", "Manhattan", 21657))   
# e3: Employee = HourlyEmployee(3,  500, "Josh", Address("New York", "Manhattan", 21657))   
# s: Employee = StudentEmployee("TSU", 500, "Josh", Address("New York", "Manhattan", 21657))   

# print(mike) 
# print(e2) 
# print(e3) 


# s.study()
# s.work()


class A:
    def __init__(self) -> None:
        print('A __init__ called')
        self.a = 2
        
class B:
    def __init__(self) -> None:
        print('B __init__ called')
        self.b = 5
    
    def b_method(self):
        print("b Method called")
        

class C(A, B):
    def __init__(self) -> None:
        super().__init__()
        B.__init__(self)


c = C()

# print(c.a)
# c.b_method()
# print(c.b)
