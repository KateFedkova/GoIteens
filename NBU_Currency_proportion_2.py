# NBU_Currency_proportion
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

Token = "5263522363:AAGpPQg0WqnV9TFvi6cToES57idg5KwZBa8"

print("Bot is up")

update = Updater(Token)
dispatcher = update.dispatcher

def start(update,context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='''Привіт! 
Я валютний бот

Якщо ви хочете подивитися назви усіх валют, натисніть /help

Щоб подивитися курс валюти, натисніть /find_info''')

def help(update,context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='''USD - Долар США
EUR - Євро
PLN - Злотий
BGN - Болгарський лев
ILS - Новий ізраїльський шекель
TRY - Турецька ліра
GBP - Фунт стерлінгів
CHF - Швейцарський франк
DKK - Данська крона
EGP - Єгипетський фунт''')



def find_info(update,context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Введіть код валюти та потрібну дату(рік,місяць,число)")


def val_info(update,context):
    chat = update.effective_chat
    code_and_date = update.message.text
    global info
    info = code_and_date.split(',')
    if info[0] in ('USD','EUR','PLN','BGN','ILS','TRY','GBP','CHF','DKK','EGP'):
        valid_date(update,context)
        find_date(update, context)
    else:
        context.bot.send_message(chat_id=chat.id, text="Не є кодом,спробуйте ще раз /find_info")


def find_date(update,context):
    chat = update.effective_chat
    if valid_date(update,context) == info[1]:
        date_api = valid_date(update,context)
        currency = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={info[0]}&date={date_api}&json").json()
        rate = currency[0]['rate']
        message = f"{valid_date(update,context)} - {info[0]} rate: {rate} UAH"
        context.bot.send_message(chat_id=chat.id, text=message)


def valid_date(update,context):
    chat = update.effective_chat
    dig_1 = info[1][0:4]
    dig_2 = info[1][4:6]
    dig_3 = info[1][6:8]
    try:
        if info[1] == datetime.date(int(dig_1),int(dig_2),int(dig_3)).strftime("%Y%m%d"):
            return info[1]
    except ValueError:
        context.bot.send_message(chat_id=chat.id, text='''Невірний формат,спробуйте ще раз"
find_info''')

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('find_info',find_info))
dispatcher.add_handler(MessageHandler(Filters.all,val_info))


update.start_polling()
update.idle()