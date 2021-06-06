import logging
import sys
import config
import weather
import telebot
import datetime
import subprocess
from telebot import types
from time import sleep

level = logging.INFO
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logfile = '/weather_bot/tmp/log/weather_bot.log'
logging.basicConfig(format = FORMAT, level=level, filename = logfile )
logger = logging.getLogger(__name__)
debug = logger.debug
print = logger.info

bot = telebot.TeleBot(config.token)
keyboard = types.ReplyKeyboardMarkup()
geo = types.KeyboardButton(text='Погода по геолокации 🌎', request_location=True)

keyboard.row('Москва', 'Питер', 'Тверь', 'Ереван')
keyboard.row('Метеорологическая карта 🗺')
keyboard.add(geo)
keyboard.row('Donate 💰')

@bot.message_handler(commands=['start'])
def start_message(message):
    print('New user: ' +
            '{"username": "' + str(message.from_user.username) +
            '", "id": ' + str(message.from_user.id) +
            ', "first_name": "' + str(message.from_user.first_name) + '", "last_name": "' + str(message.from_user.last_name) + '"}')
    bot.send_sticker(message.chat.id,

                     'CAACAgUAAxkBAAIDE1448lrMpAvcNM-Qqjq50hVuDTtGAAKAAwAC6QrIA5dYbzvjPsr4GAQ')
    bot.send_message(message.chat.id,
                     'Определение погоды по геолокации!',
                     reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Бот присылает метеосводку по городам из списка или по вашей геолокации.')

@bot.message_handler(commands=['log'])
def log_message(message):
    if message.from_user.username == config.username and message.from_user.id == config.userid:
        doc = open('/weather_bot/tmp/log/weather_bot.log','rb')
        bot.send_document(message.chat.id, doc)
        doc.close()

@bot.message_handler(commands=['js'])
def log_message(message):
    if message.from_user.username == config.username and message.from_user.id == config.userid:
        proc = subprocess.Popen('/weather_bot/collect_stat.sh', stdout=subprocess.PIPE)
        output = proc.stdout.read()
        bot.send_message(message.chat.id, output)
        doc = open('/weather_bot/tmp/json/bot_users.js','rb')
        bot.send_document(message.chat.id, doc)
        doc.close()
        doc = open('/weather_bot/tmp/json/users_geoloc.js','rb')
        bot.send_document(message.chat.id, doc)
        doc.close()

@bot.message_handler(commands=['debug'])
def debug_message(message):
    if message.from_user.username == config.username and message.from_user.id == config.userid:
        bot.send_message(message.chat.id, str(message))
        return

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Москва':
        info = weather.weather('Moscow,RU')
        bot.send_message(message.chat.id,
                         "~~~~~~~~~~~~~~~~~~~~" + "\n" +
                         'Погода в Москве на ' +
                         datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "\n" +
                         str(info.get('stat')) + "\n" +
                         str(info.get('wind')) + "\n" +
                         str(info.get('hum')) + "\n" +
                         str(info.get('temp')) + "\n" +
                         "~~~~~~~~~~~~~~~~~~~~")
    elif message.text == 'Питер':
        info = weather.weather('Saint Petersburg,RU')
        bot.send_message(message.chat.id,
                         "~~~~~~~~~~~~~~~~~~~~" + "\n" +
                         'Погода в Санкт-Петербурге на ' +
                         datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "\n" +
                         str(info.get('stat')) + "\n" +
                         str(info.get('wind')) + "\n" +
                         str(info.get('hum')) + "\n" +
                         str(info.get('temp')) + "\n" +
                         "~~~~~~~~~~~~~~~~~~~~")
    elif message.text == 'Тверь':
        info = weather.weather('Tver,RU')
        bot.send_message(message.chat.id,
                         "~~~~~~~~~~~~~~~~~~~~" + "\n" +
                         'Погода в Твери на ' +
                         datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "\n" +
                         str(info.get('stat')) + "\n" +
                         str(info.get('wind')) + "\n" +
                         str(info.get('hum')) + "\n" +
                         str(info.get('temp')) + "\n" +
                         "~~~~~~~~~~~~~~~~~~~~")
    elif message.text == 'Ереван':
        info = weather.weather('Yerevan,AM')
        bot.send_message(message.chat.id,
                         "~~~~~~~~~~~~~~~~~~~~" + "\n" +
                         'Погода в Ереване на ' +
                         datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "\n" +
                         str(info.get('stat')) + "\n" +
                         str(info.get('wind')) + "\n" +
                         str(info.get('hum')) + "\n" +
                         str(info.get('temp')) + "\n" +
                         "~~~~~~~~~~~~~~~~~~~~")
    elif message.text == 'Метеорологическая карта 🗺':
        print('Button pressed: Meteo map ' +
                '{"user_id": ' + str(message.from_user.id) + '}')
        bot.send_animation(message.chat.id,
                           'https://static.tildacdn.com/tild6665-6138-4735-b430-393531373732/01.gif')
    elif message.text == 'Donate 💰':
        print('Button pressed: Donate ' + 
                '{"username": "' + str(message.from_user.username) + 
                '", "id": ' + str(message.from_user.id) + 
                ', "first_name": "' + str(message.from_user.first_name) + '", "last_name": "' + str(message.from_user.last_name) + '"}')
        markup = types.InlineKeyboardMarkup()
        btn_50 = types.InlineKeyboardButton(text='50 руб.',
                                            url='https://money.yandex.ru/to/4100111748072190/50')
        btn_100 = types.InlineKeyboardButton(text='100 руб.',
                                             url='https://money.yandex.ru/to/4100111748072190/100')
        btn_200 = types.InlineKeyboardButton(text='200 руб.',
                                             url='https://money.yandex.ru/to/4100111748072190/200')
        markup.add(btn_50, btn_100, btn_200)
        bot.send_message(message.chat.id,
                         "Помогите нашему проекту стать еще лучше! 🔝🔝🔝",
                         reply_markup=markup)
    else:
        bot.send_sticker(message.chat.id,
                         'CAACAgUAAxkBAAIC3F447q5L0RXMOb5Jv-AeJAfb5VvGAAKBAwAC6QrIA0N0OWENjsi5GAQ')
        bot.send_message(message.chat.id,
                         'Ваш запрос не распознан, попробуйте еще раз.')

@bot.message_handler(content_types=["location"])
def send_weather_by_location(message):
    if message.location is not None:
        print('Button pressed: Geolocation {"lat": ' + str(message.location.latitude) +
                ', "lon": ' + str(message.location.longitude) +
                ', "username": "' + str(message.from_user.username) + 
                '", "id": ' + str(message.from_user.id) + 
                ', "first_name": "' + str(message.from_user.first_name) + '", "last_name": "' + str(message.from_user.last_name) + '"}')
        lat = float('{0:.2f}'.format(message.location.latitude))
        lon = float('{0:.2f}'.format(message.location.longitude))
        info = weather.weather_coord(lat, lon)
        bot.send_message(message.chat.id,
                         "~~~~~~~~~~~~~~~~~~~~" + "\n" +
                         str(info.get('stat')) + "\n" +
                         str(info.get('wind')) + "\n" +
                         str(info.get('hum')) + "\n" +
                         str(info.get('temp')) + "\n" +
                         "~~~~~~~~~~~~~~~~~~~~")
    else:
        bot.send_sticker(message.chat.id,
                         'CAACAgUAAxkBAAIC3F447q5L0RXMOb5Jv-AeJAfb5VvGAAKBAwAC6QrIA0N0OWENjsi5GAQ')
        bot.send_message(message.chat.id,
                         'Ваш запрос не распознан, попробуйте еще раз.')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        sleep(15)
