"""
This file contains the "heart" of the bot.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, Defaults

from teledictionary_bot import handlers
from teledictionary_bot.settings import settings_instance

LOGS_FOLDER = settings_instance.LOGS_FOLDER

os.makedirs(
    LOGS_FOLDER,
    exist_ok=True,
)

logger = logging.basicConfig(
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(
            f"{LOGS_FOLDER}/bot.log",
            maxBytes=10_000_000,  # 10 MB
            backupCount=5,
            encoding="UTF-8",
        ),
    ],
    level=settings_instance.LOG_LEVEL,
)


def build() -> None:
    app = (
        ApplicationBuilder()
        .token(
            settings_instance.BOT_TOKEN,
        )
        .defaults(Defaults(parse_mode=ParseMode.HTML))
        .concurrent_updates(True)  # Enable the concurrent updates processing  # noqa: FBT003
        .build()
    )

    app.add_handler(handlers.add_dictionary_handler)
    app.add_handler(handlers.list_dictionaries_handler)
    app.add_handler(handlers.remove_dictionary_handler)
    app.add_handler(handlers.list_dictionaries_callback_handler)
    app.add_handler(handlers.edit_dictionary_handler)

    app.add_handler(handlers.start_handler)
    app.add_handler(handlers.help_handler)
    app.add_handler(handlers.select_dictionary_handler)
    app.add_handler(handlers.choose_dictionary_handler)
    app.add_handler(handlers.search_handler)

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    build()
