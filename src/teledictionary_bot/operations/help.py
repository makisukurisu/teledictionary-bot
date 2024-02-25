from telegram import Update
from telegram.ext import ContextTypes

from teledictionary_bot.enums import StringNames
from teledictionary_bot.strings import get


async def help_method(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    message_text = get.get_string(StringNames.HELP_MESSAGE, update)
    await update.message.reply_text(message_text)
