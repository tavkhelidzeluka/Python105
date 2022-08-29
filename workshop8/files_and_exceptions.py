"""
file_path: str = 'C:\\Users\\tavkh\\PycharmProjects\\Python105\\workshop8\\names.txt'


f = open(file_path, 'r')

data: list[str] = f.read() \
                        .split('\n')

print(data)

data = [name.upper() for name in data]
print(data)
data_to_write: str = '\n'.join(data)
f.close()

f = open(file_path, 'w')
# print(data_to_write)
f.write(data_to_write)

f.close()
"""

with open('C:\\Users\\tavkh\\PycharmProjects\\Python105\\workshop8\\numbers.txt') as f:
    try:
        number_list = [
            int(number.strip())
            for number in f.read().split(',')
        ]
       
    except ValueError:
        print("File must contain only numbers!")
        quit()
    # else:
    #     n: int | None = None
    #     for number in number_list:
    #         if n is None:
    #             n = number
    #             continue
    #         n /= number
        
    #     print(n)
    # finally:
    #     # f.close()
    #     print("This is executed No matter what!")
    
    try:
        n: int | None = None
        for number in number_list:
            if n is None:
                n = number
                continue
            n /= number
        
        print(n)
    except ZeroDivisionError:
        print("Divisor Must not be equal to 0")
        
    
