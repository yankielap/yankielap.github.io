import telebot
import json

TOKEN = '8159536193:AAEGK6gNB6Wl1hojOjnzoWUNgmiTDHU7lVw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['web_app_data'])
def handle_app_data(message):
    # Leer lo que envió la Mini App
    data = json.loads(message.web_app_data.data)
    action = data.get('action')

    if action == 'consultar_saldo':
        bot.send_message(message.chat.id, "💰 Tu saldo actual es de **$150.00 USD**.", parse_mode="Markdown")

    elif action == 'ticket_soporte':
        bot.send_message(message.chat.id, "🛠️ Se ha creado un ticket. Un técnico te contactará en breve.")

    elif action == 'enviar_pdf':
        bot.send_chat_action(message.chat.id, 'upload_document')
        # Supongamos que tienes el PDF en la misma carpeta que el bot
        try:
            with open('catalogo.pdf', 'rb') as doc:
                bot.send_document(message.chat.id, doc, caption="Aquí tienes nuestro nomenclador completo.")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "❌ Error: El catálogo no está disponible en el servidor local.")

bot.infinity_polling()