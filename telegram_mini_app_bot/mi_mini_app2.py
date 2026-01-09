import telebot
import json
from telebot import types

TOKEN = '8159536193:AAEGK6gNB6Wl1hojOjnzoWUNgmiTDHU7lVw'
bot = telebot.TeleBot(TOKEN)
URL_APP = 'https://yankielap.github.io/telegram_mini_app_web'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Botón que abre la Mini App
    btn = types.KeyboardButton("🚀 Abrir Panel de Soporte", web_app=types.WebAppInfo(URL_APP))
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "¡Bienvenido! Usa el botón de abajo para gestionar tus reportes:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_app_data(message):
    # Recibimos el JSON enviado por tg.sendData()
    data = json.loads(message.web_app_data.data)

    tipo = data.get('tipo', 'Desconocido')
    desc = data.get('desc', 'Sin descripción')

    respuesta = (
        "✅ **Reporte Recibido**\n\n"
        f"**Categoría:** {tipo.capitalize()}\n"
        f"**Descripción:** {desc}\n\n"
        "Nuestro equipo lo revisará pronto."
    )

    bot.send_message(message.chat.id, respuesta, parse_mode="Markdown")

if __name__ == "__main__":
    print("Bot encendido...")
    bot.infinity_polling()