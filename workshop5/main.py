from datetime import date
from typing import TypedDict, Any
from module_1 import pow

def c(x, y):
    print(f'{x = }')
    print( x ** 2 + y )
    

def f(x):
    print(f'გამარჯობა {x}')
    
"""
x = 2
y = 1  
c(x, y)

c(1, 2)
c(x=1, y=2)
c(1, y=2)
# c("1", 2)

f("Nika")
f("Elene")
f(5)
"""

def format_name(first_name: str, last_name: str, middle_name: str | None = None):
    # print(f'{first_name}-{middle_name}-{last_name}')
    if not middle_name:
        print(first_name, last_name)
    else:
        print(first_name, middle_name, last_name, sep=' ')
"""
format_name("Muhamed", "Ali", "Chritopher")
format_name("Muhamed", "Ali", middle_name="Chritopher")
format_name("Muhamed", last_name="Ali", middle_name="Chritopher")
format_name(first_name="Muhamed", last_name="Ali", middle_name="Chritopher")

format_name("Irakly", "Lezhava")
"""

def shekribe(x: float, y: float, *args, multiplier: float = 1) -> float:
    # print(args)
    # print(x + y)
    s: float = x + y
    for num in args:
        s += num
    
    return s * multiplier

# print(None)
"""
print( shekribe(5, 5, multiplier=2) )
print( shekribe(5, 5, 7, 8, 9, 10, -1,17, 1.1) )
"""

class UserDict(TypedDict):
    name: str
    date_of_birth: date


def create_user(name: str, date_of_birth: date) -> UserDict:
    return {
        'name': name,
        'date_of_birth': date_of_birth
    }

def create_advanced_user(name: str, **kwargs) -> dict[str, Any]:
    # print(name)
    # print(kwargs)
    """
    udpate
    
    Pseudo code
    1. names-ს შევინახავ დიქშენარიში
    2. ამ დიქშენარის განვაახლებ kwargs-ის დიქშენარით
    3. დავაბრუნებ ამ ახალ დიქშენარის
    """
    # new_user: dict[str, Any] = {}
    
    # new_user['name'] = name
    # new_user.update(kwargs)
    # return new_user
    return {
        'name': name,
        **kwargs
    }
    

"""
user_1: UserDict = create_user("John", date.today())
print(user_1)
"""
"""
kwargs = {
    # 'name': "Luka",
    'age': 16,
    'car': "Tesla",
    'studies': "Harvard"
}
# print( create_advanced_user("luka", age=16, car="Tesla", studies="Harvard") )
print( create_advanced_user("luka", **kwargs) )


{
    "name": "luka",
    "age": 16,
    "car": "Tesla",
    "studies": "Harvard"
}
names: list[str] = ["Philip", "John", "Jane"]
print(names, sep=" <-> ")
print(*names, sep=" <-> ")
print("Philip", "John", "Jane", sep=" <-> ")
"""

print( pow(5) )