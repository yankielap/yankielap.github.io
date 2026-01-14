import telebot
import json
from datetime import datetime

TOKEN = '8159536193:AAEGK6gNB6Wl1hojOjnzoWUNgmiTDHU7lVw'
bot = telebot.TeleBot(TOKEN)

def log_transaction(user_id, action):
    with open("transacciones.log", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] User: {user_id} - Action: {action}\n")

@bot.message_handler(content_types=['web_app_data'])
def handle_app_data(message):
    data = json.loads(message.web_app_data.data)
    action = data.get('action')

    # Registrar la operación en tu servidor Ubuntu
    log_transaction(message.from_user.id, action)

    respuestas = {
        'consultar_saldo': "💰 Saldo verificado: $150.00",
        'ticket_soporte': "🛠️ Ticket #{} creado exitosamente.".format(message.message_id),
        'enviar_pdf': "📄 Generando catálogo..."
    }

    bot.send_message(message.chat.id, respuestas.get(action, "Acción desconocida"))

    if action == 'enviar_pdf':
        # Simulación de envío de archivo local
        bot.send_document(message.chat.id, open('catalogo.pdf', 'rb'))

bot.infinity_polling()