import telebot

# Sustituye 'TU_TOKEN_AQUI' por el token que te dio BotFather
TOKEN = '8159536193:AAEGK6gNB6Wl1hojOjnzoWUNgmiTDHU7lVw'
bot = telebot.TeleBot(TOKEN)

# Responde al comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu primer bot de Telegram. ¿En qué puedo ayudarte?")

# Responde al comando /ayuda
@bot.message_handler(commands=['ayuda'])
def send_help(message):
    bot.reply_to(message, "Puedes enviarme cualquier mensaje y te lo repetiré.")

# Reenvía (eco) cualquier mensaje de texto que reciba
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Me dijiste: {message.text}")

# Inicia el bot
print("El bot está funcionando...")
bot.infinity_polling()
