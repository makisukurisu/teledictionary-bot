import enum


class StringNames(enum.Enum):
    DICTIONARY_ADDED = "dictionary_added"
    DICTIONARIES_LIST = "dictionaries_list"
    DICTIONARY_REMOVED = "dictionary_removed"

    SELECT_DICTIONARY = "select_dictionary"
    REMOVE_DATA = "remove_data"

    START_MESSAGE = "start_message"
    HELP_MESSAGE = "help_message"

    INVALID_DATA = "invalid_data"


class CommandNames(enum.Enum):
    START = "start"
    HELP = "help"

    SELECT_DICTIONARY = "select_dictionary"
    REMOVE_DATA = "remove_data"

    # Admin commands
    ADD_DICTIONARY = "add_dictionary"
    LIST_DICTIONARIES = "list_dictionaries"
    EDIT_DICTIONARY = "admin_edit_dictionary"
    REMOVE_DICTIONARY = "admin_remove_dictionary"
