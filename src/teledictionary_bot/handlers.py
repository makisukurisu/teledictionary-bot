"""
This file contains all the handlers that the bot uses to respond to updates.
"""

from telegram.ext import CallbackQueryHandler, CommandHandler

from teledictionary_bot import operations
from teledictionary_bot.enums import CommandNames

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
