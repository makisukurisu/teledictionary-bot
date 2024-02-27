from teledictionary_bot.database.base import DatabaseHandler
from teledictionary_bot.models.dictionary import Dictionary


def _dictionary_from_record(record: tuple) -> Dictionary:
    return Dictionary(
        id=record[0],
        name=record[1],
        description=record[2],
    )


def get_dictionaries() -> list[Dictionary]:
    records: list[Dictionary] = []
    with DatabaseHandler().get_db() as conn:
        cursor = conn.execute("SELECT id, name, description FROM dictionaries")
        for row in cursor:
            records.append(_dictionary_from_record(row))

    return records


def get_dictionary_by_id(dictionary_id: int) -> Dictionary:
    with DatabaseHandler().get_db() as conn:
        cursor = conn.execute(
            "SELECT id, name, description FROM dictionaries WHERE id = ?",
            (dictionary_id,),
        )
        return _dictionary_from_record(cursor.fetchone())


def get_dictionary_by_name(name: str) -> Dictionary:
    with DatabaseHandler().get_db() as conn:
        cursor = conn.execute(
            "SELECT id, name, description FROM dictionaries WHERE name = ?",
            (name,),
        )
        return _dictionary_from_record(cursor.fetchone())


def add_dictionary(name: str, description: str = "") -> Dictionary:
    Dictionary(name=name, description=description)
    with DatabaseHandler().get_db() as conn:
        conn.execute(
            "INSERT INTO dictionaries (name, description) VALUES (?, ?)",
            (name, description),
        )
        conn.commit()

    return get_dictionary_by_name(name)


def remove_dictionary(dictionary_id: int) -> None:
    with DatabaseHandler().get_db() as conn:
        conn.execute(
            "DELETE FROM dictionaries WHERE id = ?",
            (dictionary_id,),
        )
        conn.commit()
