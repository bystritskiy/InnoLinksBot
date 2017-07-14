

from parser import create_database, fill_database

import sqlite3
import telebot
import config
from table import Table, Block, Category, Subcategory
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from flask import Flask, request



bot = telebot.TeleBot(config.TOKEN, threaded=False)

DATABASE = '/home/InnoLinksBot/mysite/database/test.db'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def start_app():
    return '!'

@app.route('/update')
def update_data():
    create_database(app.config['DATABASE'])
    fill_database(app.config['DATABASE'])
    update_bot()
    bot.send_message('57344339', 'Your majesty, I was updated!')
    return config.update_text



print('Listening...')
bot.send_message('57344339', 'I announce my loyalty to the Emperor.')

def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {} {}. (id={})".format(message.from_user.first_name, message.from_user.last_name, message.from_user.id))
    print(answer + '\n')


@bot.message_handler(commands=['start'])
def start_handler(message):
    log(message, message.text)
    bot.send_message(message.chat.id, config.start_text, reply_markup=create_menu_markup())


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, config.help_text, disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    handler.handle(message)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    block = handler.cards[c.data]
    bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=create_card(block),
        parse_mode='HTML',
        disable_web_page_preview=True
    )


class Handler:
    def __init__(self):
        self.clicked_category = ''
        self.clicked_subcategory = ''
        self.categories = set()
        self.subcategories = set()
        self.cards = {}
        self.subs = {}

    def handle(self, *args, **kwargs):
        fill_table()
        message = args[0]
        if message.text in self.categories:
            category_handler(message)
        elif message.text in self.subcategories:
            subcategory_handler(message)
        elif message.text == config.buttons['back']:
            back_handler(message)
        else:
            bot.send_message(message.from_user.id, config.no_handler_text, disable_web_page_preview=True,
                             parse_mode='HTML')
            print("No handle for {}".format(message.text))


def category_handler(message):
    log(message, message.text)
    subcategory_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    subcategories = []
    for subcategory in table.dict_categories[message.text].dict_subcategories.keys():

        subcategories.append(subcategory)
    index = 0
    if len(subcategories) % 2 == 0:
        while index < len(subcategories):
            subcategory_markup.row(subcategories[index], subcategories[index + 1])
            index += 2
        subcategory_markup.row(config.buttons['back'])
    else:
        while index < len(subcategories) - 1:
            subcategory_markup.row(subcategories[index], subcategories[index + 1])
            index += 2
        subcategory_markup.row(subcategories[index], config.buttons['back'])
    bot.send_message(message.chat.id, config.category_text.format(message.text), reply_markup=subcategory_markup,
                     parse_mode='HTML', disable_web_page_preview=True)


def subcategory_handler(message):

    log(message, message.text)
    inline_keyboard = InlineKeyboardMarkup()
    blocks = []
    for block in handler.subs[message.text].dict_blocks.keys():
        blocks.append(block)
    if len(blocks) == 1:
        block = handler.subs[message.text].dict_blocks[blocks[0]]
        bot.send_message(message.chat.id, create_card(block), parse_mode='HTML', disable_web_page_preview=True)
    else:
        for name in blocks:
            new_inline_button = InlineKeyboardButton(text=name, callback_data=name)
            inline_keyboard.add(new_inline_button)
        bot.send_message(message.chat.id, config.chose_text, reply_markup=inline_keyboard,
                             disable_web_page_preview=True, parse_mode='HTML')


def back_handler(message):
    bot.send_message(message.chat.id, config.menu_text, reply_markup=create_menu_markup(), parse_mode='HTML',
                     disable_web_page_preview=True)


def fill_table():
    connection = sqlite3.connect(app.config['DATABASE'])
    cursor = connection.execute('SELECT * FROM COMPANY')
    for row in cursor:
        name = str(row[1])
        category = str(row[2])
        subcategory = str(row[3])
        description = str(row[4])
        address = str(row[5])
        phone = str(row[6])
        schedule = str(row[7])
        link = str(row[8])
        block = Block(name, category, subcategory, description, address, phone, schedule, link)

        handler.cards[name] = block
        handler.categories.add(category)
        handler.subcategories.add(subcategory)

        # if there is no such category
        if table.dict_categories.get(category) is None:
            new_subcategory = Subcategory(subcategory)  # create new subcategory
            new_subcategory.dict_blocks[name] = block  # put new block in dictionary
            new_category = Category(category)  # create new category
            new_category.dict_subcategories[subcategory] = new_subcategory  # put this subcategory in dictionary
            handler.subs[subcategory]=new_subcategory
            table.dict_categories[category] = new_category  # add new category in table

        # if there is no such subcategory
        elif table.dict_categories.get(category).dict_subcategories.get(subcategory) is None:
            new_subcategory = Subcategory(subcategory)  # create new subcategory
            new_subcategory.dict_blocks[name] = block  # put new block in dictionary
            table.dict_categories.get(category).dict_subcategories[
                subcategory] = new_subcategory  # put new subcategory in category's dictionary
            handler.subs[subcategory]=new_subcategory

        # add new block in subcategory
        elif table.dict_categories.get(category).dict_subcategories.get(subcategory).dict_blocks.get(name) is None:
            table.dict_categories.get(category).dict_subcategories.get(subcategory).dict_blocks[
                name] = block  # add new block in subcategory
            handler.subs[subcategory]=table.dict_categories.get(category).dict_subcategories.get(subcategory)

            # print(table.dict_categories[category].name, "->",
            #       table.dict_categories[category].dict_subcategories[subcategory].name,"->",
            #       table.dict_categories[category].dict_subcategories[subcategory].dict_blocks[name].name)


def create_menu_markup():
    categories = []
    new_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for category in table.dict_categories.keys():
        categories.append(category)
    index = 0
    if len(categories) % 2 == 0:
        while index < len(categories):
            new_markup.row(categories[index], categories[index + 1])
            index += 2
    else:
        while index < len(categories) - 1:
            new_markup.row(categories[index], categories[index + 1])
            index += 2
        new_markup.row(categories[index])
    return new_markup


def create_card(block):
    card = '<b>{}</b>'.format(block.name)
    card += '\n' + '<i>{} / {}</i>'.format(block.category, block.subcategory)
    card += '\n' + '<b>Описание:</b> {}'.format(block.description)
    if not block.address == '':
        card += '\n' + '<b>Адрес:</b> {}'.format(block.address)
    if not block.phone == '':
        card += '\n' + '<b>Телефон:</b> {}'.format(block.phone)
    if not block.schedule == '':
        card += '\n' + '<b>График работы:</b>\n{}'.format(block.schedule)
    if not block.link == '':
        card += '\n' + '<b>Telegram:</b>\n{}'.format(block.link)
    return card

def update_bot():
    global table, handler
    table = Table()
    handler = Handler()
    fill_table()

update_bot()



@app.route('/{}'.format(config.TOKEN), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/set")
def webhook():
    bot.remove_webhook()
    bot.set_webhook("https://innolinksbot.pythonanywhere.com/{}".format(config.TOKEN))
    return "Webhook is setted successfully", 200







