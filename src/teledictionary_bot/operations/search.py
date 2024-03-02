import hashlib

from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    Update,
)
from telegram.ext import ContextTypes

from teledictionary_bot.enums import StringNames
from teledictionary_bot.strings import get


async def search(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    # WIP, this is just a placeholder
    if not update.inline_query:
        return

    # Hash the query to use it as part of the ID of the result
    hashed_query = hashlib.sha256(
        string=update.inline_query.query.encode("utf-8"),
    ).hexdigest()

    await update.inline_query.answer(
        results=[
            InlineQueryResultArticle(
                id=hashed_query,
                title="Test",
                input_message_content=InputTextMessageContent(
                    get.get_string(StringNames.HELP_MESSAGE, update)
                ),
            )
        ]
    )
