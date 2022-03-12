#GoIteens_math
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '5286322882:AAFJgbOHA8lxCeb4YlZcn3-A50r61rJnKYk'
updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher
print('Bot started. Press Ctrl+C to exit')

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! Welcome to math Bot!")

def help(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="""You can: add +
                subtract - 
                multiply * 
                divide / 
                
                For example: 3+4 """)

def any_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    global elements
    elements = list(text)
    options = ['+','-','*','/']
    if elements[0].isdigit() and elements[2].isdigit():
        if elements[1] in options:
            if elements[1] == '+':
                add_func()
            elif elements[1] == '-':
                sub_func()
            elif elements[1] == '*':
                mul_func()
            elif elements[1] == '/':
                div_func()
            context.bot.send_message(chat_id=chat.id, text=str(result))
        else:
            text = "This option isn't developed yet"
            context.bot.send_message(chat_id=chat.id, text=text)
    else:
        text = 'Sorry, that doesn\'t look like number'
        context.bot.send_message(chat_id=chat.id, text=text)

def add_func():
    global result
    result = int(elements[0]) + int(elements[2])

def sub_func():
    global result
    result = int(elements[0]) - int(elements[2])

def mul_func():
    global result
    result = int(elements[0]) * int(elements[2])

def div_func():
    global result
    result = int(elements[0]) / int(elements[2])

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.all, any_message))


updater.start_polling()
updater.idle()