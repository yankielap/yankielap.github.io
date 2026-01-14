import telebot
from telebot import types
import json
import base64

TOKEN = '8159536193:AAEGK6gNB6Wl1hojOjnzoWUNgmiTDHU7lVw'
bot = telebot.TeleBot(TOKEN)

# Tu sitio estático (ej: GitHub Pages o Vercel)
# Este sí debe ser público para que el celular del usuario lo descargue
URL_BASE = 'https://yankielap.github.io/telegram_mini_app_web'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # 1. El Nomenclador que vive en tu servidor local
    nomenclador = [
        {"id": "A1", "n": "Soporte Técnico", "p": 10},
        {"id": "B2", "n": "Consultoría", "p": 25},
        {"id": "C3", "n": "Instalación", "p": 15}
    ]

    # 2. Convertir a JSON y luego a Base64 para que viaje seguro en la URL
    json_data = json.dumps(nomenclador)
    encoded_data = base64.b64encode(json_data.encode()).decode()

    # 3. Construir la URL con el parámetro 'd'
    url_con_datos = f"{URL_BASE}?d={encoded_data}"

    # 4. Crear el botón
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(
        "Abrir App con Datos Actualizados",
        web_app=types.WebAppInfo(url_con_datos)
    )
    markup.add(btn)

    bot.send_message(message.chat.id, "Presiona para ver el nomenclador local:", reply_markup=markup)

bot.infinity_polling()