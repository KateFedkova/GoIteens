# Task 1
#Написати калькулятор для операцій + - * /

print('Welcome to calculator!')
open = input('''We have a few options: + - * /
Choose the one you like: ''')
if open == '+':
    first = input('Enter first number: ')
    if first.isdigit():
        second = input('Enter second number: ')
        if second.isdigit():
            print(f"{first} + {second} = {int(first) + int(second)}")
        else:
            print(f"{second} isn't digit")
    else:
        print(f"{first} isn't digit") 
elif open == '-':
    first = input('Enter first number: ')
    if first.isdigit():
        second = input('Enter second number: ')
        if second.isdigit():
            print(f"{first} - {second} = {int(first) - int(second)}")
        else:
            print(f"{second} isn't digit")        
    else:
        print(f"{first} isn't digit")
elif open == '*':
    first = input('Enter first number: ')
    if first.isdigit():
        second = input('Enter second number: ')
        if second.isdigit():
            print(f"{first} * {second} = {int(first) * int(second)}")
        else:
            print(f"{second} isn't digit")        
    else:
        print(f"{first} isn't digit")
elif open == '/':
    first = input('Enter first number: ')
    if first.isdigit():
        second = input('Enter second number: ')
        if second == '0':
                    print('Dividing by zero is not allowed')        
        elif second.isdigit():
                print(f"{first} / {second} = {int(first) / int(second)}")
        else:
            print(f"{second} isn't digit")
    else:
        print(f"{first} isn't digit")    
else:
    print("Not valid operation")