import enum


class StringNames(enum.Enum):
    SELECT_DICTIONARY = "select_dictionary"
    REMOVE_DATA = "remove_data"

    START_MESSAGE = "start_message"
    HELP_MESSAGE = "help_message"


class CommandNames(enum.Enum):
    START = "start"
    HELP = "help"

    SELECT_DICTIONARY = "select_dictionary"
    REMOVE_DATA = "remove_data"
