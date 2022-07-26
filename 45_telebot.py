import telebot
from telebot import types

token='5422547033:AAF01FbxySXM-ni0HTlorfyUptOWvLM50PI'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    walk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('tc.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Вода",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('1a.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Еда",
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('20.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Прогуляйся",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('03.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Сладких снов",
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            img = open('17.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Шутка-минутка",
                reply_markup=keyboard)
            img.close()

if __name__=="__main__":
    bot.polling(none_stop=True)