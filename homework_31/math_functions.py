def menu():
    options = input("""
    You can:
             - add        : add_func
             - subtract   : sub_func
             - multiply   : mul_func
             - divide     : div_func

     q - quit 
     Choose from the list: """)
    return options


def add_func(first_number, second_number):
    return float(first_number) + float(second_number)


def sub_func(first_number, second_number):
    return float(first_number) - float(second_number)


def mul_func(first_number, second_number):
    return float(first_number) * float(second_number)


def div_func(first_number, second_number):
    return float(first_number) / float(second_number)