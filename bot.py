from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8665701318:AAHJb89qsy20WgpS0U_SPtMk2QTqLrLfKKg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti ✅")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")

app.run_polling()