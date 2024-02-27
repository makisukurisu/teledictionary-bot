import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    BOT_TOKEN: str = pydantic.Field(description="A bot token that you've got from BotFather")
    BOT_NAME: str = pydantic.Field(
        default="Tele-Dictionary",
        description="The name of the bot",
    )
    BOT_ADMINISTRATORS: list[str] = pydantic.Field(
        default=[],
        description="The list of user IDs that are allowed to use the bot",
    )

    DATABASE_PATH: str = pydantic.Field(
        default="data/teledictionary_bot.db",
        description="The path to the database",
    )

    LOG_LEVEL: str = pydantic.Field(
        default="WARNING",
        description="The log level for the bot",
    )
    LOGS_FOLDER: str = pydantic.Field(
        default="logs",
        description="The folder where the logs will be stored",
    )


settings_instance = Settings(_env_file=".env", _env_file_encoding="UTF-8")
