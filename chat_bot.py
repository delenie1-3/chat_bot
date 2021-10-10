import telebot
from telebot import types

bot = telebot.TeleBot('2075149976:AAFSxgVfUtAgZ5ouuAiawN0V8X2QvPrBKDU')
'''
@bot.message_handler(content_types=['text'])
def get_text_messages(message):#слушатель
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. напиши /help.')
'''

name = ''
surname = ''
age = 0

@bot.message_handler(content_types=['text'])
def start(message):#начало регистрации, имя
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):#фамилия
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):#возраст
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):#проверка возраста
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Укажи возраст цифрами')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):#оброботка ввода с клавиатуры
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Запомнил')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Повтори запрос /reg')


bot.polling(non_stop=True, interval=0)#Запрос к телеграмму о сообщениях