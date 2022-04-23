import random
#Згенерувати квадрати значень від 0 до 100000 і записати у різні файли

def squares():
    for number in range(100000):
        result = number*number
        yield result
        if result % 3 == 0:
            f = open('3.txt', 'a')
            f.write(f"{result}\n")
        elif result % 5 == 0:
            f = open('5.txt', 'a')
            f.write(f"{result}\n")
        elif result % 2 == 0:
            f = open('pair.txt', 'a')
            f.write(f"{result}\n")

squares = squares()
for el in squares:
    print(el)


#Hаписати генератор безпечних паролів. Згенерувати і записати 1000 паролів в файл

def generate_password():
    for i in range(1000):
        password = create_password()
        f = open('passwords.txt', 'a')
        f.write(f"{password}\n")
        yield password


def create_password():
    password = ''
    while len(password) < 8:
        elements = '!@$%^&*_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        password += random.choice(elements)
    if password.find('!@$%^&*_') and any(el.isupper() for el in password) and any(el.islower() for el in password) and any(el.isdigit() for el in password):
        return password
    else:
        return f"{password} - недостатньо безпечний"


passwords = generate_password()
for el in passwords:
    print(el)

#Hаписати власний генератор, який повертає значення як це робить range():може приймати start, end, step і поверне відповідні згенеровані значення

def own_range(start=0, end=None, step=1):
    if end is None:
        end, start = start, 0

    if end > start and step < 0:
        yield None
        exit()

    elif end < start and step > 0:
        yield None
        exit()

    if start < end:
        while start < end:
            yield start
            start += step

    elif start > end:
        step = -1
        while start > end:
            yield start
            start += step

numbers = own_range(3, 9, 5)
for el in numbers:
    print(el)

#Hаписати програму яка генерує одне рандомне число random_number від 0 до 100, а потім генерує рандомні числа від 0 до 100 поки не вгадає random_number

def random_number():
    first = random.randint(0, 100)
    print(f'The right number is {first}')
    second = random.randint(0, 100)
    while first != second:
        yield second
        second = random.randint(0, 100)
    print(second)
    print('Right')

first_second = random_number()
for el in first_second:
    print(el)
