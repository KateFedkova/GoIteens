from pprint import pprint
# Task 1
# Використовуючи класи, написати програму - контактну книгу 

def menu():
    options = input(""" 
    Привіт!
    Ви можете:
             - Додавати контакт користувача    : add_func
             - Видаляти контакт користувача    : del_func
             - Видозмінювати дані користувача  : change_func
             - Пошук користувачів по місту     : city_search_func
             - Пошук користувача по емейлу     : email_search_func
             - Виводити кількість контактів    : num_of_cont_func
             - Список всіх контактів           : all_contacts
             
     q - quit 
     Оберіть:  """)
    return options 


class Phonebook:
    contacts = []
    numbers_of_contacts = 0
    def __init__(self, tel_number,first_name,last_name,city):
        self.tel_number = tel_number
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.email = f"{first_name}_{last_name}.{city}@{city}.com"    

        
    def add_func():
        tel_number =  input("Введіть номер телефону(12 цифр): ")
        if len(tel_number) != 12:
            return "Неправильна кількість цифр!"  
            exit()
        first_name = input("Введіть ім'я: ").capitalize()
        last_name = input("Введіть призвіще: ").capitalize()
        city = input("Введіть місто: ").capitalize()
        contact = Phonebook(tel_number,first_name,last_name,city)                                                                                     
        if contact.__dict__ not in Phonebook.contacts:
            Phonebook.contacts.append(contact.__dict__)
            Phonebook.numbers_of_contacts += 1
            return "Вітаю! Контакт уcпішно додано"
        else: 
            return "Такий контакт вже є!"     
        
    def all_contacts():
        return Phonebook.contacts
   
    
    def num_of_cont_func():
        return Phonebook.numbers_of_contacts
        
    def change_func():
        new_name = input("Введіть нову інформацію!\nВведіть ім'я: ").capitalize()
        new_last_name = input("Введіть призвіще: ").capitalize()
        new_tel_num = input("Введіть телефон: ").capitalize()
        new_city = input("Введіть нове місто : ").capitalize()
        for element in Phonebook.contacts:
            if any([new_name, new_last_name, new_tel_num, new_city]):
                element['first_name'] = new_name
                element['last_name'] = new_last_name
                element['tel_number'] = new_tel_num  
                element['city'] = new_city 
                return "Успішно змінено!"
            
    def city_search_func():
        city_search = input("Введіть місто: ").capitalize()
        for element in Phonebook.contacts:
            if element['city'] == city_search:
                return element['first_name'],element['last_name']
            else:
                return "Hе знайдено"
                
    def email_search_func():
        email_search = input("""Введіть email у форматі - Ім'я_Призвіще.Місто@Місто.com 
        : """)
        for element in Phonebook.contacts:
            if element['email'] == email_search:
                return (element['first_name'],element['last_name'])
            else:
                return "Hе знайдено"
           
        
    def del_func():
        del_name = input("Введіть ім'я користувача,якого ви хочете видалити: ").capitalize()
        del_surname = input("Введіть призвіще користувача,якого ви хочете видалити: ").capitalize()
        for element in  Phonebook.contacts:
            if element['first_name'] == del_name:
                if element['last_name'] == del_surname:
                    Phonebook.contacts.remove(element)
                    return "Успішно видалено!"

        
        
while True:
    option = menu()
    if option == "q":
        print("OK,bye")
        break
    elif option == "add_func":
        print(Phonebook.add_func())
    elif option == "del_func":  
        print(Phonebook.del_func())     
    elif option == "change_func":
        print(Phonebook.change_func())      
    elif option == "city_search_func":
        print(Phonebook.city_search_func())  
    elif option == "email_search_func":
        print(Phonebook.email_search_func())
    elif option == "num_of_cont_func":
        print(Phonebook.num_of_cont_func())
    elif option == "all_contacts":
        pprint(Phonebook.all_contacts())
    else:
        print(f"{option} isn't developed yet") 