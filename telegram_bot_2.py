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
    if '+' in text:
        elements = text.split('+')
        if elements[0].replace('.', '', 1).isdigit() and elements[1].replace('.', '', 1).isdigit():
            add_func(elements)
            context.bot.send_message(chat_id=chat.id, text=add_func(elements))
        else:
            text = 'Sorry, that doesn\'t look like number'
            context.bot.send_message(chat_id=chat.id, text=text)
    elif "-" in text:
        elements = text.split('-')
        if elements[0].replace('.', '', 1).isdigit() and elements[1].replace('.', '', 1).isdigit():
            sub_func(elements)
            context.bot.send_message(chat_id=chat.id, text=sub_func(elements))
        else:
            text = 'Sorry, that doesn\'t look like number'
            context.bot.send_message(chat_id=chat.id, text=text)
    elif '*' in text:
        elements = text.split('*')
        if elements[0].replace('.', '', 1).isdigit() and elements[1].replace('.', '', 1).isdigit():
            mul_func(elements)
            context.bot.send_message(chat_id=chat.id, text=mul_func(elements))
        else:
            text = 'Sorry, that doesn\'t look like number'
            context.bot.send_message(chat_id=chat.id, text=text)
    elif "/" in text:
        elements = text.split('/')
        if elements[0].replace('.','',1).isdigit() and elements[1].replace('.','',1).isdigit():
            div_func(elements)
            context.bot.send_message(chat_id=chat.id, text=div_func(elements))
        else:
            text = 'Sorry, that doesn\'t look like number'
            context.bot.send_message(chat_id=chat.id, text=text)
    else:
        text = "This option isn't developed yet"
        context.bot.send_message(chat_id=chat.id, text=text)

def add_func(elements):
    result = float(elements[0]) + float(elements[1])
    return '%.2f' % (result)

def sub_func(elements):
    result = float(elements[0]) - float(elements[1])
    return  '%.2f' % (result)

def mul_func(elements):
    result = float(elements[0]) * float(elements[1])
    return '%.2f' % (result)

def div_func(elements):
    if elements[1] == '0':
        result = "Dividing by zero is not allowed"
        return result
    result = float(elements[0]) / float(elements[1])
    return '%.2f' % (result)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.all, any_message))


updater.start_polling()
updater.idle()