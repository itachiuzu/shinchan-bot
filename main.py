import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😆 Shinchan aa gaya!\n\n"
        "Buri buri zaemon! 😂\n"
        "Bot successfully online hai."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Shinchan Bot\n\n"
        "/start - Bot start karo\n"
        "/help - Help"
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN Secret nahi mila!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Shinchan Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()