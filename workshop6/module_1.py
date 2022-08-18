# from settings import WIDTH, HEIGHT, func as s_func
import settings
# from settings import *
# import settings as st

def func():
    print(__name__)


def main() -> None:
    """
    print(__name__)

    print(settings.WIDTH, settings.HEIGHT)
    # print(st.WIDTH)
    func()
    # s_func()
    settings.func()
    """
    

    my_list: list[int] = [
        num 
        for num in range(100) 
        if num % 2 == 0
        ]

    my_list: list[int] = [
        num 
        for num in range(0, 100, 2)
        ]
    
    my_list: list[int] = [*range(0, 100, 2)]
    my_list: list[int] = list(range(0, 100, 2))
    
    print(my_list)


if __name__ == '__main__':
    main()
