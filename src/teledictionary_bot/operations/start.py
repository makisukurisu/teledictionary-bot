from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from teledictionary_bot.enums import StringNames
from teledictionary_bot.settings import settings_instance
from teledictionary_bot.strings import get


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    bot_username = update.get_bot().username

    buttons = [
        [
            InlineKeyboardButton(
                text=get.get_string(StringNames.SELECT_DICTIONARY, update),
                callback_data="select_dictionary",
            )
        ],
        [
            InlineKeyboardButton(
                text=get.get_string(StringNames.REMOVE_DATA, update),
                callback_data="remove_data",
            )
        ],
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    message_text = get.get_string(StringNames.START_MESSAGE, update).format(
        bot_name=settings_instance.BOT_NAME,
        bot_username=bot_username,
    )

    await update.message.reply_text(
        text=message_text,
        reply_markup=keyboard,
    )
