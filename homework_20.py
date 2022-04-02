#Store

def hello(user_name):
    print(f"""
    Вітаю, {user_name}!
    Ласкаво просимо до нашого магазину канцелярії!
    """)


def user_name():
    user_name = input( "Enter your username: ")
    return user_name   

    
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
            
    def menu(self):
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
    
    def characteristic(self):
        characteristic = input('''
        Ви можете додати:
        - Папір офісний
        - Настільне приладдя
        - Письмове приладдя
        - Скотч, стрейч-плівка
        
        Введіть категорію товару: ''')
        return characteristic
   
    def characteristic_desicion(self, characteristic):
        if characteristic == 'Папір офісний':
            brand,colour,format_of_paper,num_of_paper,price = self.copy_paper()
            result_dict = self.add_copy_paper(brand,colour,format_of_paper,num_of_paper,price)
            return self.add_to_list(result_dict)
        elif characteristic == 'Настільне приладдя':
            brand_t,size,material,price_t = self.for_table()
            result_dict = self.add_for_table(brand_t,size,material,price_t)
            return self.add_to_list(result_dict)
        elif characteristic == 'Письмове приладдя':
            brand_w,diametr,colour_of,price_w,line = self.writing_instruments()
            result_dict = self.add_writ_inst(brand_w,diametr,colour_of,price_w,line)
            return self.add_to_list(result_dict)
        elif characteristic == 'Скотч, стрейч-плівка':
            brand_s,size_s,wide,scale_s,colour_of_s,length,price_s = self.scotch()
            result_dict = self.add_scotch(brand_s,size_s,wide,scale_s,colour_of_s,length,price_s)
            return self.add_to_list(result_dict)
        return "Ви не можете додати товар такої категорії!"    
    
    def copy_paper(self):
        brand = input("Введіть торгову марку: ").capitalize()
        colour = input("Введіть колір: ").capitalize()
        format_of_paper = input("Введіть формат паперу: ").capitalize()
        num_of_paper = input("Введіть кількість листів: ").capitalize()
        price = input("Введіть вартість: ").capitalize()
        return brand,colour,format_of_paper,num_of_paper,price
        
    def add_copy_paper(self,brand,colour,format_of_paper,num_of_paper,price):
        result_dict = {'категорія': "Папір офісний", 'торгова марка': f"{brand}", ' колір': f"{colour}", ' формат паперу': f"{format_of_paper}", 'кількість листів': f"{num_of_paper}",'вартість': f"{price}"}
        return result_dict
        
    def for_table(self):
        brand_t = input("Введіть торгову марку: ").capitalize()
        size = input("Введіть розмір: ").capitalize()
        material = input("Введіть матеріал: ").capitalize()
        price_t = input("Введіть вартість: ").capitalize()
        return brand_t,size,material,price_t
    
    def add_for_table(self,brand_t,size,material,price_t):
        result_dict = {'категорія': "Настільне приладдя", 'торгова марка': f"{brand_t}", 'розмір': f"{size}", 'матеріал': f"{material}",'вартість': f"{price_t}"}
        return result_dict
        
    def writing_instruments(self):
        brand_w = input("Введіть торгову марку: ").capitalize()
        diametr = input("Введіть діаметр стрижня: ").capitalize()
        colour_of = input("Введіть колір чорнила: ").capitalize()
        line = input("Введіть товщину лінії: ").capitalize()
        price_w = input("Введіть вартість: ").capitalize()
        return brand_w,diametr,colour_of,price_w,line
        
    def add_writ_inst(self,brand_w,diametr,colour_of,price_w,line):
        result_dict = {'категорія': "Письмове приладдя", 'торгова марка': f"{brand_w}", 'діаметр стрижня': f"{diametr}", 'колір чорнила': f"{colour_of}", 'товщина лінії': f"{line}",'вартість': f"{price_w}"}
        return result_dict
        
    def scotch(self):
        brand_s = input("Введіть торгову марку: ").capitalize()
        size_s = input("Введіть розмір: ").capitalize()
        wide = input("Введіть ширину: ").capitalize()
        scale_s = input("Введіть шкалу: ").capitalize()
        colour_of_s = input("Введіть колір: ").capitalize()
        length = input("Введіть довжину лінії: ").capitalize()
        price_s = input("Введіть вартість: ").capitalize()
        return brand_s,size_s,wide,scale_s,colour_of_s,length,price_s
        
    def add_scotch(self,brand_s,size_s,wide,scale_s,colour_of_s,length,price_s):
        result_dict = {'категорія': "Скотч, стрейч-плівка", 'торгова марка': f"{brand_s}", 'розмір': f"{size_s}", 'ширина': f"{scale_s}", 'колір': f"{colour_of_s}", 'довжина лінії': f"{length}",'вартість': f"{price_s}"}
        return result_dict
         
    def num_of_items_func(self):
        return Store.number_of_items 
    
    def all_items(self):
        for element in self.list_storage:
            print(element)
    
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
                    
    def add_to_list(self, result_dict):
        if result_dict not in self.list_storage:
            self.list_storage.append(result_dict)
            Store.number_of_items +=1
            return "Вітаю! Товар уcпішно додано"
        else: 
            return "Такий товар вже є!" 
        
        
hello(user_name()) 

list_storage = []   
storage_filling(list_storage)

items = Store(list_storage)   

while True:
    option = items.menu()
    if option == "q":
        print("OK,до зустрічі!")
        break    
    elif option == "add_func":
        characteristic = items.characteristic()
        print(items.characteristic_desicion(characteristic))
    elif option == "search_func":
        print(items.search_func())
    elif option == "del_func":
        print(items.del_func())
    elif option == "num_of_items_func":
        print(items.num_of_items_func())
    elif option == "all_items":
        items.all_items()
    elif option == "review_func":
        print(items.review_func())
    else:
        print(f"{option} ще нема")