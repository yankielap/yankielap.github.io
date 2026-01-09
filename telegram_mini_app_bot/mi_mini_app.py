import telebot
from telebot import types

TOKEN = '8159536193:AAEGK6gNB6Wl1hojOjnzoWUNgmiTDHU7lVw'
bot = telebot.TeleBot(TOKEN)
# URL donde subiste tu index.html
WEB_APP_URL = 'https://yankielap.github.io/telegram-mini-app'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    # Creamos el botón que lanza la Web App
    web_app_info = types.WebAppInfo(WEB_APP_URL)
    btn = types.KeyboardButton("Abrir Mi Aplicación", web_app=web_app_info)
    markup.add(btn)

    bot.send_message(message.chat.id, "Presiona el botón de abajo para abrir la Mini App:", reply_markup=markup)

@bot.message_handler(commands=['check'])
def start(message):
    bot.send_message(message.chat.id, "Todo bien!")

# Captura los datos enviados desde la Mini App (vía tg.sendData)
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    bot.send_message(message.chat.id, f"Recibí esto de la App: {message.web_app_data.data}")

bot.infinity_polling()
