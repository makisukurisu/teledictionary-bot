"""
This module contains the operations that the bot can perform.

Operations are certain actions bot can perform in response to an update.
For example, the bot can respond to a message, or to a command.
"""

from . import help, remove_data, search, select_dictionary, start

__all__ = ["help", "remove_data", "search", "select_dictionary", "start"]
