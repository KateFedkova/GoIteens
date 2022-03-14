# NBU_Currency_proportion

import requests
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

#Token

print("Bot is up")

update = Updater(Token)
dispatcher = update.dispatcher

def start(update,context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='''Привіт! 
Я валютний бот

Якщо ви хочете подивитися назви усіх валют, натисніть /help

Щоб подивитися різницю курса валюти в рік, натисніть /currency''')

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

def buttons(update,context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('USD')], [KeyboardButton('EUR')], [KeyboardButton('PLN')], [KeyboardButton('BGN')],
               [KeyboardButton('ILS')], [KeyboardButton('TRY')], [KeyboardButton('GBP')], [KeyboardButton('CHF')],
               [KeyboardButton('DKK')], [KeyboardButton('EGP')]]
    context.bot.send_message(chat_id=chat.id,text= "Оберіть валюту",reply_markup=ReplyKeyboardMarkup(buttons))

def currency_proportion(update,context):
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD','EUR','PLN','BGN','ILS','TRY','GBP','CHF','DKK','EGP'):
        currency_rate = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&date=20220313&json").json()
        rate = currency_rate[0]['rate']
        currency_year_ago = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&date=20210313&json").json()
        rate_year_ago = currency_year_ago[0]['rate']
        proportion = (((rate - rate_year_ago) / rate_year_ago) * 100)
        message = f"""13.03.2021
{currency_code} вартість: {rate_year_ago} UAH

13.03.2022
{currency_code} вартість: {rate} UAH

Відношення:  {proportion} %"""
    context.bot.send_message(chat_id=chat.id, text=message)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('currency', buttons))
dispatcher.add_handler(MessageHandler(Filters.all, currency_proportion))


update.start_polling()
update.idle()
