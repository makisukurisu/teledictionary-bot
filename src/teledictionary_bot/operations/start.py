from telegram import Update
from telegram.ext import ContextTypes

from teledictionary_bot.settings import settings_instance


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"This is a test start command. My name is: {settings_instance.BOT_NAME}"
    )
