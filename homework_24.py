import datetime

class Cash_Machine:
    
    @staticmethod
    def menu():
        option = input("""
Подивитися рахунок: 1
Зняти гроші: 2 

Оберіть: """)
        return option
    
    def __init__(self, pin,card_name, balance=0):
        self.__pin = pin
        self.__card_name = card_name
        self.__balance = balance     
        if self.confirm_PIN():
            print('Вітаємо! Оберіть опцію')
            option = Cash_Machine.menu()
            self.option_desicion(option)
        
    def confirm_PIN(self):
        num_of_trying = 0     
        while num_of_trying < 4:
            pin = input('Pin: ')
            if self.__pin == int(pin):
                return True
            else:
                num_of_trying += 1
                print("Неправильний пін-код")
        print("Кількість спроб вичерпана")
        
    def option_desicion(self, option):          
        if option == '1':
            print(self.__show_balance())
        elif option == '2':
            amount = self.__get_cash()
        return "Ви не можете викорисати таку функцію!"    
    
    def __show_balance(self):
        return f"Залишок на вашому рахунку: {self.__balance} грн"
    
    def __get_cash(self):
        amount = input('Кількість грошей,які ви хочете зняти: ')
        if int(amount) < self.__balance:
            self.__balance -= int(amount)
            print("Гроші успішно знято")
            print(self.__cheque(amount))
            return amount
        return "Недостатньо грошей"
        
    def __cheque(self, amount):
        return f"""
{datetime.datetime.today()}
Знято: {amount}
Залишок: {self.__balance}
"""
        
    
class BankAccount:
    __password = '77zth8jm'
    
    def __init__(self, name, num_of_card, pin, balance=0):
        self.__name = name
        self.__num_of_card = num_of_card
        self.__pin = pin
        self.__balance = balance  
        if self.confirm_PIN():
            self.__paying()
        
    def confirm_PIN(self):
        num_of_trying = 0     
        while num_of_trying < 3:
            password_ = input('Password: ')
            if self.__password == password_:
                return True
            else:
                num_of_trying += 1
                print("Неправильний пароль")
        print("Кількість спроб вичерпана")  
        
    @classmethod
    def __change_password(cls, pas):
        if len(pas) < 8:
            cls.__password = pas
        else:
            return f"Забагато цифр"

    def __paying(self):
        card_transfer = input('Номер картки на яку хочете перказати: ')
        money = input('Кількість грошей,яку ви хочете переказати: ')
        if len(card_transfer) == 16:
            print(f"""{money} грн 
from card:{self.__num_of_card} to card:{card_transfer}""")
            self.__balance -= int(money)
        else:
            print("Така картка не існує")

bank_card = Cash_Machine(8875, 'junior', 1000)

account_1 = BankAccount('Olena', 2745958658873965, 8875, 1000)

account_1._BankAccount__change_password('1234567')
