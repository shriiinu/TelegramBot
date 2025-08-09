from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
Token = os.getenv("Telegram_Token")

if Token is None:
    raise ValueError("Telegram_Token environment variable not set")
#command : /start
async def start(update: Update, context):
    await update.message.reply_text("Hello! I am Yepsi :)") 

# Reply to messages with keyword checks
async def echo(update: Update, context):
    user_message = update.message.text.lower()

    # Keyword-based replies
    if "hello" in user_message or "hi" in user_message:
        await update.message.reply_text("Hey there! 👋")
    elif "bye" in user_message:
        await update.message.reply_text("Goodbye! See you soon! 👋")
    elif "how are you" in user_message:
        await update.message.reply_text("I'm doing great, thanks for asking! 😊")
    elif "weather" in user_message:
        await update.message.reply_text("I can’t check the weather yet, but it looks like a good day to code! 🌤️")
    else:
        # Default echo
        await update.message.reply_text(f"You said: {update.message.text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(Token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

