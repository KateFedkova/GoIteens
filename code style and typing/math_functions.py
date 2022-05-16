from typing import Union


def menu():
    '''All available functions'''
    options = input("""
    You can:
             - add        : add_func
             - subtract   : sub_func
             - multiply   : mul_func
             - divide     : div_func

    q - quit
    Choose from the list: """)
    return options


def add_func(first_number: Union[int, float],
             second_number: Union[int, float]) -> float:
    '''Add 2 numbers'''
    return float(first_number) + float(second_number)


def sub_func(first_number: Union[int, float],
             second_number: Union[int, float]) -> float:
    '''Substract 2 numbers'''
    return float(first_number) - float(second_number)


def mul_func(first_number: Union[int, float],
             second_number: Union[int, float]) -> float:
    '''Multiply 2 numbers'''
    return float(first_number) * float(second_number)


def div_func(first_number: Union[int, float],
             second_number: Union[int, float]) -> float:
    '''Divide 2 numbers'''
    return float(first_number) / float(second_number)
