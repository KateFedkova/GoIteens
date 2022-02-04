import random
import re 
# Task 1 
# створити два списка рандомно згенерованих значень від 0 до 10 по 10 значень в кожному

first_list = random.choices(range(0,11),k =10)
print(first_list)
second_list = random.choices(range(0,11),k =10)
print(second_list)

# вивести унікальні значення кожного списка
print(set(first_list))
print(set(second_list))

# вивести унікальні значення, які зустрічаються в обох списках
c = list(set(first_list) & set(second_list))
print(c)

# Task 2 
#створити список з десяти рандомно згенерованих значень від 0 до 100

list_ = random.choices(range(0,101),k =10)
print(list_)

#вивести кожне значення через цикл while

index = 0
while index <  len(list_):
    print(list_[index])
    index += 1

# вивести кожне значення через цикл for

for number in list_:
    print(number)

# створити список з десяти рандомно згенерованих значень від 10 до 100 через list comprehension

list_comprehension = ([random.randint(10,101) for element in range(0,10)])
print(list_comprehension)

# Task 3 
#створити список рандомно згенерованих значень від 20 до 100, які діляться на 2 і 4 без остачі

#написати цей чикл через while

number = 20
while number < 101:
  if number % 2 == 0:
    if number % 4 == 0:
      print(number)
  number += 1
    

#через for
for number in range(20,101):
    if number % 2 == 0:
        if number % 4 ==0:
            print(number)
            index += 1
            
 #через list comprehension
                              
random_list =  [number for number in range(20, 100) if number % 2 == 0 and number % 4 == 0 ]
print(random_list)

# Task 4 
#створити список і вивести кортежі в який міститься індекс і елемент кожного значення зі списку

list_5 = random.choices(range(0, 100), k=5)
print(list_5)

for tuple_1 in enumerate(list_5):
    print(tuple_1)    


# Task 5 
#написати програму, яка б перевіряла введений користувачем пароль на валідність умови наступні:
#мінімум 8 символів,велика буква,маленька буква,цифра,символ
operation = input("Enter your password: ")

while index != len(operation):
    if len(operation) < 8 :
        print("The password has less than 8 characters")
        break
    elif  operation.isdigit():
        print("Must be lettres")        
        break
    elif operation.islower():
        print("One letter must be capitalized")
        break
    elif re.search('[^\w-]|_', operation):
        print("Well done!")
        break