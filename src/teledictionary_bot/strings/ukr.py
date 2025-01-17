# ruff: noqa: E501
from teledictionary_bot.enums import CommandNames

select_dictionary = "Обрати словник"
remove_data = "Видалити мої дані"

start_message = (
    """
Вітаємо у {bot_name}!
Використовуйте меню команд, щоб отримати доступні команди

Треба зауважити, що основний спосіб використання цього бота - це використання "інлайн" режиму
Напишіть @{bot_username} та слово, значення якого ви хочете дізнатися

Наприклад: <code>@{bot_username} транскрипція</code>"""
    f"""

Перед тим як ви скористаєтеся кнопками знизу, ви можете захотіти спочатку прочитати /{CommandNames.HELP.value}
"""
)

help_message = f"""
Перед тим, як ви оберете опцію <i>{select_dictionary}</i>, ви можете захотіти знати, що:
Коли ви обираєте словник, бот зберігає ваш user_id, мову вашого клієнту (застосунку) та обраний словник в нашій локальній базі даних.

Ви можете видалити свої дані в будь-який час скориставшись кнопкою <i>{remove_data}</i>.
"""
