"""
This file contains the "heart" of the bot.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from telegram.ext import ApplicationBuilder

from teledictionary_bot import handlers

from .settings import settings_instance

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
        .concurrent_updates(True)  # Enable the concurrent updates processing  # noqa: FBT003
        .build()
    )

    app.add_handler(handlers.start_handler)

    app.run_polling()


if __name__ == "__main__":
    build()
