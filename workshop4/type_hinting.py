from typing import TypedDict
from datetime import date, datetime, timedelta


class User(TypedDict):
    username: str
    birth_date: date
    gender: str


users: list[User] = [
    {
        'username': "Nika",
        'birth_date': date.today(),
        'gender': "Male"
    }
]


for user in users:
    user['age'] = 0

print(users)

a = None
# name_1 = input("name_1: ")
# name_2 = input("name_2: ")
name_1: str = "goervweiruvthnweouihvtnworuitvn"
name_2: str = "goervweiruvthnweouihvtnworuitvn"

print(f'{name_1 is name_2 = }')
# print(a is None)
# print("Nick" == "Nick")

print(5 is 5)

# print(500000000000000000000000000 is 500000000000000000000000000)
print('-' * 10, 'Dates', '-' * 10)

d: date = date(year=1665, month=6, day=5)
print(d)
print(date(2001, 1, 1))
print(date(2001, 1, 2) - date(2001, 1, 1))
print((date.today() - d).days / 365)
print('-' * 10, 'Datetime', '-' * 10)
birth_datetime: datetime = datetime(2001, 1, 1, 14, 45, 45)
print(birth_datetime)

time_passed: timedelta = datetime.now() - birth_datetime
print(time_passed.days // 365)
