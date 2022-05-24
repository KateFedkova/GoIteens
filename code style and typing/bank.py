from functools import wraps

from typing import Union, Optional, List, Tuple, Dict, Any, Callable


class Account_Info:
    """Menu"""

    @staticmethod
    def menu() -> str:
        place = input('''
Банкомат: 1
Аккаунт банку: 2
Оберіть: ''')
        return place


class BankAccount:
    """All functions that are available in the Bank Account"""

    __password: str = '77zth8jm'
    list_for_info: List[dict] = []

    def __init__(self, name: str, num_of_card: int,
                 pin: int, balance: int = 0) -> None:
        self.__name = name
        self.__num_of_card = num_of_card
        self.__pin = pin
        self.__balance = balance

    def __append_info(self) -> None:
        result_dict = {'name': f"{self.__name}",
                       'num_of_card': f"{self.__num_of_card}",
                       'pin': f"{self.__pin}", 'balance': f"{self.__balance}"}
        BankAccount.list_for_info.append(result_dict)

    def confirm_pin(self) -> Optional[bool]:
        num_of_trying = 0
        while num_of_trying < 4:
            pin_ = input('Pin: ')
            if int(self.__pin) == int(pin_):
                return True
            else:
                num_of_trying += 1
                print("Неправильний пін-код")
        print("Кількість спроб вичерпана")

    def info_from_card(self) -> bool:
        if self.confirm_pin():
            self._BankAccount__append_info()
        return False

    @staticmethod
    def account_menu() -> str:
        choice = input("""
Змінити пароль: 1
Змінити ім'я: 2
Поповнити рахунок: 3
Переказати кошти: 4
Оберіть: """)
        return choice

    def confirm_password(self) -> Optional[bool]:
        num_of_trying = 0
        while num_of_trying < 3:
            try_password = input('Password: ')
            if self.__password == try_password:
                return True
            else:
                num_of_trying += 1
                print("Неправильний пароль")
        print("Кількість спроб вичерпана")

    @classmethod
    def change_password(cls, pas) -> str:
        if len(pas) < 8:
            cls.__password = pas
            return "Успішно"
        else:
            return "Забагато цифр"

    def change_name(self) -> None:
        new_name = input("Введіть нове ім'я: ")
        for element in BankAccount.list_for_info:
            element['name'] = new_name

    def paying(self) -> str:
        card_transfer = input('Номер картки на яку хочете перказати: ')
        if len(card_transfer) == 16:
            money = input('Кількість грошей,яку ви хочете переказати: ')
            if int(money) < self.__balance:
                print(f"""{money} грн
from card: {self.__num_of_card} to card: {card_transfer}""")
                for element in BankAccount.list_for_info:
                    element['balance'] = int(element['balance']) - int(money)
                    return "Успішно"
        return "Така картка не існує"

    def replenish(self) -> str:
        am_of_m = input("Кількість грошей,які ви хочете покласти на картку: ")
        for element in BankAccount.list_for_info:
            element['balance'] = int(element['balance']) + int(am_of_m)
            return "Успішно"


class Cash_Machine:
    """All functions that are available in the Cash Machine"""

    name_ob_bank: str = 'Mono'
    __collection_code = 774230

    def __init__(self, quantity_of_money: Union[int, float]) -> None:
        self.__quantity_of_money = quantity_of_money

    @staticmethod
    def bank_menu() -> str:
        option = input("""
Поповнити баланс: 1
Зняти гроші: 2
Bилучення грошей з банкомату інкасаторами: 3
Оберіть: """)
        return option

    def conf_pin_bef_getting(self) -> Optional[bool]:
        num_of_trying = 0
        while num_of_trying < 4:
            pin_ = input('Pin: ')
            for element in BankAccount.list_for_info:
                if int(element['pin']) == int(pin_):
                    return True
                else:
                    num_of_trying += 1
                    print("Неправильний пін-код")
        print("Кількість спроб вичерпана")
        exit()

    def get_info(self) -> Tuple[Dict[Any, Any], Any, Any, Any, Any]:
        if self.conf_pin_bef_getting():
            for element in BankAccount.list_for_info:
                name = element['name']
                num_of_card = element['num_of_card']
                pin = element['pin']
                balance = element['balance']
                return element, name, num_of_card, pin, balance
        exit()

    @staticmethod
    def time_logger(func: Callable[..., Any]) -> Callable[..., Any]:
        import logging
        import datetime
        logging.basicConfig(filename=f'{func.__name__}.log',
                            level=logging.INFO)

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logging.info(f'{func.__name__} made in {datetime.datetime.now()}')
            return result

        return wrapper

    @staticmethod
    def info_logger(new_func: Callable[..., Any]) -> Callable[..., Any]:
        import logging

        logging.basicConfig(filename=f'{new_func.__name__}.log',
                            level=logging.INFO)

        @wraps(new_func)
        def wrapper(*args, **kwargs):
            logging.info(f'{new_func(*args, **kwargs)}')

        return wrapper

    def confirm_PIN(self) -> Optional[bool]:
        num_of_trying = 0
        while num_of_trying < 4:
            pin_ = input('Pin: ')
            if int(pin) == int(pin_):
                return True
            else:
                num_of_trying += 1
                print("Неправильний пін-код")
        print("Кількість спроб вичерпана")

    @time_logger
    def replenish_balance(self, balance) -> Union[int, None]:
        if self.confirm_PIN():
            am_of_m = input("Кількість грошей,які "
                            "ви хочете покласти на картку: ")
            new_balance = int(balance)
            new_balance += int(am_of_m)
            print("Успішно")
            return new_balance
        return False

    @info_logger
    def return_info(self, new_balance) -> List[Dict[Any, Any]]:
        element['balance'] = new_balance
        return BankAccount.list_for_info

    @time_logger
    def get_cash(self) -> Tuple[str, int]:
        if self.confirm_PIN():
            amount = input('Кількість грошей,які ви хочете зняти: ')
            cash = int(element['balance'])
            if int(amount) < self.__quantity_of_money:
                if int(amount) < cash:
                    cash -= int(amount)
                    element['balance'] = cash
                    print("Гроші успішно знято")
                    return amount, cash
                print("Недостатньо грошей")
                exit()
            print("Недостатньо грошей")
            exit()
        print("Недостатньо грошей")
        exit()

    @info_logger
    def cheque(self, amount: Union[int, float], cash: float) -> str:
        import datetime
        result = f"""
{datetime.datetime.today()}
Знято: {amount}
Залишок: {cash}
"""
        return result

    @time_logger
    def collection(self) -> str:
        code = input('Введіть код для вилучення грошей '
                     'з банкомату інкасаторами: ')
        if int(code) == Cash_Machine.__collection_code:
            self.__quantity_of_money = 0
            return "Гроші успішно вилучено"


bank = Cash_Machine(54000)

account_1 = BankAccount('Olena', 2745958658873965, 8875, 1000)


while True:
    place = Account_Info.menu()
    account_1.info_from_card()
    if place == '1':
        option = bank.bank_menu()
        element, name, num_of_card, pin, balance = bank.get_info()
        if option == '1':
            new_balance = bank.replenish_balance(balance)
            bank.return_info(new_balance)
        elif option == '2':
            amount, cash = bank.get_cash()
            bank.cheque(amount, cash)
        elif option == '3':
            print(bank.collection())
        else:
            print('Помилка!')
    elif place == '2':
        choice = account_1.account_menu()
        if account_1.confirm_password():
            if choice == '1':
                new = input('Новий пароль: ')
                print(account_1.change_password(new))
            elif choice == '2':
                account_1.change_name()
            elif choice == '3':
                print(account_1.replenish())
            elif choice == '4':
                print(account_1.paying())
    else:
        print('Помилка!')
