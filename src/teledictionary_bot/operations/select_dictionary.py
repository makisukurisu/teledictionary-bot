from telegram import Update
from telegram.ext import ContextTypes


async def select_dictionary(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer("You have selected the dictionary", show_alert=True)
