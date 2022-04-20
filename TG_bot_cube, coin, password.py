import telebot
from random import *
from telebot import types


# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я экспериментальный бот для реализации разных идей')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Бросить кубики")
    item2 = types.KeyboardButton("Бросить монету")
    item3 = types.KeyboardButton("Генерация криптостойкого пароля")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Выбери из предложенного: ', reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1
    if message.text.strip() == 'Бросить кубики':
        a = randint(1, 6)
        b = randint(1, 6)
        ans = 'Значение граней: ' + str(a) + ' - ' + str(b)
        bot.send_message(message.chat.id, ans)  # Отсылаем юзеру сообщение в его чат

    # Если юзер прислал 2
    elif message.text.strip() == 'Бросить монету':
        a = randint(0, 1)
        ans = 'Результат броска: '
        if a == 0:
            ans += 'Орёл'
        else:
            ans += 'Решка'
        bot.send_message(message.chat.id, ans)

    # Если юзер прислал 3
    elif message.text.strip() == 'Генерация криптостойкого пароля':
        digits = '0123456789'
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        uppercase_letters = lowercase_letters.upper()
        punctuation = '!#$%&*+-=?@^_'
        # Пароль называется криптостойким, если он включает в себя
        # и строчные латинские буквы, и заглавные латинские буквы, и цифры,
        # при этом его длина должна быть не менее 8 символов (в боте ровно 8)
        password = []
        for _ in range(2):
            password.append(choice(digits))
            password.append(choice(lowercase_letters))
            password.append(choice(uppercase_letters))
            password.append(choice(punctuation))
        shuffle(password)
        pwd = ''.join(password)
        pwd = 'Пароль: ' + pwd
        bot.send_message(message.chat.id,  pwd)

    elif message.text == "привет" or message.text == "Привет":
        bot.send_message(message.from_user.id, 'Привет! Напиши /start или выбери кнопку')
    else:
        bot.send_message(message.from_user.id, "Я выполняю только заложенные в меня функции. Для начала работы: /start")


# Запускаем бота
bot.polling(none_stop=True, interval=0)
