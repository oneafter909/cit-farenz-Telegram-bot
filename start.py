from telegram.ext import *
import telegram as tg
from telegram import InputMediaPhoto
import os
bot = tg.Bot('')
def citaMarco(update, context):
	testo = str(update.message.text)
	quote_text = ""
	reply_to_message = update.message.reply_to_message
	if reply_to_message is None:
		if("/cita@citfarenzbot" in testo): quote_text = testo.replace("/cita@citfarenzbot", "")
		elif ("/cita" in testo ): quote_text = testo.replace("/cita", "")
		if quote_text != "":
			os.system("python3 MakeImage.py \""+ quote_text +"\" temp.png")
			chat_id = update.message.chat.id
			photo_farenz = open("temp.png", 'rb')
			bot.send_photo(chat_id=chat_id, photo=photo_farenz)
		else:
			update.message.reply_text("Inserisci il testo!")
	else:	
		quote_text = reply_to_message.text
		if quote_text != "":
			os.system("python3 MakeImage.py \""+ quote_text +"\" temp.png")
			chat_id = update.message.chat.id
			photo_farenz = open("temp.png", 'rb')
			bot.send_photo(chat_id=chat_id, photo=photo_farenz)

def Pane(update, context):
	chatID = update.message.chat_id
	bot.send_message(chat_id=chatID, text="Sto funzionando.")

def startCommand(update, context):
	update.message.reply_text("Scrivi \"/cita Testo che vuoi\"\nper far dire al maestro quello che vuoi")

def helpCommand(update, context):
	update.message.reply_text("Scrivi \"/cita Testo che vuoi \"per far dire al maestro quello che vuoi")

def error(update, context):
	print("ERRORE")
	print(f"Python {context.error}")

def main():
	updater = Updater(keys.TOKEN, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", startCommand))
	dp.add_handler(CommandHandler("helpcitfarenz", helpCommand))
	dp.add_handler(CommandHandler("pane", Pane))
	dp.add_handler(CommandHandler("cita", citaMarco))
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

main()
