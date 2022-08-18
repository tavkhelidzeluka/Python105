from datetime import date

class Dog:
    def __init__(self, name: str, age: int = 0) -> None:
        # Method (Not a Function)
        self.name = name  # attribute
        self.age = age  # attribute
        self.nickname = ""
    
    def bark(self) -> None:
        # Behavior
        print(self.name, self.age, sep='-')
        
    def __str__(self) -> str:
        # magic method
        return f'{self.name}, {self.age}'


"""
# instance / object 
my_dog: Dog = Dog("Mailo")  # instantiate
my_dog_2: Dog = Dog("Rubert", 10)

# print(my_dog.name, my_dog.age)
# print(my_dog_2.name, my_dog_2.age)
my_dog.bark()
my_dog_2.bark()

my_dog.age += 1
# del my_dog.age
my_dog.nickname = "mai" # Don't do this
print(my_dog, my_dog.nickname)
# print(my_dog_2, my_dog_2.nickname)
"""


class Brand:
    def __init__(self, name: str, founded: date) -> None:
        self.name = name
        self.founded = founded

    def __str__(self) -> str:
        return self.name

class Car:
    def __init__(self, brand: Brand, model: str, year: int, color: str) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def __str__(self) -> str:
        return f'{self.year} {self.brand} {self.model} - {self.color}'

    def __gt__(self, other) -> bool:
        # Greater Than
        return self.year > other.year
    
    def __le__(self, other) -> bool:
        # Less Than or Equal
        return self.year <= other.year

    def __eq__(self, other) -> bool:
        # Equality
        return self.year == other.year
    
    def honk(self) -> None:
        print(f'{self}: beep beep!')
    
        

mercedes: Brand = Brand("Mercedes-Benz", date(year=1926, month=5, day=28))
tesla: Brand = Brand("Tesla, Inc.", date(year=2003, month=6, day=1))

gle_white: Car = Car(mercedes, "GLE", 2022, 'white')
gle_black: Car = Car(mercedes, "GLE", 2022, 'black')
g = gle_black

tesla_model_s: Car = Car(tesla, "Model S", 2016, "red")

"""
# print(gle_white.brand, gle_white.model)
print(gle_white)
print(gle_black)

print(tesla_model_s)

print(tesla_model_s > gle_black)
print(tesla_model_s <= gle_black)
print(gle_white == gle_black)
print(gle_white is gle_black)
print(g is gle_black)
"""
tesla_model_s.honk()

