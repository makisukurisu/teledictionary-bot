from teledictionary_bot.database.base import DatabaseHandler
from teledictionary_bot.models.user import User


def _make_user(record: tuple) -> User:
    return User(
        id=record[0],
        user_id=record[1],
        dictionary_id=record[2],
    )


def get_user(user_id: int) -> User:
    with DatabaseHandler().get_db() as conn:
        cursor = conn.execute(
            "SELECT * FROM users WHERE user_id = ?",
            (user_id,),
        )
        return _make_user(cursor.fetchone())


def add_user(user: User) -> User:
    with DatabaseHandler().get_db() as conn:
        conn.execute(
            "INSERT INTO users (user_id, dictionary_id) VALUES (?, ?)",
            (user.user_id, user.dictionary_id),
        )
        conn.commit()

    return get_user(user.user_id)


def add_or_update_user(user: User) -> User:
    with DatabaseHandler().get_db() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO users (user_id, dictionary_id) VALUES (?, ?)",
            (user.user_id, user.dictionary_id),
        )
        conn.commit()


def delete_user(user_id: int) -> None:
    with DatabaseHandler().get_db() as conn:
        conn.execute(
            "DELETE FROM users WHERE user_id = ?",
            (user_id,),
        )
        conn.commit()
