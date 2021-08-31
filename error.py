from enum import Enum


class ErrorType(Enum):
    LEXICAL = 0
    SEMANTIC = 1
    IOError = 2


def print_error(e_type, line=None, cause=None, handle=None):
    print(
        "\033[91m"
        + "\n{} error occurred: {}{}{}".format(
            e_type.name,
            "" if line is None else "line({})".format(line),
            "" if cause is None else "\n\t{}.".format(cause),
            "" if handle is None else "\n\t{}.\n\t".format(handle),
        )
    )
