import telebot
from currency_converter import CurrencyConverter
from telebot import types

currency = CurrencyConverter()

bot = telebot.TeleBot('8074439906:AAE_cTas9Cye_jsGmxpvYKegQBHgVcZ_SX0')
amount = 0

CURRENCIES = {
    'RUB': '🇷🇺 RUB',
    'USD': '🇺🇸 USD',
    'EUR': '🇪🇺 EUR',
    'GBP': '🇬🇧 GBP',
    'CNY': '🇨🇳 CNY',
    'AED': '🇦🇪 AED',
    'KZT': '🇰🇿 KZT'
}

@bot.message_handler(commands=['start', 'hello'])

def main(message):
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


        btn1 = types.InlineKeyboardButton('RUB🇷🇺→ USD🇺🇸', callback_data='RUB/USD')
        btn2 = types.InlineKeyboardButton('USD🇺🇸 → RUB🇷🇺', callback_data='USD/RUB')
        btn3 = types.InlineKeyboardButton('RUB🇷🇺 → EUR🇪🇺', callback_data='RUB/EUR')
        btn4 = types.InlineKeyboardButton('EUR🇪🇺 → RUB🇷🇺', callback_data='EUR/RUB')
        btn5 = types.InlineKeyboardButton('RUB🇷🇺 → GBP🇬🇧', callback_data='RUB/GBP')
        btn6 = types.InlineKeyboardButton('GBP🇬🇧 → RUB🇷🇺', callback_data='GBP/RUB')
        btn7 = types.InlineKeyboardButton('RUB🇷🇺 → CNY🇨🇳', callback_data='RUB/CNY')
        btn8 = types.InlineKeyboardButton('CNY🇨🇳 → RUB🇷🇺', callback_data='CNY/RUB')
        btn9 = types.InlineKeyboardButton('RUB🇷🇺 → AED🇦🇪', callback_data='RUB/AED')
        btn10 = types.InlineKeyboardButton('AED🇦🇪 → RUB🇷🇺', callback_data='AED/RUB')
        btn11 = types.InlineKeyboardButton('RUB🇷🇺 → KZT🇰🇿', callback_data='RUB/KZT')
        btn12 = types.InlineKeyboardButton('KZT🇰🇿 → RUB🇷🇺', callback_data='KZT/RUB')
        btn13 = types.InlineKeyboardButton('Другая валюта', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12,btn13)


        bot.send_message(message.chat.id, 'Выберите валютную пару из списка или введите свою 💱', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0. Введите сумму')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    value = call.data.upper().split('/')
    res = currency.convert(value[0], value[1])




    if value[1] == 'USD':
        bot.send_message(call.message.chat.id, f'{amount}RUB = {round(res, 2)}USD. Можете ввести другую сумму💸')
    elif value[1] == 'EUR':
        bot.send_message(call.message.chat.id, f'{amount}RUB = {round(res, 2)}EUR. Можете ввести другую сумму💸')
    elif value[1] == 'GBP':
        bot.send_message(call.message.chat.id, f'{amount}RUB = {round(res, 2)}GBP. Можете ввести другую сумму💸')
    elif value[1] == 'CNY':
        bot.send_message(call.message.chat.id, f'{amount}RUB = {round(res, 2)}CNY. Можете ввести другую сумму💸')
    elif value[1] == 'KZT':
        bot.send_message(call.message.chat.id, f'{amount}RUB = {round(res, 2)}KZT. Можете ввести другую сумму💸')
    elif value[1] == 'AED':
        bot.send_message(call.message.chat.id, f'{amount}RUB = {round(res, 2)}AED. Можете ввести другую сумму💸')

    if value[0] == 'USD':
        bot.send_message(call.message.chat.id, f'{amount}USD = {round(res, 2)}RUB. Можете ввести другую сумму💸')
    elif value[0] == 'EUR':
        bot.send_message(call.message.chat.id, f'{amount}EUR = {round(res, 2)}RUB. Можете ввести другую сумму💸')
    elif value[0] == 'GBP':
        bot.send_message(call.message.chat.id, f'{amount}GBP = {round(res, 2)}RUB. Можете ввести другую сумму💸')
    elif value[0] == 'CNY':
        bot.send_message(call.message.chat.id, f'{amount}CNY = {round(res, 2)}RUB. Можете ввести другую сумму💸')
    elif value[0] == 'KZT':
        bot.send_message(call.message.chat.id, f'{amount}KZT = {round(res, 2)}RUB. Можете ввести другую сумму💸')
    elif value[0] == 'AED':
        bot.send_message(call.message.chat.id, f'{amount}AED = {round(res, 2)}RUB. Можете ввести другую сумму💸')
    bot.register_next_step_handler(call.message, summa)

bot.polling(none_stop=True)
