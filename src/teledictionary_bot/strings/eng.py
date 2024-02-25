# ruff: noqa: E501
from teledictionary_bot.enums import CommandNames

select_dictionary = "Select a dictionary"
remove_data = "Remove my data"

start_message = (
    """
Welcome to {bot_name}!
Use commands menu to get available commands

Primary way to use this bot, however, is to use inline mode
Simply write @{bot_username} followed by a word to get its meaning

For example: <code>@{bot_username} locomotive</code>"""
    f"""

Before you use any buttons bellow - consider reading /{CommandNames.HELP.value} first
"""
)

help_message = f"""
Before you proceed with <i>{select_dictionary}</i> option, you may want to know that:
When you select a dictionary, bot will store your user_id, (client) language and selected dictionary in our local database.

You can remove your data from our database at any time by using <i>{remove_data}</i> option.
"""
