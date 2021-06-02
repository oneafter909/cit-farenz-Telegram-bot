import constanti as keys
from telegram.ext import *
import telegram as tg
from telegram import InputMediaPhoto
import risposta as r
import os
import sys
bot = tg.Bot(keys.TOKEN)
def citaMarco(update, context):
	testo = str(update.message.text)
	citazione = testo.replace("/cita", "")
	os.system("python3 makeImage.py \""+ citazione +"\" temp.png")
	chat_id = update.message.chat.id
	msg_id = update.message.message_id
	fotomaestro = open("temp.png", 'rb')
	bot.send_photo(chat_id=chat_id, photo=fotomaestro)
	
def startCommand(update, context):
	update.message.reply_text("Scrivi \"/cita Testo che vuoi\"\nper far dire al maestro quello che vuoi")

def helpCommand(update, context):
	update.message.reply_text("Scrivi \"/cita Testo che vuoi \"per far dire al maestro quello che vuoi")

def handleMessaggio(update, context):
	text = str(update.message.text).lower()
	response = r.rispondi(text)
	update.message.reply_text(response)

def error(update, context):
	print("ERRORE")
	print(f"Python {context.error}")

def main():
	updater = Updater(keys.TOKEN, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", startCommand))
	dp.add_handler(CommandHandler("helpcitfarenz", helpCommand))
	dp.add_handler(CommandHandler("cita", citaMarco))
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

main()
