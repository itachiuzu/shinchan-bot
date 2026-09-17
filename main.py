import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PORT = int(os.getenv("PORT", "10000"))
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😆 Shinchan aa gaya!\n\n"
        "Buri buri zaemon! 😂\n"
        "Bot successfully online hai.\n\n"
        "Type /help to see commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Shinchan Bot\n\n"
        "/start - Bot start karo\n"
        "/help - Help"
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN missing hai!")

    if not RENDER_URL:
        raise RuntimeError("RENDER_EXTERNAL_URL missing hai!")

    if not WEBHOOK_SECRET:
        raise RuntimeError("WEBHOOK_SECRET missing hai!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    webhook_url = f"{RENDER_URL}/telegram"

    print("Shinchan Bot starting...")
    print(f"Webhook: {webhook_url}")

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="telegram",
        webhook_url=webhook_url,
        secret_token=WEBHOOK_SECRET,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()