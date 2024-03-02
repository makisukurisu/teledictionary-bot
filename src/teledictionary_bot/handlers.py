"""
This file contains all the handlers that the bot uses to respond to updates.
"""

import re

from telegram.ext import CallbackQueryHandler, CommandHandler, InlineQueryHandler

from teledictionary_bot import operations
from teledictionary_bot.enums import CommandNames
from teledictionary_bot.operations import admin as admin_operations

# admin handlers

add_dictionary_handler = CommandHandler(
    command=CommandNames.ADD_DICTIONARY.value,
    callback=admin_operations.dictionaries.add_dictionary,
)
list_dictionaries_handler = CommandHandler(
    command=CommandNames.LIST_DICTIONARIES.value,
    callback=admin_operations.dictionaries.list_dictionaries,
)
list_dictionaries_callback_handler = CallbackQueryHandler(
    pattern=CommandNames.LIST_DICTIONARIES.value,
    callback=admin_operations.dictionaries.list_dictionary_callback,
)
edit_dictionary_handler = CallbackQueryHandler(
    pattern=re.compile(r"^" + CommandNames.EDIT_DICTIONARY.value + r";(\d+)$"),
    callback=admin_operations.dictionaries.edit_dictionary,
)
remove_dictionary_handler = CallbackQueryHandler(
    pattern=re.compile(r"^" + CommandNames.REMOVE_DICTIONARY.value + r";(\d+)$"),
    callback=admin_operations.dictionaries.remove_dictionary,
)

# user handlers

start_handler = CommandHandler(
    command=CommandNames.START.value,
    callback=operations.start.start,
)

help_handler = CommandHandler(
    command=CommandNames.HELP.value,
    callback=operations.help.help_method,
)

select_dictionary_handler = CallbackQueryHandler(
    pattern=CommandNames.SELECT_DICTIONARY.value,
    callback=operations.select_dictionary.select_dictionary,
)
choose_dictionary_handler = CallbackQueryHandler(
    pattern=re.compile(r"^" + CommandNames.CHOOSE_DICTIONARY.value + r";(\d+)$"),
    callback=operations.select_dictionary.choose_dictionary,
)
search_handler = InlineQueryHandler(callback=operations.search.search, pattern=re.compile(r".+"))
