from typing import Any

from telegram import Update

from teledictionary_bot.enums import StringNames
from teledictionary_bot.settings import settings_instance
from teledictionary_bot.strings import eng, ukr

DEFAULT_LANGUAGE = "en"


# We are using `Any` type here, because we are not sure what type the module will be.
def _fetch_translation(module: Any, string_name: StringNames) -> str:  # noqa: ANN401
    return getattr(
        module,
        string_name.value,
        getattr(eng, string_name.value, "Translation not found :( (This is a bug)"),
    )


def get_string(string_name: StringNames, update: Update) -> str:
    language_code: str = DEFAULT_LANGUAGE

    user = update.effective_user
    if user and user.language_code:
        language_code = user.language_code

    match language_code:
        case "en":
            return _fetch_translation(eng, string_name)
        case "uk":
            return _fetch_translation(ukr, string_name)
        case _:
            return _fetch_translation(eng, string_name)


def get_start_string(update: Update) -> str:
    return get_string(StringNames.START_MESSAGE, update).format(
        bot_name=settings_instance.BOT_NAME,
        bot_username=update.get_bot().username,
    )
