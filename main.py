## -*- coding: utf-8 -*-
import sqlite3
import telebot
from pythonds.basic.stack import Stack
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(config.TOKEN)
stack = Stack()
bold_start = "\033[1m"
bold_end = "\033[0;0m"
print(bold_start + 'Listening...' + bold_end)


# This method handles 'start' press
@bot.message_handler(commands=['start'])
def start_handler(message):
    stack.push(config.menu_markup)
    log(message, message.text)
    bot.send_message(message.chat.id, config.start_text, reply_markup=config.menu_markup)


# This method handles 'help' press
@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, config.help_text)


# This method handles 'start' press
@bot.message_handler(content_types=['text'])
def handle_text(message):
    Handlers()(message)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'test':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Good job!'
        )
        # bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)


def make_inline_blocks(message):
    request = message.text[:-2]
    inline_keyboard = InlineKeyboardMarkup()
    conn = sqlite3.connect(config.db_path)
    if request == 'Главное':
        print()
        cursor = conn.execute(f"SELECT * FROM COMPANY WHERE category = '{request}'")
        msg = ''
        for row in cursor:
            msg += make_card(row)
        bot.send_message(message.chat.id, msg, reply_markup=config.back_markup)
        return 1
    elif request in config.subcategories_with_inline:
        cursor = conn.execute(f"SELECT * FROM COMPANY WHERE subcategory = '{request}'")
        for row in cursor:
            card_title = str(row[1])
            new_inline_button = InlineKeyboardButton(text=card_title, callback_data='test')
            inline_keyboard.add(new_inline_button)
        bot.send_message(message.chat.id, 'Выберите пункт', reply_markup=inline_keyboard)
        return 1
    else:
        return 0


# There are methods for all requests
class Handlers:
    def __init__(self):
        self.handlers = {
            # Menu
            config.buttons['transport']: self.general_handler(config.transport_markup, config.menu_markup),
            config.buttons['main']: self.general_handler(config.back_markup, config.menu_markup),
            config.buttons['medicine']: self.general_handler(config.medicine_markup, config.menu_markup),
            config.buttons['food']: self.general_handler(config.food_markup, config.menu_markup),
            config.buttons['sport']: self.general_handler(config.sport_markup, config.menu_markup),
            config.buttons['activities']: self.general_handler(config.activities_markup, config.menu_markup),
            config.buttons['infrastructure']: self.general_handler(config.infrastructure_markup, config.menu_markup),
            config.buttons['services']: self.general_handler(config.services_markup, config.menu_markup),
            config.buttons['clubs']: self.general_handler(config.clubs_markup, config.menu_markup),
            config.buttons['search']: self.search_handler,  # TODO change to search_markup
            config.buttons['back']: self.back_handler,
            # Transport
            config.buttons['bus']: self.general_handler(config.back_markup, config.transport_markup),
            config.buttons['travel_companions']: self.general_handler(config.back_markup, config.transport_markup),
            config.buttons['taxi']: self.general_handler(config.back_markup, config.transport_markup),
            # Food
            config.buttons['cafe']: self.general_handler(config.back_markup, config.food_markup),
            config.buttons['canteen']: self.general_handler(config.back_markup, config.food_markup),
            config.buttons['grocery_store']: self.general_handler(config.back_markup, config.food_markup),
            config.buttons['delivery_food']: self.general_handler(config.back_markup, config.food_markup),
            config.buttons['other_food']: self.general_handler(config.back_markup, config.food_markup),
            # Medicine
            config.buttons['med_centre']: self.general_handler(config.back_markup, config.medicine_markup),
            config.buttons['pediatrician']: self.general_handler(config.back_markup, config.medicine_markup),
            config.buttons['pharmacy']: self.general_handler(config.back_markup, config.medicine_markup),
            # Infrastructure
            config.buttons['banks']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['post']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['accommodation']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['shops']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['security']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['mayoralty']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['motorists']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['jobs']: self.general_handler(config.back_markup, config.infrastructure_markup),
            config.buttons['beauty_salon']: self.general_handler(config.back_markup, config.infrastructure_markup),
            # Sport
            config.buttons['sport_center']: self.general_handler(config.back_markup, config.sport_markup),
            config.buttons['equipment_rental']: self.general_handler(config.back_markup, config.sport_markup),
            config.buttons['playgrounds']: self.general_handler(config.back_markup, config.sport_markup),
            config.buttons['sport_clubs']: self.general_handler(config.back_markup, config.sport_markup),
            # Main
            config.buttons['security']: self.general_handler(config.back_markup, config.menu_markup),
            # Services
            config.buttons['schools']: self.general_handler(config.back_markup, config.services_markup),
            config.buttons['communications']: self.general_handler(config.back_markup, config.services_markup),
            config.buttons['clothes']: self.general_handler(config.back_markup, config.services_markup),
            config.buttons['photos']: self.general_handler(config.back_markup, config.services_markup),
            config.buttons['eats']: self.general_handler(config.back_markup, config.services_markup),
            config.buttons['laws']: self.general_handler(config.back_markup, config.services_markup),
            config.buttons['habitation']: self.general_handler(config.back_markup, config.services_markup),
            # Activities
            config.buttons['active_rest']: self.general_handler(config.back_markup, config.activities_markup),
            config.buttons['helpful_info']: self.general_handler(config.back_markup, config.activities_markup),
            # Clubs
            config.buttons['active_rest']: self.general_handler(config.back_markup, config.clubs_markup),
            config.buttons['rest']: self.general_handler(config.back_markup, config.clubs_markup),
            config.buttons['social']: self.general_handler(config.back_markup, config.clubs_markup),
            config.buttons['development']: self.general_handler(config.back_markup, config.clubs_markup),
            config.buttons['language']: self.general_handler(config.back_markup, config.clubs_markup),
            config.buttons['other_clubs']: self.general_handler(config.back_markup, config.clubs_markup),
        }

    def __call__(self, *args, **kwargs):
        message = args[0]
        if message.text in self.handlers:
            self.handlers[message.text](message)
        else:
            answer = "На данный момент я не могу обрабатывать такие запросы"
            bot.send_message(message.from_user.id, answer)
            print(f"No handle for {message.text}")

    # Handlers
    def search_handler(self, message):
        # bot.register_next_step_handler() #TODO реализовать поиск по бд и вывести результат
        stack.push(config.menu_markup)
        log(message, message.text)
        bot.send_message(message.from_user.id, config.func_dev_text, reply_markup=config.back_markup)

    def back_handler(self, message):
        log(message, message.text)
        if not stack.isEmpty():
            bot.send_message(message.from_user.id, config.menu_text, reply_markup=stack.pop())

    def general_handler(self, markup, previous_markup):
        def handler(message):
            stack.push(previous_markup)
            log(message, message.text)
            if make_inline_blocks(message) == 0:
                bot.send_message(message.from_user.id, config.menu_text, reply_markup=markup)

        return handler


def make_card(row):
    card = '\n' + f'{str(row[1])}'  # card_title
    card += '\n' + f'Описание: ' + str(row[4])  # card description
    if not str(row[5]) == '':
        card += '\n' + f'Адресс: {str(row[5])}'
    if not str(row[6]) == '':
        card += '\n' + f'Телефон: {str(row[6])}'
    if not str(row[7]) == '':
        card += f'Граифик работы:\n{str(row[7])}'
    card += '\n' + f'Telegram: {str(row[8])}' + '\n' + " "
    return card


# This function print message info
def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print(f"Сообщение от {message.from_user.first_name} {message.from_user.last_name}. (id={message.from_user.id})")
    print(answer + '\n')


config.create_keyboards()
bot.polling(none_stop=True, interval=0)
