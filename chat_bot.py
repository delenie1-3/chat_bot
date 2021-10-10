import telebot

bot = telebot.TeleBot('2075149976:AAFSxgVfUtAgZ5ouuAiawN0V8X2QvPrBKDU')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):#слушатель
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. напиши /help.')

bot.polling(non_stop=True, interval=0)#Запрос к телеграмму о сообщениях