import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from teledictionary_bot.database import dictionaries
from teledictionary_bot.enums import CommandNames, StringNames
from teledictionary_bot.models.dictionary import Dictionary
from teledictionary_bot.settings import settings_instance
from teledictionary_bot.strings import get


def verify_is_admin(update: Update) -> bool:
    return str(update.effective_user.id) in settings_instance.BOT_ADMINISTRATORS


async def add_dictionary(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    verify_is_admin(update)

    if not update.message or not update.message.text:
        return

    try:
        data = json.loads(
            update.message.text.replace("/" + CommandNames.ADD_DICTIONARY.value, "", 1).strip()
        )

        dictionary = Dictionary(**data)
    except ValueError:
        await update.message.reply_text(get.get_string(StringNames.INVALID_DATA, update))
        raise

    dictionary = dictionaries.add_dictionary(dictionary)

    message_text = get.get_string(StringNames.DICTIONARY_ADDED, update).format(
        name=dictionary.name,
        description=dictionary.description,
    )
    await update.message.reply_text(message_text)


def get_dictionaries_list_keyboard() -> InlineKeyboardMarkup:
    dictionaries_list = dictionaries.get_dictionaries()

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=dictionary.name,
                    callback_data=f"{CommandNames.EDIT_DICTIONARY.value};{dictionary.id}",
                )
            ]
            for dictionary in dictionaries_list
        ]
    )


async def list_dictionaries(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    verify_is_admin(update)

    keyboard = get_dictionaries_list_keyboard()

    message_text = get.get_string(StringNames.DICTIONARIES_LIST, update)
    await update.message.reply_text(message_text, reply_markup=keyboard)


async def list_dictionary_callback(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    verify_is_admin(update)

    if not update.callback_query:
        return

    await update.callback_query.edit_message_text(
        text=get.get_string(StringNames.DICTIONARIES_LIST, update),
        reply_markup=get_dictionaries_list_keyboard(),
    )


async def edit_dictionary(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    verify_is_admin(update)

    if not update.callback_query or not update.callback_query.data:
        return

    _, dictionary_id = update.callback_query.data.split(";")
    dictionary = dictionaries.get_dictionary_by_id(int(dictionary_id))

    message_text = dictionary.as_string()
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🗑️",
                        callback_data=f"{CommandNames.REMOVE_DICTIONARY.value};{dictionary.id}",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🔙", callback_data=f"{CommandNames.LIST_DICTIONARIES.value}"
                    )
                ],
            ]
        ),
    )


async def remove_dictionary(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    verify_is_admin(update)

    if not update.callback_query or not update.callback_query.data:
        return

    _, dictionary_id = update.callback_query.data.split(";")
    dictionaries.remove_dictionary(int(dictionary_id))

    message_text = get.get_string(StringNames.DICTIONARY_REMOVED, update)
    await update.callback_query.answer(message_text, show_alert=True)
    await list_dictionary_callback(update=update, _=_)
