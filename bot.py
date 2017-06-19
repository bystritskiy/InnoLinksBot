## -*- coding: utf-8 -*-
import telebot

TOKEN = '396424405:AAHQZxMEkBdsAkFk2BxSgJBKEQaaoWtjuhc'
bot = telebot.TeleBot(TOKEN)

def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id={2})".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer + '\n')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup_main_menu = telebot.types.ReplyKeyboardMarkup()
    user_markup_main_menu.row('Главное' + u'\U00002757', 'Транспорт' + u'\U0001f68c')
    user_markup_main_menu.row('Медицина' + u'\U0001f691', 'Еда' + u'\U0001F37D')
    user_markup_main_menu.row('Спорт' + u'\U0001f6b4', 'Развлечения' + u'\U0001f3a5')
    user_markup_main_menu.row('Инфраструктура' + u'\U0001f3d9', 'Услуги' + u'\U0001f465')
    user_markup_main_menu.row('Кружки, секции, чаты' + u'\U0001f3a8')
    log(message, message.text)
    bot.send_message(message.chat.id, 'Выберите одну из категорий', reply_markup=user_markup_main_menu)

@bot.message_handler(commands=['help'])
def command_handler(message):
    bot.send_message(message.chat.id, "Я собираюсь помочь тебе")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Main menu categories
    if message.text == 'Главное' + u'\U00002757':
        answer = "Вы находитесь в категории, в которой находятся самые необходимые ссылки и информация в нашем городе. \nВыберите следующую категорию"
        user_markup_main = telebot.types.ReplyKeyboardMarkup()
        user_markup_main.row('Back' + u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_main)

    elif message.text == 'Транспорт' + u'\U0001f68c':
        answer = "Вы находитесь в категории, посвященной транспорту в нашем городе."
        user_markup_transport = telebot.types.ReplyKeyboardMarkup()
        user_markup_transport.row('Back' + u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_transport)

    elif message.text == 'Медицина' + u'\U0001f691':
        answer = "Вы находитесь в категории, посвященной медицине в нашем городе."
        user_markup_medicine = telebot.types.ReplyKeyboardMarkup()
        user_markup_medicine.row('Back' + u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_medicine)

    elif message.text == 'Еда' + u'\U0001F37D':
        user_markup_food = telebot.types.ReplyKeyboardMarkup()
        user_markup_food.row('Столовые', 'Кафе и бары')
        user_markup_food.row('Продуктовые магазины')
        user_markup_food.row('Back'+u'\U0001F519')
        answer = "Вы находитесь в категории, посвященной питанию в нашем городе. \nВыберите следующую категорию"
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_food)

    elif message.text == 'Спорт' + u'\U0001f6b4':
        answer = "Вы находитесь в категории, посвященной спорту в нашем городе."
        user_markup_sports = telebot.types.ReplyKeyboardMarkup()
        user_markup_sports.row('Back' + u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_sports)

    elif message.text == 'Развлечения' + u'\U0001f3a5':
        answer = "Вы находитесь в категории, посвященной развлечениям в нашем городе."
        user_markup_activities = telebot.types.ReplyKeyboardMarkup()
        user_markup_activities.row('Back'+u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_activities)

    elif message.text == 'Инфраструктура' + u'\U0001f3d9':
        user_markup_infrastructure = telebot.types.ReplyKeyboardMarkup()
        user_markup_infrastructure.row('Банки' + u'\U0001F4B0', 'Магазины' + u'\U0001F6D2')
        user_markup_infrastructure.row('Почта' + u'\U0001F4EE', 'Салоны красоты' + u'\U0001F487')
        user_markup_infrastructure.row('Жильё' + u'\U0001F3E1', 'Безопасность' + u'\U0001F46E')
        user_markup_infrastructure.row('Вакансии' + u'\U0001F64B', 'Мэрия' + u'\U0001F3E2')
        user_markup_infrastructure.row('Автомобилистам' + u'\U0001F697')
        user_markup_infrastructure.row("Back" + u'\U0001f519')
        answer = "Вы находитесь в категории, посвященной инфраструктуре нашего города Innopolis. \nВыберите следующую категорию"
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_infrastructure)

    elif message.text == 'Услуги' + u'\U0001f465':
        answer = "Вы находитесь в категории, посвященной услугам в нашем городе."
        user_markup_services = telebot.types.ReplyKeyboardMarkup()
        user_markup_services.row('Back'+u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_services)

    elif message.text == 'Кружки, секции, чаты' + u'\U0001f3a8':
        answer = "Вы находитесь в категории, посвященной кружкам, секциям и чатам  в нашем городе."
        user_markup_associations = telebot.types.ReplyKeyboardMarkup()
        user_markup_associations.row('Back' + u'\U0001F519')
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_associations)

    elif message.text == "Back" + u'\U0001f519':
        handle_start(message)
    # End of Main menu categories

    #elif message.text ==

bot.polling(none_stop=True, interval=0)