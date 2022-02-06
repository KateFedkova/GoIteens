import random
# Task 1 
#використовуючи enumerate() створіть словник для списку,який складається з 20 рандомнич значень від 0 до 100

list_random = random.choices(range(0,101),k=20)
print(list_random)
for elements in enumerate(list_random):
    print(dict(enumerate(list_random)))
    break

#Task 2
#створіть словник family в якому по іменах будуть доступні словники для кожного члена сім'ї/родини

family_dict = {
    'Mother': {
        'name':'Vera',
        'sex':'female',
        'job':'teacher'
    },
    'Father':{
        'name':'Alex',
        'sex':'male',
        'job':'engineer'
        },
    'I':{ 
        'name':'Kate',
        'sex':'female',
        'school':'Gymnasium 11'
        },
}

#Task 3
#з вашого словника family виведіть тільки імена з усіх записів
print(family_dict['Mother']['name'])
print(family_dict['Father']['name'])
print(family_dict['I']['name'])

#Task 4 
#Напишіть скрипт, з допомогою якого користувач може перевірити чи значення(ключ або значення),є у вашому словнику family і якщо воно є то виведіть словник, в якому це значення зустрічається

element_to_find = input("Enter value or key you want to search for: ")
for family,family_info in family_dict.items():
    family_info_list= list(family_info.items())
    for element in family_info_list:
        if element_to_find  in element:
           print(f"{element_to_find} was found in \n{family}:{family_info}")