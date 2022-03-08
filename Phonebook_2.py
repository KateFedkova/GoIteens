# Task 1
# Використовуючи класи, написати програму - контактну книгу 

def menu():
    options = input(""" 
    Привіт!
    Ви можете:
             - Додавати контакт користувача        : add_func
             - Видаляти контакт користувача        : del_func
             - Видозмінювати дані користувача      : change_func
             - Пошук користувачів по місту/емейлу  : city_or_email_search_func    
             - Виводити кількість контактів        : num_of_cont_func
             - Список всіх контактів               : all_contacts
             
     q - quit 
     Оберіть: """)
    return options 


class Phonebook:
    numbers_of_contacts = 0
   
    def __init__(self, contact_storage):
        self.contact_storage = contact_storage  

    def valid_tel_num(self):
        if len(tel_number) != 12:
            print("Неправильна кількість цифр!") 
            exit()
        else:
            return tel_number

        
    def add_func(self):
        global tel_number
        tel_number =  input("Введіть номер телефону(12 цифр): ")
        self.valid_tel_num()
        if self.valid_tel_num() != "Неправильна кількість цифр!":
            first_name = input("Введіть ім'я: ").capitalize()
            last_name = input("Введіть призвіще: ").capitalize()
            city = input("Введіть місто: ").capitalize()
            email = f"{first_name}_{last_name}.{city}@{city}.com"
            result_dict = {'city': f"{city}", 'first_name': f"{first_name}", 'last_name': f"{last_name}", 'tel_number': f"{tel_number}", 'email': f"{email}"}
            if result_dict not in self.contact_storage:
                self.contact_storage.append(result_dict)
                self.numbers_of_contacts += 1
                return "Вітаю! Контакт уcпішно додано"
            else: 
                return "Такий контакт вже є!"     
            
        
    def all_contacts(self):
        return self.contact_storage
   
    
    def num_of_cont_func(self):
        return  self.numbers_of_contacts
        
    def change_func(self):
        new_name = input("Введіть нову інформацію!\nВведіть ім'я: ").capitalize()
        new_last_name = input("Введіть призвіще: ").capitalize()
        new_tel_num = input("Введіть телефон: ").capitalize()
        new_city = input("Введіть нове місто : ").capitalize()
        for element in self.contact_storage:
            if any([new_name, new_last_name, new_tel_num, new_city]):
                element['first_name'] = new_name
                element['last_name'] = new_last_name
                element['tel_number'] = new_tel_num  
                element['city'] = new_city 
                return "Успішно змінено!"
   
   
   
   
    def city_or_email_search_func(self):
        city_or_email_search = input("Введіть місто або емейл у форматі - Ім'я_Призвіще.Місто@Місто.com : ").capitalize()
        for element in self.contact_storage:
            if  element['city'] or element['email'] == city_or_email_search:
                return element['first_name'],element['last_name']
            else:
                return "Hе знайдено"
    
           
        
    def del_func(self):
        del_name = input("Введіть ім'я користувача,якого ви хочете видалити: ").capitalize()
        del_surname = input("Введіть призвіще користувача,якого ви хочете видалити: ").capitalize()
        for element in self.contact_storage:
            if element['first_name'] == del_name:
                if element['last_name'] == del_surname:
                    self.contact_storage.remove(element)
                    return "Успішно видалено!"

contact_storage = []        
my_phonebook = Phonebook(contact_storage)   

while True:
    option = menu()
    if option == "q":
        print("OK,bye")
        break
    elif option == "add_func":
        print(my_phonebook.add_func())
    elif option == "del_func":  
        print(my_phonebook.del_func())
    elif option == "change_func":
        print(my_phonebook.change_func())     
    elif option == "city_or_email_search_func":
        print(my_phonebook.city_or_email_search_func())
    elif option == "num_of_cont_func":
        print(my_phonebook.num_of_cont_func())
    elif option == "all_contacts":
        print(my_phonebook.all_contacts())
    else:
        print(f"{option} isn't developed yet") 