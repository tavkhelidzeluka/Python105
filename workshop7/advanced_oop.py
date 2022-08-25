from datetime import datetime
import random
import time

# Static attributes & methods
class Student:
    # static Attribute
    university: str = 'MIT'
    founded_year: int = 1976
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
    
    def calculate_gpa(self) -> float:
        self.score = random.randrange(1, 4)
        return self.score
    
    @staticmethod
    def university_age() -> int:
        return datetime.today().year - Student.founded_year

    
        
"""
s1: Student = Student("Josh")
# s1.score = "Score"
s2: Student = Student("Jane")

print(s1.university, s1.name, s1.calculate_gpa())
# print(s1.score)

# print( Student.gpa(s1) )
print(s2.university, s2.name, s2.calculate_gpa(), s2.university_age())
print(Student.university, Student.university_age())
"""

# Wrappers / Decorators

def execution_time(func):
    def wrapper():
        # print("Before Call")
        start_time = time.time()
        func()
        print(f"Function Took {(time.time() - start_time):.0f} seconds to run")

    return wrapper


@execution_time
def big_operation() -> None:
    time.sleep(random.randint(0, 5))


@execution_time
def small_operation() -> None:
    pass


"""
# big_operation()

# execution_time(big_operation)()
big_operation()
small_operation()
"""


# Inheritance

class Animal:
    # Parent
    def __init__(self, 
                 name: str, 
                 age: int, 
                 has_tail: bool = True) -> None:
        self.name = name
        self.age = age
        self.has_tail = has_tail
    
    def animal_sound(self) -> None:
        raise NotImplementedError()
    
    def move(self) -> None:
        print(f'{self.name} is Moving!')


class Dog(Animal):
    # def __init__(self, collar_color: str, name: str, age: int, has_tail: bool = True) -> None:
    #     super().__init__(name, age, has_tail)
    #     self.collar_color = collar_color
        
    def __init__(self, collar_color: str, *args) -> None:
        super().__init__(*args)
        self.collar_color = collar_color
    # Child

    # def bark(self):
    #     print(f'{self.name} - woof woof!')

    def animal_sound(self) -> None:
        # super().move()
        print(f'{self.name} - woof woof!')
    
    # def move(self) -> None:
    #     print(f'{self.name} is crawling!')


class Cat(Animal):
    # Child
    def animal_sound(self) -> None:
        print(f'{self.name} - Moew Moew!')


class Horse(Animal):
    # Child
    def animal_sound(self) -> None:
        print(f'{self.name} - Horse Sounds!')


class Pig(Animal):
    def animal_sound(self) -> None:
        # overriding
        print(f'{self.name} - Pig Sounds!')


class Cow(Animal):
    def animal_sound(self) -> None:
        print(f'{self.name} - Moo Moo!')


names: list[str] = [
   "Bella", "Luna", "Lucy", "Daizy", "Zoe", "Lily", "Lola", "Bailey", "Stella", "Molly",
   "Max", "Charlie", "Milo", "Buddy", "Rocky", "Bear", "Leo", "Duke", "Teddy", "Tucker"
]

def get_details() -> tuple[str, int]:
    return random.choice(names), random.randint(0, 15)

farm: list[Animal] = [
    Dog("red", *get_details()),
    Cat(*get_details()),
    Cow(*get_details()),
    Cow(*get_details()),
    Pig(*get_details()),
    Pig(*get_details()),
    Pig(*get_details()),
    Pig(*get_details()),
    Pig(*get_details()),
    Pig(*get_details()),
    Horse(*get_details()),
    Horse(*get_details()),
    Horse(*get_details()),
    Horse(*get_details()),
    Cow(*get_details()),
    Cow(*get_details()),
    Cow(*get_details()),
    Cow(*get_details()),
]


for animal in farm:
    # animal.bark()
    # animal.move()
    animal.animal_sound()
    print(animal.name, animal.age)