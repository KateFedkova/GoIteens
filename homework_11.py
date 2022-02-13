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

def student_info(student,course,any_dictionary={'age': '16', 'city':'Kiev', 'sex':'female'}):
    return  f"{student}: {course}"
result = student_info('Lilly','IT')
print(result)
any_dictionary = {'age': '16', 'city':'Kiev', 'sex':'female'}
any_dictionary['Lilly'] = 'IT'
print(any_dictionary)
 

# Task 3 
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
 
    
def add_func():
    add_result = first_number + second_number
    print("Result",add_result)
def sub_func():
    sub_result = first_number - second_number
    print("Result",sub_result)    
    
def mul_func():
    mul_result = first_number * second_number
    print("Result",mul_result)    

def div_func():
    if second_number == 0:
        print( "Dividing by zero is not allowed")
    div_result = first_number / second_number
    print("Result",div_result)    


while True:
    option = menu()
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if option =='q':
        print("Ok, bye")
        break
    elif option == 'add_func':
        add_func()
    elif option == 'sub_func':
        sub_func()
    elif option == 'mul_func':
        mul_func()
    elif option == 'div_func':
        div_func()
    else:
        print(f"{option} isn't developed yet")