# Task 1 
# наповнити порожній список значеннями від 0 до 100, які кратні 5 та 7 одночасно
listt = [ ]
number = 0
while  number < 100:
    if number % 5 == 0 and number % 7 == 0:
        print(number)
    number += 1

# Task 2 
# Повернути суму чисел усіх елементів списку

list_1 = [2,4,7,84,598,6378]
index = 0
number = 0
while index != len(list_1):
    number = number + int(list_1[index])
    print(f" previous number + next number: {number} ")
    index += 1 


#Task 3 
#вивести тип кожного значення через while

given_list = [False, 0, 'str', '123', 'hello', '%', 1.2, 1]

index = 0 
while index != len(given_list):
   print(type(given_list[index]))
   if index == len(given_list):
       break
   index += 1

#Task 4 
#вивести на екран найбільше та найменше число кожного списка,спільні значення з двох списків

list_0 = [2,46,8,4,6]
max_number = max(list_0)
print(max_number)
min_number = min(list_0)
print(min_number)

list_2 = [3,4,6,89,0]
max_number = max(list_2)
print(max_number)
min_number = min(list_2)
print(min_number)

c = list(set(list_0) & set(list_2))
print(c)