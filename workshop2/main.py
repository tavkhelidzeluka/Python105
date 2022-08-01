# Type Casting

my_number = "5"

print(type(my_number))
print(int(my_number) + 7)
print(my_number + "7")

print(float("5.6") + 0.4)

# print(float("5.6f"))
# print(int("ughoirvr"))

# Truthy and Falsy
print(bool(1), bool(-1), bool(0))
print(bool(""), bool("Hello"))
print(bool([]), bool([1, 2, 3, 4]))

# Data Structures list

# name_1 = "Liza"
# name_2 = "Nika"
student_names = ["Nika", "Liza", "Irakly", "Elene", "Natia", "Shavla"]  # Initialization
my_numbers = [1, 2, 3, 4, 5, 6, 7]

print(student_names)

print(student_names[0])
print(my_numbers[0])

# Index Error 
# print(my_numbers[7])

# print('Last element is:',  my_numbers[6])
print(f'Last element is: {my_numbers[6]}')

my_numbers[1] = 25
print(my_numbers)

my_numbers.append(17)
my_numbers.append(25)
my_numbers.append(12)
my_numbers.append(31)
print(my_numbers)

my_numbers.insert(0, 25)
my_numbers.insert(5, -125)
print(my_numbers)

my_numbers.pop()
my_numbers.pop(5)
# Index Error
# my_numbers.pop(127)
my_numbers.append(-125)

print(my_numbers)


my_numbers.sort()
print(my_numbers)

my_numbers.sort(reverse=True)
print(my_numbers)

print('Before Sorting:', student_names)
student_names.sort()
print('After Sorting:', student_names)

# print(ord("A"))

print(my_numbers[:])

print(my_numbers[5:7])
print(my_numbers[:5:2])
print(my_numbers[::-1])
print(my_numbers)


print(len(my_numbers))
print('last element is:', my_numbers[len(my_numbers) - 1])
print('last element is:', my_numbers[-1])


# Loop for
print('-' * 10, 'For Loops', '-' * 10)

my_numbers = [-91, 2, 32, 45]
for number in my_numbers:
    print(number ** 2)
    # print(my_numbers)

# print(my_numbers)

print('-' * 10, 'Students names', '-' * 10)

for name in student_names:
    print(name)
    print(f'Hello, I am {name}')


print('-' * 10, 'Range Function', '-' * 10)
for i in range(10):
    print(i)

print('-' * 10, 'Range Function with steps and start point', '-' * 10)
for i in range(5, 10, 2):
    print(i)


print('-' * 10, 'Retrieving numbers from my_numbers list with Range function', '-' * 10)
for i in range(len(my_numbers)):
    print(i, my_numbers[i])

print('-' * 10, 'Retrieving numbers from my_numbers list with enumerate function', '-' * 10)
for index, element in enumerate(my_numbers):
    print(index, element)

# User Input
print('-' * 10, 'Input', '-' * 10)

my_number = int(input("Enter Number: "))

print(my_number + 3, type(my_number))
