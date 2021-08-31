import lexer
import parser_
from error import *

import sys


def main():
    in_stream = sys.stdin
    if len(sys.argv) > 1:
        try:
            in_stream = open(sys.argv[1], "r")
        except IOError:
            print_error(ErrorType.IOError)
            exit(1)

    tokens = lexer.lex(in_stream)
    parser_.parse(tokens)


if __name__ == "__main__":
    main()
