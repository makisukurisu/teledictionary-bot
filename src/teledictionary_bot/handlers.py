"""
This file contains all the handlers that the bot uses to respond to updates.
"""

from telegram.ext import CommandHandler

from teledictionary_bot import operations

start_handler = CommandHandler(
    command="start",
    callback=operations.start.start,
)
