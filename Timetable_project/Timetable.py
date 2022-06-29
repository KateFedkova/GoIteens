import os
import datetime
import json
from telegram.ext import Updater, CommandHandler, \
    MessageHandler, Filters, ConversationHandler

from telegram import KeyboardButton, ReplyKeyboardMarkup
from contextlib import contextmanager
from settings import TOKEN


print("Bot is up")

update = Updater(TOKEN)
dispatcher = update.dispatcher

DAY, MONTH, TIME, END_OF_MEETING, NAME, DAY_DEL, MONTH_DEL, NAME_DEL = range(8)


def start(update, context):
    """Send message if a user clicks a start command"""
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='''Привіт!

Це ITimetable_bot

Я допоможу організувати твій час!

Натисни /help, щоб дізнатися більше''')


def help(update, context):
    """Send message if a user clicks a help button"""
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='''В цьому боті ти можеш:

     додавати зустрічі,

     видаляти їх

Ти не забудеш про зустріч, бо
можеш подивитися, які зустрічі будуть в цей день!!!

Почни планувати свій день: /buttons
Якщо хочете відмінити функцію планування, введіть /close''')


def buttons(update, context):
    """Show all available buttons"""
    chat = update.effective_chat
    buttons = [[KeyboardButton('Додати нову зустріч')],
               [KeyboardButton('Видалити зустріч')],
               [KeyboardButton('Подивитися сьогоднішні зустрічі')]]
    context.bot.send_message(chat_id=chat.id,
                             text="Оберіть",
                             reply_markup=ReplyKeyboardMarkup(buttons))


@contextmanager
def create_directory(name_of_file, info_in_file):
    """Create directory or write information into a file"""
    cwd = os.getcwd()
    os.chdir("Timetable_Information")
    f = open(name_of_file + '.txt', mode="a")
    f.write(str(info_in_file) + '\n')
    f.close()
    yield
    os.chdir(cwd)


def new_meeting_day(update, context):
    """Send message to opt a day"""
    update.message.reply_text(text="Оберіть місяць зустрічі у форматі: 01 ...")
    return MONTH


def get_month(update, context):
    """Check if this month exists and ask for the time"""
    global month
    month = update.message.text
    d = datetime.date.today()
    if d.month <= int(month[1]) and int(month) < 13 and len(month) == 2:
        global list_f_info
        list_f_info = list_of_info({}, "month", month)
        update.message.reply_text(text="Оберіть день зустрічі")
        return DAY
    else:
        conv_end(update, context)


def get_day(update, context):
    """Check if this day exists and ask for a month"""
    global day
    day = update.message.text
    d = datetime.date.today()
    if d.day > int(day) and int(month[1]) == d.month:
        conv_end(update, context)
    elif check_month(month, day):
        global list_f_info_1
        list_f_info_1 = list_of_info(list_f_info, "day", day)
        update.message.reply_text(text="Введіть годину,"
                                       " о котрій починається"
                                       " зустріч у форматі 11:00")
        return TIME
    else:
        conv_end(update, context)


def check_month(month, day):
    thirty_month = ["04", "06", "09", "11"]
    short_month = "02"
    thirty_one_month = ["01", "03", "05", "07", "08", "10", "12"]
    d = datetime.date.today()
    if month in thirty_month and int(day) and 0 < int(day) < 31:
        return True
    elif month in thirty_one_month and int(day) and 0 < int(day) < 32:
        return True
    elif month == short_month:
        if d.year % 4 == 0 and d.year % 100 != 0 or d.year % 400 == 0:
            if int(day) and 0 < int(day) < 30:
                return True
        else:
            if int(day) and 0 < int(day) < 29:
                return True
    return False


def get_time(update, context):
    """Check if time exists and ask for a title of meeting"""
    global time
    time = update.message.text
    if 0 <= int(time.split(':')[0]) < 24 \
            and 0 <= int(time.split(':')[1]) <= 60:
        global list_f_info_2
        list_f_info_2 = list_of_info(list_f_info_1, "time", time)
        update.message.reply_text(text="Введіть годину,"
                                       " о котрій закiнчується зустріч")
        return END_OF_MEETING
    else:
        conv_end(update, context)


def clash_duration(update, day, month, time, end):
    time_split, end_split = split_time(time, end)
    cwd = os.getcwd()
    os.chdir("Timetable_Information")
    f = open(f"{update.message.chat.first_name}_"
             f"{update.message.chat.id}" + '.txt', mode="r")
    for line in f.readlines():
        if day in line and month in line:
            first = line.replace("\'", "\"")
            c = json.loads(first)
            end_time_l = c['end']
            time_l = c['time']
            os.chdir(cwd)
            value = check_time_end(update, line, cwd, end_time_l,
                                   time_l, time, end)
            if value:
                continue
            else:
                return value
    os.chdir(cwd)
    return True


def try_again_repeat(update):
    update.message.reply_text(text="Вже є зустріч в цей час."
                                   "Почніть ще раз спочатку!")
    return False


def check_time_end(update, line, cwd, end_time_l,
                   time_l, time, end):
    if time in line:
        os.chdir(cwd)
        try_again_repeat(update)
    elif end in line:
        os.chdir(cwd)
        try_again_repeat(update)
    elif time_l < time_split < end_split < end_time_l:
        os.chdir(cwd)
        try_again_repeat(update)
    elif time_l < time_split < end_time_l < end_split:
        os.chdir(cwd)
        try_again_repeat(update)
    elif time_split < time_l < end_split < end_time_l:
        os.chdir(cwd)
        try_again_repeat(update)
    elif time_split < time_l < end_time_l < end_split:
        os.chdir(cwd)
        try_again_repeat(update)
    else:
        return True


def get_end_meeting(update, context):
    """Check if time exists and ask for a time when a meeting will end"""
    global end
    end = update.message.text
    if 0 <= int(end.split(':')[0]) <= 24 and 0 <= int(end.split(':')[1]) <= 60:
        end_s = f"{end.split(':')[0]}{end.split(':')[1]}"
        time_s = f"{time.split(':')[0]}{time.split(':')[1]}"
        if int(end_s) > int(time_s): 
            global list_f_info_3
            list_f_info_3 = list_of_info(list_f_info_2, "end", end)
            if not empty_file(update):
                if clash_duration(update, day, month, time, end):
                    update.message.reply_text(text="Введіть назву зустрічі")
                    return NAME
                else:
                    return ConversationHandler.END
            else:
                update.message.reply_text(text="Введіть назву зустрічі")
                return NAME
        else:
            conv_end(update, context)


def empty_file(update):
    cwd = os.getcwd()
    if not os.path.isdir("Timetable_Information"):
        os.mkdir("Timetable_Information")
    os.chdir("Timetable_Information")
    try:
        f = open(f"{update.message.chat.first_name}_"
                 f"{update.message.chat.id}.txt", mode="r")
    except FileNotFoundError:
        f = open(f"{update.message.chat.first_name}_"
                 f"{update.message.chat.id}.txt", mode="w")
    finally:
        empty = os.stat(f"{update.message.chat.first_name}_"
                        f"{update.message.chat.id}.txt").st_size == 0
        os.chdir(cwd)
        return empty


def get_title(update, context):
    """Write a dict into a file and return ConversationHandler.END """
    name = update.message.text
    name_of_file = f"{update.message.chat.first_name}_{update.message.chat.id}"
    list_f_info_4 = list_of_info(list_f_info_3, "title", name)
    with create_directory(name_of_file, list_f_info_4):
        update.message.reply_text(text="Успішно записано!")
    return ConversationHandler.END


def close(update, context):
    """Return ConversationHandler.END"""
    update.message.reply_text(text='До зустрічі!')
    return ConversationHandler.END


def list_of_info(list_f_info, key_word, arg_word):
    """Create a dict"""
    list_f_info[key_word] = arg_word
    return list_f_info


def del_meeting_day(update, context):
    """Send message to opt a day"""
    update.message.reply_text(text="Оберіть місяць зустрічі у форматі: 01 ...")
    return MONTH_DEL


def del_month(update, context):
    """Check if this day exists and ask for a title"""
    global month_del
    month_del = update.message.text
    d = datetime.date.today()
    if d.month <= int(month_del[1]) and \
            int(month_del) < 13 and len(month_del) == 2:
        global num_line
        num_line = check_if_true(update, month_del)
        update.message.reply_text(text="Оберіть день зустрічі")
        return DAY_DEL
    else:
        conv_end(update, context)


def del_day(update, context):
    """Check if this day exists and ask for a month"""
    day_del = update.message.text
    if check_month(month_del, day_del):
        global num_line_2
        num_line_2 = check_if_true(update, day_del)
        if num_line == num_line_2:
            update.message.reply_text(text="Оберіть назву зустрічі")
            return NAME_DEL
        else:
            conv_end(update, context)
    else:
        conv_end(update, context)


def del_title(update, context):
    """Delete a dict from a file and return ConversationHandler.END """
    name = update.message.text
    num_line_3 = check_if_true(update, name)
    if num_line_3 == num_line_2:
        del_from_file(update, num_line_3)
        update.message.reply_text(text="Успішно видалено!")
        return ConversationHandler.END


def del_from_file(update, num_line):
    """Delete from file"""
    cwd = os.getcwd()
    os.chdir("Timetable_Information")
    with open(f"{update.message.chat.first_name}_"
              f"{update.message.chat.id}" + ".txt", 'r') as f:
        lines = f.readlines()
    with open(f"{update.message.chat.first_name}_"
              f"{update.message.chat.id}" + ".txt", 'w') as f:
        for number, line in enumerate(lines):
            if number != num_line:
                f.write(line)
    os.chdir(cwd)


def all_meetings(update, context):
    """Separate all lines"""
    all_lines = read_file(update)
    for line in all_lines:
        first = line.strip()
        first = first.replace("\'", "\"")
        c = json.loads(first)
        check(update, c)


def read_file(update):
    """Read all lines"""
    cwd = os.getcwd()
    os.chdir("Timetable_Information")
    f = open(f"{update.message.chat.first_name}_"
             f"{update.message.chat.id}" + '.txt', mode="r")
    all_lines = f.readlines()
    os.chdir(cwd)
    return all_lines


def check(update, first):
    """Check if date is equal to date in a file"""
    d = datetime.date.today()
    d_now = f"{d.day}.0{d.month}"
    d_l = f"{first['day']}.{first['month']}"
    if d_now == d_l:
        reply(update, first)


def reply(update, first):
    message = f"""
Назва зустрічі: {first['title']}
Початок зустрічі: {first['time']}
Кінець зустрічі: {first['end']}
"""
    update.message.reply_text(text=message)


def check_if_true(update, arg_word):
    """Look for a word in each line"""
    cwd = os.getcwd()
    os.chdir("Timetable_Information")
    f = open(f"{update.message.chat.first_name}_"
             f"{update.message.chat.id}" + '.txt', mode="r")
    for num_line, line in enumerate(f):
        if arg_word in line:
            os.chdir(cwd)
            return num_line
    os.chdir(cwd)


def conv_end(update, context):
    """Send a message that the information does not exist"""
    update.message.reply_text(text="Не відповідає дійсності. "
                                   "Почніть ще раз спочатку! /close")


conv_hand_add = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex(r'Додати'), new_meeting_day)],
    states={
        MONTH: [MessageHandler(Filters.text & (~ Filters.command), get_month)],
        DAY: [MessageHandler(Filters.text & (~ Filters.command), get_day)],
        TIME: [MessageHandler(Filters.text & (~ Filters.command), get_time)],
        END_OF_MEETING: [MessageHandler
                         (Filters.text & (~ Filters.
                                          command), get_end_meeting)],
        NAME: [MessageHandler(Filters.text & (~ Filters.command), get_title)],
    },
    fallbacks=[CommandHandler('close', close)],
)


conv_hand_del = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex
                                 (r'Видалити зустріч'), del_meeting_day)],
    states={
        MONTH_DEL: [MessageHandler(Filters.text &
                                   (~ Filters.command), del_month)],
        DAY_DEL: [MessageHandler(Filters.text & (~ Filters.command), del_day)],
        NAME_DEL: [MessageHandler(Filters.text &
                                  (~ Filters.command), del_title)],
    },
    fallbacks=[CommandHandler('close', close)],
)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('buttons', buttons))
dispatcher.add_handler(MessageHandler(
    Filters.regex(r'Подивитися сьогоднішні зустрічі'), all_meetings))
dispatcher.add_handler(conv_hand_add)
dispatcher.add_handler(conv_hand_del)


update.start_polling()
update.idle()


