#Store

def hello(user_name):
    print(f"""
    Вітаю, {user_name}!
    Ласкаво просимо до нашого магазину канцелярії!
    """)


def user_name():
    user_name = input( "Enter your username: ")
    return user_name   
    
    
def menu():
    options = input("""
    Ви можете:
      Для продавців:
                     - зареєструвати товар                   : add_func
                     - видалити товар                        : del_func
      Для покупців:
                     - пошук товару за категоріями           : search_func
                     - подивитися загальну кількість товарів : num_of_items_func
                     - список всіх товарів                   : all_items
                     - купити товар                          : buy_func
                     - залишити відгук                       : review_func
             
     q - вийти
     Оберіть: """)
    return options 

def characteristic_desicion(characteristic):
    if characteristic == 'Папір офісний':
        items.copy_paper()
        return items.add_copy_paper()
    elif characteristic == 'Настільне приладдя':
        items.for_table()
        return items.add_for_table()
    elif characteristic == 'Письмове приладдя':
        items.writing_instruments()
        return items.add_writ_inst()
    elif characteristic == 'Скотч, стрейч-плівка':
        items.scotch()
        return items.add_scotch()
    return "Ви не можете додати товар такої категорії!"
    
def storage_filling(list_storage):
    goods = [
        {'категорія': "Папір офісний", 'торгова марка': "Crystal", ' колір': "білий", ' формат паперу': "A4", 'кількість листів': "100",'вартість': "150"},
        {'категорія': "Настільне приладдя", 'торгова марка': "Axent", 'розмір': "590*415", 'матеріал': "Пластик",'вартість': "200"},
        {'категорія': "Письмове приладдя", 'торгова марка': "1 вересня", 'діаметр стрижня': "0.7", 'колір чорнила': "чорний", 'товщина лінії': "0.2 мм",'вартість': "40"},
        {'категорія': "Скотч, стрейч-плівка", 'торгова марка': "Kores", 'розмір': "12*10", 'ширина': "12 мм", 'колір': "білий", 'довжина лінії': "2 м",'вартість': "50"},
    ]
    for element in goods:
        list_storage.append(element)
    
class Store:
    number_of_items = 4
    
    def __init__(self, list_storage):
        self.list_storage = list_storage  
        
    
    def characteristic(self):
        characteristic = input('''
        Ви можете додати:
        - Папір офісний
        - Настільне приладдя
        - Письмове приладдя
        - Скотч, стрейч-плівка
        
        Введіть категорію товару: ''')
        return characteristic
    
    
    def copy_paper(self):
        global brand,colour,format_of_paper,num_of_paper,price
        brand = input("Введіть торгову марку: ").capitalize()
        colour = input("Введіть колір: ").capitalize()
        format_of_paper = input("Введіть формат паперу: ").capitalize()
        num_of_paper = input("Введіть кількість листів: ").capitalize()
        price = input("Введіть вартість: ").capitalize()
        
    
    def add_copy_paper(self):
        result_dict = {'категорія': "Папір офісний", 'торгова марка': f"{brand}", ' колір': f"{colour}", ' формат паперу': f"{format_of_paper}", 'кількість листів': f"{num_of_paper}",'вартість': f"{price}"}
        if result_dict not in self.list_storage:
            self.list_storage.append(result_dict)
            Store.number_of_items +=1
            return "Вітаю! Товар уcпішно додано"
        else: 
            return "Такий товар вже є!" 
        
    def for_table(self):
        global brand_t,size,material,price_t
        brand_t = input("Введіть торгову марку: ").capitalize()
        size = input("Введіть розмір: ").capitalize()
        material = input("Введіть матеріал: ").capitalize()
        price_t = input("Введіть вартість: ").capitalize()
    
    def add_for_table(self):
        result_dict = {'категорія': "Настільне приладдя", 'торгова марка': f"{brand_t}", 'розмір': f"{size}", 'матеріал': f"{material}",'вартість': f"{price_t}"}
        if result_dict not in self.list_storage:
            self.list_storage.append(result_dict)
            Store.number_of_items +=1
            return "Вітаю! Товар уcпішно додано"
        else: 
            return "Такий товар вже є!" 
        
    def writing_instruments(self):
        global brand_w,diametr,colour_of,lin,price_w,line
        brand_w = input("Введіть торгову марку: ").capitalize()
        diametr = input("Введіть діаметр стрижня: ").capitalize()
        colour_of = input("Введіть колір чорнила: ").capitalize()
        line = input("Введіть товщину лінії: ").capitalize()
        price_w = input("Введіть вартість: ").capitalize()
        
    def add_writ_inst(self):
        result_dict = {'категорія': "Письмове приладдя", 'торгова марка': f"{brand_w}", 'діаметр стрижня': f"{diametr}", 'колір чорнила': f"{colour_of}", 'товщина лінії': f"{line}",'вартість': f"{price_w}"}
        if result_dict not in self.list_storage:
            self.list_storage.append(result_dict)
            Store.number_of_items +=1
            return "Вітаю! Товар уcпішно додано"
        else: 
            return "Такий товар вже є!"
        
    def scotch(self):
        global brand_s,size_s,wide,scale_s,colour_of_s,length,price_s
        brand_s = input("Введіть торгову марку: ").capitalize()
        size_s = input("Введіть розмір: ").capitalize()
        wide = input("Введіть ширину: ").capitalize()
        scale_s = input("Введіть шкалу: ").capitalize()
        colour_of_s = input("Введіть колір: ").capitalize()
        length = input("Введіть довжину лінії: ").capitalize()
        price_s = input("Введіть вартість: ").capitalize()
        
    def add_scotch(self):
        result_dict = {'категорія': "Скотч, стрейч-плівка", 'торгова марка': f"{brand_s}", 'розмір': f"{size_s}", 'ширина': f"{scale_s}", 'колір': f"{colour_of_s}", 'довжина лінії': f"{length}",'вартість': f"{price_s}"}
        if result_dict not in self.list_storage:
            self.list_storage.append(result_dict)
            Store.number_of_items +=1
            return "Вітаю! Товар уcпішно додано"
        else: 
            return "Такий товар вже є!"
        
         
    def num_of_items_func(self):
        return Store.number_of_items 
    
    def all_items(self):
        return self.list_storage    
   
    
    def del_func(self):
        del_categ = input("Введіть категорію товара,який хочете видалити: ").capitalize()
        del_brand = input("Введіть торгову марку товара,який хочете видалити: ").capitalize()
        del_price = input("Введіть вартість товара,який хочете видалити: ").capitalize()
        for element in self.list_storage:
            if element['категорія'] == del_categ:
                if element['торгова марка'] == del_brand:
                    if element['вартість'] == del_price:
                        self.list_storage.remove(element)
                        return "Успішно видалено!"
                    
                    
    def search_func(self):
        search_categ = input("Введіть категорію товара,який хочете знайти: ").capitalize()
        for element in self.list_storage:
            if element['категорія'] == search_categ:
                return element    
        
        
    def review_func(self):
        categ = input("Введіть категорію товара,який хочете прокоментувати: ").capitalize()
        brand = input("Введіть торгову марку товара,який хочете прокоментувати: ").capitalize()
        price = input("Введіть вартість товара,який хочете прокоментувати: ").capitalize()
        comment = input("Введіть свій коментарій: ")
        for element in self.list_storage:
            if element['категорія'] == categ:
                if element['торгова марка'] == brand:
                    if element['вартість'] == price:
                        element['коментарій'] = comment
                        return "Успішно додано!"
    
        

hello(user_name()) 

list_storage = []   
storage_filling(list_storage)

items = Store(list_storage)   

while True:
    option = menu()
    if option == "q":
        print("OK,до зустрічі!")
        break    
    elif option == "add_func":
        characteristic = items.characteristic()
        print(characteristic_desicion(characteristic))
    elif option == "search_func":
        print(items.search_func())
    elif option == "del_func":
        print(items.del_func())
    elif option == "num_of_items_func":
        print(items.num_of_items_func())
    elif option == "all_items":
        print(items.all_items())
    elif option == "review_func":
        print(items.review_func())
    else:
        print(f"{option} ще нема")