'''Task 1
Відрефакторити калькулятор:винести усі функції в окремий файл, винести усі перевірки/валідації в окремий файл'''

from math_functions import add_func, sub_func, mul_func, div_func, menu
from number_validation import numbers, number_validation

def welcome(username):
    print(f"""
    Hello, {username}!
    Welcome to our calculator!
    """)

def username():
    user_name = input("Enter your username: ")
    return user_name

welcome(username())


while True:
    option = menu()
    if option == 'q':
        print("Ok, bye")
        break
    first_number, second_number = numbers()
    number_validation(first_number, second_number)
    if number_validation(first_number, second_number) != False:
        if option == 'add_func':
            print(add_func(first_number, second_number))
        elif option == 'sub_func':
            print(sub_func(first_number, second_number))
        elif option == 'mul_func':
            print(mul_func(first_number, second_number))
        elif option == 'div_func':
            if second_number == '0':
                print("Dividing by zero is not allowed")
            else:
                print(div_func(first_number, second_number))
        else:
            print(f"{option} isn't developed yet")
    else:
        print("Can't be digits")
