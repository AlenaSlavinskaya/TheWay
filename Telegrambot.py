import telebot
from telebot import types

token = '5548726196:AAFNHGurx4i6qNWUEg6UbmphO81z8RGnqYY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton("Habr.com", url='https://freelance.habr.com/tasks')
    button2 = types.InlineKeyboardButton("FL.ru", url='https://www.fl.ru/projects/?kind=1#/')
    button3 = types.InlineKeyboardButton("Pchel.net", url='https://pchel.net/jobs/')
    button4 = types.InlineKeyboardButton("Freelancejob.ru", url='https://www.freelancejob.ru/projects/')
    button5 = types.InlineKeyboardButton("Kwork.ru", url='https://kwork.ru/projects')
    button6 = types.InlineKeyboardButton("Weblancer.net", url='https://www.weblancer.net/jobs/')

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    markup.add(button6)

    bot.send_message(message.chat.id, "Привет, {0.first_name}! Выбери биржу фриланса, на которую хочешь перейти)".format(message.from_user), reply_markup=markup)
bot.polling(none_stop=True)