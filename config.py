import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# BOT TOKEN
TOKEN = '396424405:AAHQZxMEkBdsAkFk2BxSgJBKEQaaoWtjuhc'

# LINKS CONSTANTS
db_path = './database/test.db'
companies_path = './documents/companies.xlsx'

# DATABASE COMMANDS
create_db_command = '''CREATE TABLE COMPANY
                        (id INT PRIMARY KEY NOT NULL,
                        name TEXT ,
                        category TEXT,
                        subcategory TEXT,
                        description TEXT,
                        address TEXT,
                        phone TEXT,
                        schedule TEXT,
                        links TEXT
                        );'''
search_column = "SELECT * FROM COMPANY WHERE category = {}"
chose_column={}

# TEXT CONSTANTS
start_text = '''Я помогу тебе найти информацию о всех организациях в Иннополисе. Если ты не нашел нужной информации,
то можешь позвонить в Консьерж-сервис: 
☎️: 8-800-222-22-87 
📩: helpme@innopolis.ru 
telegram: @InnopolisHelp! '''
menu_text = "Выберите категорию:"
main_text = "Здесь закреплены "
category_text = "Вы находитесь в категории {}. Выберите следующую категорию:"
help_text = 'Я собираюсь помочь тебе'
func_dev_text = 'Функция находится в разработке'

# CATEGORIES WITH INLINE BLOCKS
subcategories_with_inline = [
    'Автобусы',
    'Такси',
    'Чаты',

    'Кафе, бары, пиццерии',
    'Столовые',
    'Продуктовые магазины',
    'Заказ и доставка еды',
    'Прочее',

    'Медицинский центр',
    'Аптеки',

    'Банки',
    'Почта',
    'Жилье',
    'Магазины',
    'Безопасность',
    'Мэрия',
    'Автомобилистам',
    'Вакансии',
    'Салон красоты',

    'Спорткомплекс',
    'Прокат',
    'Секции',

    'Детские школы, сады',
    'Связь, телевидение, интернет',
    'Одежда и аксессуары',
    'Фото, видео, печать',
    'Еда',
    'Правовые институты',
    'Жилье',
    'Полезная информация',

    'Активный отдых',
    'Отдых',
    'Лингвисты',
    'Профессиональное развитие',
    'Прочее',
    'Общение',
]

# BUTTONS FOR KEYBOARDS
buttons = {
    # Main categories
    'search': 'Поиск ' + u'🔍',
    'back': 'Back ' + u'🔙',
    'main': 'Главное ' + u'❗',
    'transport': 'Транспорт ' + u'🚌',
    'medicine': 'Медицина ' + u'🚑',
    'food': 'Питание ' + u'🍽',
    'sport': 'Спорт ' + u'🚴',
    'activities': 'Развлечения ' + u'🎥',
    'infrastructure': 'Инфраструктура ' + u'🏙',
    'services': 'Услуги ' + u'👥',
    'clubs': 'Кружки, секции, чаты ' + u'🎨',

    # Transport
    'bus': 'Автобусы ' + u'🚎',
    'taxi': 'Такси ' + u'🚕',
    'chats_transport': 'Чаты ' + u'👥',

    # Food
    'cafe': 'Кафе, бары, пиццерии ' + u'🍹',
    'canteen': 'Столовые ' + u'🍴',
    'grocery_store': 'Продуктовые магазины ' + u'🛍',
    'delivery_food': 'Заказ и доставка еды ' + u'📦',
    'other_food': 'Прочее ' + u'🍖',

    # Medicine
    'med_centre': 'Медицинский центр ' + u'🏥',
    #'pharmacy': 'Back ' + u'🔙',
    'pharmacy': 'Аптека ' + u'💊',

    # Infrastructure
    'banks': 'Банки ' + u'💰',
    'post': 'Почта ' + u'📮',
    'accommodation': 'Жилье ' + u'🏨',
    'shops': 'Магазины ' + u'🛒',
    'security': 'Безопасность ' + u'👮',
    'mayoralty': 'Мэрия ' + u'🤵',
    'motorists': 'Автомобилистам ' + u'🚘',
    'jobs': 'Вакансии ' + u'🙋‍',
    'beauty_salon': 'Салон красоты ' + u'💅',

    # Sport
    'sport_center': 'Спорткомплекс ' + u'🏋',
    'playgrounds': 'Спортивные площадки ' + u'⛳',
    'equipment_rental': 'Прокат ' + u'🛴',
    'sport_clubs': 'Секции ' + u'🤼',

    # Main
    'InnoHelpBot': 'InnoHelpBot ' + u'ℹ',
    'SuperInnopolis': 'Super Innopolis ' + u'ℹ',
    'concierge service': 'Консьерж сервис ' + u'ℹ',

    # Services
    'schools': 'Детские школы, сады ' + u'👨‍🏫',
    'communications': 'Связь, телевидение, интернет ' + u'📞',
    'clothes': 'Одежда и аксессуары ' + u'🛍',
    'photos': 'Фото, видео, печать ' + u'📷',
    'eats': 'Еда ' + u'🍕',
    'laws': 'Правовые институты ' + u'👩‍💼',
    'habitation': 'Жилье ' + u'🏙️',

    # Activities
    'helpful_info': 'Полезная информация ' + u'ℹ',
    'active_rest': 'Активный отдых ' + u'🏄‍',

    # Clubs
    'rest': 'Отдых ' + u'🏖️',
    'language': 'Лингвисты ' + u'🇬🇧',
    'development': 'Профессиональное развитие ' + u'🕵️',
    'other_clubs': 'Прочее ' + u'✮',
    'social': 'Общение ' + u'👥',

    # Others
}

# REPLY KEYBOARDS:
menu_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
transport_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
medicine_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
food_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
sport_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
infrastructure_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
services_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
activities_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
clubs_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
back_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)


def create_keyboards():
    # Menu keyboard
    menu_markup.row(buttons['search'])
    menu_markup.row(buttons['main'], buttons['transport'])
    menu_markup.row(buttons["medicine"], buttons['food'])
    menu_markup.row(buttons['sport'], buttons['activities'])
    menu_markup.row(buttons['infrastructure'], buttons['services'])
    menu_markup.row(buttons['clubs'])

    # Transport keyboard
    transport_markup.row(buttons['bus'], buttons['taxi'])
    transport_markup.row(buttons['chats_transport'])
    transport_markup.row(buttons['back'])

    # Medicine keyboard
    medicine_markup.row(buttons['med_centre'], buttons['pharmacy'])
    medicine_markup.row(buttons['back'])

    # Food keyboard
    food_markup.row(buttons['canteen'], buttons['cafe'])
    food_markup.row(buttons['grocery_store'], buttons['other_food'])
    food_markup.row(buttons['back'])

    # Sport keyboard
    sport_markup.row(buttons['sport_center'], buttons['equipment_rental'])
    sport_markup.row(buttons['sport_clubs'])
    sport_markup.row(buttons['back'])

    # Infrastructure keyboard
    infrastructure_markup.row(buttons['banks'], buttons['shops'])
    infrastructure_markup.row(buttons['post'], buttons['beauty_salon'])
    infrastructure_markup.row(buttons['accommodation'], buttons['security'])
    infrastructure_markup.row(buttons['jobs'], buttons['mayoralty'])
    infrastructure_markup.row(buttons['motorists'])
    infrastructure_markup.row(buttons['back'])

    # Services keyboard
    services_markup.row(buttons['schools'], buttons['eats'])
    services_markup.row(buttons['communications'], buttons['laws'])
    services_markup.row(buttons['clothes'], buttons['photos'])
    services_markup.row(buttons['back'])

    # Activities keyboard
    activities_markup.row(buttons['clubs'])
    activities_markup.row(buttons['active_rest'])
    activities_markup.row(buttons['helpful_info'])
    activities_markup.row(buttons['back'])

    # Clubs keyboard
    clubs_markup.row(buttons['active_rest'], buttons['rest'])
    clubs_markup.row(buttons['social'], buttons['development'])
    clubs_markup.row(buttons['language'], buttons['other_clubs'])
    clubs_markup.row(buttons['back'])

    # Back keyboard
    back_markup.row(buttons['back'])
