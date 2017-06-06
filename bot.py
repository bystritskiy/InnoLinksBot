# -*- coding: utf-8 -*-
import telebot
import config


token = config.token
bot = telebot.TeleBot(token)

# bot.send_message(57344339, "test")
# upd = bot.get_updates()
# print(upd)

# last_upd = upd [-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(bot.get_me())


def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))
    print(answer)
user_markup = telebot.types.ReplyKeyboardMarkup(True, True)

@bot.message_handler(commands=['start'])
def handle_start(message):

    user_markup.row('Главное', 'Транспорт')
    user_markup.row('Медицина', 'Еда')
    user_markup.row('Спорт', 'Развлечения')
    user_markup.row('Инфраструктура', 'Услуги')
    user_markup.row('Кружки, секции и чаты')
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=user_markup)

#@bot.message_handler(commands=['stop'])
#def handle_start(message):
#    hide_markup = telebot.types.ReplyKeyboardRemove()
#    bot.send_message(message.from_user.id, '', reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def handle_tex(message):
    bot.send_message(message.chat.id, "Я храню всю важную информацию о моем любимом городе Иннополисе")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Я не настолько крут, чтобы обрабатывать все запросы"
    if message.text == "Еда":
        user_markup2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup2.row('Общепит', 'Кафе и бары')
        user_markup2.row('Продуктовые магазины', 'Back')
        answer = "Вы находитесь в категории, посвященной питанию в нашем городе"

        bot.send_message(message.from_user.id, answer , reply_markup=user_markup2)
        log(message, answer)


    elif message.text == "Инфраструктура":
        user_markup3 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup3.row('Банки', 'Магазины')
        user_markup3.row('Почта', 'Салоны красоты')
        user_markup3.row('Жильё', 'Безопасность')
        user_markup3.row('Вакансии', 'Мэрия')
        user_markup3.row('Автомобилистам', "Back")
        answer = "Вы находитесь в категории, посвященной инфраструктуре нашего современного города"

        bot.send_message(message.from_user.id, answer, reply_markup=user_markup3)
        log(message, answer)

    elif message.text == "Back":
        answer = "Обратно к основным категориям"

        bot.send_message(message.from_user.id, answer , reply_markup=user_markup)
        log(message, answer)

    elif message.text == 'а':
        answer = "Б"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif message.text == 'б':
        answer = "B"
        bot.send_message(message.chat.id, answer)
        log(message, answer)


    elif message.text == 'в':
        answer = "Ладно, ты победил. Игра окончена."
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


#infinite loop
bot.polling(none_stop=True, interval=0)
