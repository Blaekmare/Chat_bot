##библеотека для работы с телеграм ботами Telegram_bot
import telebot
from telebot import types
##импорт наиболее часто используемых и объемных функций
from funktion import *

##указание токена бота для доступа к редактированию его HTTP API
bot = telebot.TeleBot('5784094983:AAG231mJmCCIW9L3XGRr-QYOM4I9LToNMPY')

@bot.message_handler(commands=['play'])
def start(message):
    bot.send_message(message.chat.id, 'Фамилия, Имя')
    schet = 0
    bot.register_next_step_handler(message, next_input(message, schet))


def next_input(message, schet):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("А", "Б", "В")
    questions = DID_COMMAND_INDB("select question from question")
    question = list()
    for i in questions:
        question.append(convert_tuple(i))
    schet = schet + 1
    bot.send_message(message.chat.id, question[schet], reply_markup=markup)
    bot.register_next_step_handler(message, next_input(message, schet))




##стартовое сообщение при запуске бота
@bot.message_handler(commands=['start'])#Start
def start_bot(message):
    ## переменная, которая может хранить в себе кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ##Создание кнопок
    item1 = types.KeyboardButton("Соглашаюсь")
    item2 = types.KeyboardButton("Стоп")
    markup.add(item1, item2)

    ## Отправка сообщения пользователю и вывод отображения кнопок
    bot.send_message(message.chat.id,
                     "Добрый день использование нашего бота предусмотривает "
                        "просмотр вашего Id для записи вашей информации, "
                        "{0.first_name}".format(message.from_user), reply_markup=markup)


##Декоратор реагирующий на нажатия кнопок
@bot.callback_query_handler(func=lambda call: True)

##Функция для вывода результата при нажатии кнопки
@log_error
def callback(call):
    if call.message:
        if call.data == 'Search':
            bot.send_message(call.message.chat.id,
                             "Начните вводить: @Hospitalsynegy_bot")
        if call.data == 'Questions':
            bot.send_message(call.message.chat.id,
                             "Начните вводить: \play")




##Декоратор реагирующий на сообщения
@bot.message_handler(content_types=['text'])

##функция для регистрации пользователя
def bot_message(message):

    if message.text == 'Соглашаюсь':
        ## переменная хранящая в себе новость что надо удалить кнопки
        markup = telebot.types.ReplyKeyboardRemove()
        ##проверка на присутствия логина пользователя в бд
        logins = DID_COMMAND_INDB("select id from users where"
                                  " CAST(id as TEXT) like"+"'"+str(message.chat.id)+"'")
        if not logins:##если пользователь не зарегестрирован записываем его в бд
            bot.send_message(message.chat.id, "вы впервый раз зашли в "
                                              "этот чат бот произведена "
                                              "регистрация", reply_markup=markup)
            DID_COMMAND_not_return("INSERT INTO users(id, login) "
                                   "VALUES" + "(" + str(message.chat.id)+", "
                                   + "'" + str(message.from_user.first_name)+"'"+")")
        else:
            bot.send_message(message.chat.id, "Ваш логин"+str(message.chat.id),
                                                            reply_markup=markup)
        ##создание кнопок
        switch(message)
    ## условие если пользователь решил закончить работу бота
    if message.text == 'Стоп':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Хорошего дня", reply_markup=markup)
        bot.stop_bot()

##Функция для создания кнопок
def switch(message):
    # переменная что может хранить в себе кнопки
    # row_width определяет сколько кнопок может стоять в ряд
    markup = types.InlineKeyboardMarkup(row_width=2)
    search_button = types.InlineKeyboardButton(text='Поиск лекарств',
                                               callback_data='Search')
    question_button = types.InlineKeyboardButton(text='Опросник',
                                                 callback_data='Questions')
    markup.add(search_button, question_button)
    bot.send_message(message.chat.id, "Чем вы хотели бы заняться", reply_markup=markup)

##необходимо для постоянной работы бота

bot.infinity_polling()
