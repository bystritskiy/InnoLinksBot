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
    user_markup_main_menu.row('Главное', 'Транспорт')
    user_markup_main_menu.row('Медицина', 'Еда')
    user_markup_main_menu.row('Спорт', 'Развлечения')
    user_markup_main_menu.row('Инфраструктура', 'Услуги')
    user_markup_main_menu.row('Кружки, секции, чаты')
    log(message, message.text)
    bot.send_message(message.chat.id, 'Выберите одну из категорий', reply_markup=user_markup_main_menu)

@bot.message_handler(commands=['help'])
def command_handler(message):
    bot.send_message(message.chat.id, "Я собираюсь помочь тебе")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Главное":
        answer = "Вы находитесь в категории, в которой находятся самые необходимые ссылки и информация в нашем городе. \nВыберите следующую категорию"
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Транспорт":
        answer = "Вы находитесь в категории, посвященной транспорту в нашем городе."
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Медицина":
        answer = "Вы находитесь в категории, посвященной медицине в нашем городе."
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Еда":
        user_markup_food = telebot.types.ReplyKeyboardMarkup()
        user_markup_food.row('Столовые', 'Кафе и бары')
        user_markup_food.row('Продуктовые магазины', 'Back')
        answer = "Вы находитесь в категории, посвященной питанию в нашем городе. \nВыберите следующую категорию"
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_food)

    elif message.text == "Спорт":
        answer = "Вы находитесь в категории, посвященной спорту в нашем городе."
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Развлечения":
        answer = "Вы находитесь в категории, посвященной развлечениям в нашем городе."
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Инфраструктура":
        user_markup_infrastructure = telebot.types.ReplyKeyboardMarkup()
        user_markup_infrastructure.row('Банки', 'Магазины')
        user_markup_infrastructure.row('Почта', 'Салоны красоты')
        user_markup_infrastructure.row('Жильё', 'Безопасность')
        user_markup_infrastructure.row('Вакансии', 'Мэрия')
        user_markup_infrastructure.row('Автомобилистам', "Back")
        answer = "Вы находитесь в категории, посвященной инфраструктуре нашего города Innopolis. \nВыберите следующую категорию"
        log(message, message.text)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup_infrastructure)

    elif message.text == "Услуги":
        answer = "Вы находитесь в категории, посвященной услугам в нашем городе."
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Кружки, секции, чаты":
        answer = "Вы находитесь в категории, посвященной кружкам, секциям и чатам  в нашем городе."
        log(message, message.text)
        bot.send_message(message.from_user.id, answer)

    elif message.text == "Back":
        handle_start(message)

bot.polling(none_stop=True, interval=0)