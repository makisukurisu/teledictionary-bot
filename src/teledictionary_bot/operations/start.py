from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from teledictionary_bot.enums import StringNames
from teledictionary_bot.strings import get


def start_inline_keyboard(update: Update) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=get.get_string(StringNames.SELECT_DICTIONARY_BUTTON, update),
                callback_data="select_dictionary",
            )
        ],
        [
            InlineKeyboardButton(
                text=get.get_string(StringNames.REMOVE_DATA_BUTTON, update),
                callback_data="remove_data",
            )
        ],
    ]

    return InlineKeyboardMarkup(buttons)


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        text=get.get_start_string(update),
        reply_markup=start_inline_keyboard(update),
    )
