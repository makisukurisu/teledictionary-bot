from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from teledictionary_bot.database.dictionaries import get_dictionaries
from teledictionary_bot.database.user import add_or_update_user
from teledictionary_bot.enums import CommandNames, StringNames
from teledictionary_bot.models.user import User
from teledictionary_bot.operations.start import start_inline_keyboard
from teledictionary_bot.strings import get


async def select_dictionary(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer("")

    buttons = []

    dictionaries = get_dictionaries()
    for dictionary in dictionaries:
        buttons.append(
            [
                InlineKeyboardButton(
                    dictionary.name,
                    callback_data=CommandNames.choose_dictionary(dictionary.id),
                )
            ]
        )

    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.edit_message_text(
        text=get.get_string(StringNames.SELECT_DICTIONARY_BUTTON, update),
        reply_markup=keyboard,
    )


async def choose_dictionary(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer(
        text=get.get_string(StringNames.CHOOSE_DICTIONARY_TEXT, update),
    )

    add_or_update_user(
        User(
            user_id=update.effective_user.id,
            dictionary_id=update.callback_query.data.split(";")[1],
        )
    )

    await update.callback_query.edit_message_text(
        text=get.get_start_string(update),
        reply_markup=start_inline_keyboard(update),
    )
