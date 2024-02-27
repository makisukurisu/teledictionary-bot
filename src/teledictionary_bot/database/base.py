import sqlite3
from typing import TYPE_CHECKING

from teledictionary_bot.settings import settings_instance

if TYPE_CHECKING:
    from teledictionary_bot.settings import Settings


class DatabaseHandler:
    def __init__(self: "DatabaseHandler", settings: "Settings | None" = settings_instance) -> None:
        self._db_path = settings.DATABASE_PATH

    def get_db(self) -> sqlite3.Connection:
        return sqlite3.connect(self._db_path)

    def create_tables(self) -> None:
        with self.get_db() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS dictionaries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT DEFAULT "",
                    UNIQUE(name)
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    dictionary_id INTEGER NOT NULL,
                    FOREIGN KEY (dictionary_id) REFERENCES dictionaries(id)
                )
                """
            )


DatabaseHandler().create_tables()
