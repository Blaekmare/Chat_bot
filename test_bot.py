import telebot
from telebot import types

bot = telebot.TeleBot('5974476738:AAGp65D4Du1SoljXkclTmDpqsV6-4rsLfBY')


@bot.message_handler(commands=['play'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("15", "32", "50")
    bot.send_message(message.chat.id, 'Сколько будет 25+25?', reply_markup=markup)
    bot.register_next_step_handler(message, input_number, "50")


def input_number(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("А", "Б", "В")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'Верно', reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, 'Неверно', reply_markup=types.ReplyKeyboardRemove())

    bot.send_message(message.chat.id, 'Какая буква первая?', reply_markup=markup)
    bot.register_next_step_handler(message, input_number, "А")


def input_str(message, right_answer: str):
    if message.text == right_answer:
        bot.send_message(message.chat.id, 'Верно', reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, 'Неверно', reply_markup=types.ReplyKeyboardRemove())


bot.infinity_polling()

bot.infinity_polling()