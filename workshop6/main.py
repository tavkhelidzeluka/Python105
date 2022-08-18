this_list: list[int] = [num for num in range(10)] # list comprehension
user_number: int = 50

"""
Algorithm

--- input
1. უნდა დავაგენერიროთ მთელი რიცხვების ლისტი
2. იუზერის მხრიდან უნდა შემოვიტანოთ რაღაც მთელი რიცხვი
--- processing / result
3. თითეული რიცხვი შევადაროთ იუზერის მიერ შემოტანილ რიცხვს
    - თუ ვიპოვეთ ეს რიცხვი
        - დაბეჭდოს ამ ელემენტის პოზიცია და გააჩეროს ციკლი
    - თუ ვერ ვიპოვეთ საერთოდ ეს რიცხვი
        - ეს რიცხვი ვერ მოიძებნა

"""


"""
for index in range(len(this_list)):
    if this_list[index] == user_number: 
        print(f"Position: {index}")
        break
else:
    print('Number is not in the list')
"""

x = 5  # Global variable

def f():
    y = 6 # Local scope variable
    print(x, y)


def f1():
    y = 7
    print(x, y)
    

def change_x():
    # global x
    # print(f'old x {x}')
    # Shadowing
    x = 17 # Creates local variable 
    print(f'new x {x}')
    
    
# print(x, y)
# f()
# f1()

change_x()
print(f'Global {x}')