#Написати функцію піднесення до степеня, яка приймає 2 числа: перше-число, а друге-степінь
#Написати декоратор, який буде показувати час виконання функції щоразу

from functools import wraps


def my_timer(func):
    import datetime

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} function: done in {datetime.datetime.today()}")
        return result
    return wrapper


@my_timer
def power(number, power):
    return number ** power


print(power(3, 9))
