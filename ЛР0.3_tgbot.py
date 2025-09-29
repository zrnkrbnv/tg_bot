import telebot
from currency_converter import CurrencyConverter
from telebot import types
bot = telebot.TeleBot('8074439906:AAE_cTas9Cye_jsGmxpvYKegQBHgVcZ_SX0')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])

def start(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if first_name and last_name:
        greeting = f'Привет, {first_name} {last_name}! Введите сумму:)'
    elif first_name:
        greeting = f'Привет, {first_name}! Введите сумму:)'
    elif last_name:
        greeting = f'Привет, {last_name}! Введите сумму:)'
    else:
        greeting = 'Привет! Введите сумму:)'
    bot.send_message(message.chat.id, greeting)

    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Введите сумму')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton('RUB🇷🇺 → USD🇺🇸', callback_data='RUB/USD')
        btn2 = types.InlineKeyboardButton('RUB🇷🇺 → EUR🇪🇺', callback_data='RUB/EUR')
        btn3 = types.InlineKeyboardButton('RUB🇷🇺 → GBP🇬🇧', callback_data='RUB/GBP')
        btn4 = types.InlineKeyboardButton('RUB🇷🇺 → CNY🇨🇳', callback_data='RUB/CNY')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите валютную пару из списка 💱', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0. Введите сумму')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    values = call.data.split('/')
    res = currency.convert(amount, values[0], values[1])
    if values[1] == 'USD':
        bot.send_message(call.message.chat.id, f'{amount} RUB = {round(res, 2)} USD\nМожете ввести другую сумму💸')
    elif values[1] == 'EUR':
        bot.send_message(call.message.chat.id, f'{amount} RUB = {round(res, 2)} EUR\nМожете ввести другую сумму💸')
    elif values[1] == 'GBP':
        bot.send_message(call.message.chat.id, f'{amount} RUB = {round(res, 2)} GBP\nМожете ввести другую сумму💸')
    elif values[1] == 'CNY':
        bot.send_message(call.message.chat.id, f'{amount} RUB = {round(res, 2)} CNY\nМожете ввести другую сумму💸')
    bot.register_next_step_handler(call.message, summa)
bot.polling(none_stop=True)