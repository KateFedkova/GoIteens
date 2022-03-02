import random
# Task 1 
#Написати функцію, яка приймає список чисел і повертає максимальне та мінімальне число

number = random.choices(range(1,56), k=10)
print(number)
def numbers(number):
    return f"max_number is {max(number)}, min_number is {min(number)}"
print(numbers(number))

# Task 2 
#Написати функцію, яка приймає 3 аргументи: 2 позиційних аргументи та один аргумент any_dictionary.
#Функція додає до словника один елемент(пару key:value) з двох прийнятих позиційних аргументів


def student_info(student, course, any_dictionary = {'age': '16', 'city':'Kiev', 'sex':'female'}):
    for element in any_dictionary:
        any_dictionary[f"{student}"] = f"{course}"
        return any_dictionary
print(student_info('Lilly','IT'))  


#Task 3 
#Відрефакторити калькулятор використовуючи функції

def welcome(username):
    print(f"""
    Hello, {username}!
    Welcome to our calculator!
    """)

def username():
    user_name = input( "Enter your username: ")
    return user_name


welcome(username())
   

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

def numbers():
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    if first_number.isdigit():
        if second_number.isdigit():
            return first_number, second_number
        else:
            print("Second number isn't a digit")
            exit() 
    else:
        print("First number isn't a digit")
        exit()                
    

def add_func(first_number, second_number):
    return int(first_number) + int(second_number)

def sub_func(first_number, second_number):
    return  int(first_number) - int(second_number)
    
def mul_func(first_number, second_number):
    return int(first_number) * int(second_number)

def div_func(first_number, second_number):
    return int(first_number) / int(second_number)


while True:
    option = menu()
    first_number, second_number = numbers()
    if option =='q':
        print("Ok, bye")
        break                
    elif option == 'add_func':
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