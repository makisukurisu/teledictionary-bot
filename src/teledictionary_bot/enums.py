import enum


class StringNames(enum.Enum):
    DICTIONARY_ADDED = "dictionary_added"
    DICTIONARIES_LIST = "dictionaries_list"
    DICTIONARY_REMOVED = "dictionary_removed"

    SELECT_DICTIONARY_BUTTON = "select_dictionary"
    REMOVE_DATA_BUTTON = "remove_data"

    SELECT_DICTIONARY_TEXT = "select_dictionary_text"
    CHOOSE_DICTIONARY_TEXT = "choose_dictionary_text"
    REMOVE_DATA_TEXT = "remove_data_text"

    START_MESSAGE = "start_message"
    HELP_MESSAGE = "help_message"

    INVALID_DATA = "invalid_data"


class CommandNames(enum.Enum):
    START = "start"
    HELP = "help"

    SELECT_DICTIONARY = "select_dictionary"
    CHOOSE_DICTIONARY = "choose_dictionary"
    REMOVE_DATA = "remove_data"

    # Admin commands
    ADD_DICTIONARY = "add_dictionary"
    LIST_DICTIONARIES = "list_dictionaries"
    EDIT_DICTIONARY = "admin_edit_dictionary"
    REMOVE_DICTIONARY = "admin_remove_dictionary"

    @classmethod
    def choose_dictionary(cls: "CommandNames", dictionary_id: int) -> str:
        return f"{cls.CHOOSE_DICTIONARY.value};{dictionary_id}"


class ProviderNames(enum.Enum):
    OXFORD = "oxford_dictionaries"
    URBAN = "urban_dictionaries"
    GEMINI = "google_gemini"
