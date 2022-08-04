# Boolean Operators 
import time

# tomorrow_is_rain = True
# tomorrow_will_rain = True 
# tomorrow_will_thunderstorm = False

# print(tomorrow_will_rain == tomorrow_is_rain)

print(f'{5 == 5 = }')
# print(f'5 != 5 = {5 != 5}')
print(f'{5 != 5 = }')
print(f'{5 < 5 = }')
print(f'{5 <= 5 = }')
print(f'{5 > 5 = }')
print(f'{5 >= 5 = }')

print('-' * 10, 'And/Or Operator', '-' * 10)
my_number = 9
print(f'{6 < my_number and my_number < 12 = }')
print(f'{-9 > my_number or my_number > 5 = }')
"""
print('-' * 10, 'Conditional Statements', '-' * 10)
age = int(input('Enter your age: '))

# if age > 18 and age < 30:
if 18 < age < 30:
    print('You are an young adult')
else:
    print('You are not adult')

"""
print('' * 20)
print(f'{True and True and False}')
print(f'{True and False or False = }')
print(f'{True or False or False = }')
print(f'{True or False and False = }')

print(f'{(True or False) and False = }')

print('-' * 10, 'while loop', '-' * 10) 
i = 0
n = [1, 2, 3, 4, 5]
while i < len(n):
    # Code Fragment | Body
    print(n[i])
    i += 1

print('-' * 10, 'loops (continue, break)', '-' * 10) 
i = 0
while True:
    # i % 2 -> 0, 1
    if i == 5:
        break
    i += 1

    if not i % 2:
        # pass
        continue

    print('hello')

print('-' * 10, 'not operator', '-' * 10) 

print(f'{not (not True and not False) = }')
print(f'{not not True and not False = }')

print('-' * 10, 'tuple', '-' * 10) 
my_numbers = (1, 2, 3, 4, 5)

print(type(my_numbers), my_numbers)
for num in my_numbers:
    print(num)

print('-' * 10, 'generators, comprehension', '-' * 10) 
nums = []
s = time.time()

for i in range(1000000):
    if i % 3 == 0 and i % 5 == 0:
        nums.append(i)

print(f'{time.time() - s}')
# print(nums)
s = time.time()

nums = [num for num in range(1000000) if num % 3 == 0 and num % 5 == 0]
print(f'{time.time() - s}')

# print(nums)
