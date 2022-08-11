from pprint import pprint
from typing import Any
age = 21

# if age > 18:
#     # Code Fragment
#     print("adult")
# elif age < 30 or age == 18:
#     print("young adult!")
# else:
#     # Code Fragment
#     print('Not adult')

# if - elif - else chaining
if age < 18:
    # Code Fragment
    print('Not adult')
elif age < 30:
    print("young adult!")
else:
    # Code Fragment
    print("adult")


if age < 18:
    print('candy')
else:
    print('no candy for you')

if age % 2 == 0:
    print('age is even')
# else:
#     print('age is odd')

if age % 3 == 0:
    print('age is divisible by 3')
else:
    print('age is not divisible by 3')


print('-' * 10, 'dict', '-' * 10)
# Map, object

user = {
    # Key     : Value
    'username': 'Legend27',
    
    'password': 'Legend27',
    'age': 27,
    'gender': 'Female',
}

print(user)
print(user['username'])

user['username'] = "Legend28"
print(user['username'])

user['pet'] = "Dog"
print(user)

# print(user['c'])

new_user = dict(username="User2") # {}
print(new_user)
new_user['age'] = 17
print(new_user)

new_user.pop('age')
# new_user.pop('age', None)
# del new_user['age']
print('after removing age key: ', new_user)

# print(new_user.get('age'))
print('-' * 10, 'Looping through items', '-' * 10)

for key, value in user.items():
    print(key, value)

print('-' * 10, 'Looping through keys', '-' * 10)

for key in user.keys():
    print(key)

print('-' * 10, 'Looping through values', '-' * 10)
for value in user.values():
    print(value)


user_1 = {
    'name': 'nika',
    'age': 17
}

user_2 = {
    'name': 'Gio',
    'age': 17
}

user_1['friends'] = [user_2]
user_2['friends'] = [user_1]

print(user_1)

print('-' * 10, 'List of Users', '-' * 10)
users = [
    {
        "name": "Irakli Lezhava",
        "icon": "https://lh3.googleusercontent.com/ogw/AOh-ky1xv_TnxhJNVeDzXaXl5pxcQN6NiisG3Xjw1UYXRA=s32-c-mo",
        "muted": True
    },
    {
        "name": "Luka Tavkhelidze",
        "icon": "https://lh3.googleusercontent.com/ogw/AOh-ky1xv_TnxhJNVeDzXaXl5pxcQN6NiisG3Xjw1UYXRA=s32-c-mo",
        "muted": False
    }
]
favorite_languages = [
    {
        'user': 'jen',
        'language': 'python'
    },
    {
        'user': 'sarah',
        'language': 'c'
    },
    {
        'user': 'edward',
        'language': 'ruby'
    }
]

for user in favorite_languages:
    if user['user'] == 'sarah':
        print(user['language'])
        break


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages['sarah'])

pprint(users)

user: dict[str, Any] = {
    'name': "Mari",
    'job': {
        "title": "Software Developer",
        "salary": 140_000,
    }
}

pprint(user)

 
age: int = 18
name: str = "Hello"
friends: list[str] = ['nika', 'luka', 'levani', 'mari', 'ana']

# print(age + name)
friends.append(25)
