from error import *
from tag import Tag
from token_ import Token
import math

# id: [tag, value, readonly]
symbol_table = {
    "=": [Tag.ASSIGN, "=", True],
    "+": [Tag.PLUS, "+", True],
    "-": [Tag.MINUS, "-", True],
    "*": [Tag.MULTIPLY, "*", True],
    "/": [Tag.DIVIDE, "/", True],
    "^": [Tag.POWER, "^", True],
    ";": [Tag.SEMICOLON, ";", True],
    "div": [Tag.DIV, "div", True],
    "mod": [Tag.MOD, "mod", True],
    "sin": [Tag.F_SIN, "sin", True],
    "cos": [Tag.F_COS, "cos", True],
    "tan": [Tag.F_TAN, "tan", True],
    "cot": [Tag.F_COT, "cot", True],
    "sinh": [Tag.F_SINH, "sinh", True],
    "cosh": [Tag.F_COSH, "cosh", True],
    "log": [Tag.F_LOG, "log", True],
    "exp": [Tag.F_EXP, "exp", True],
    "sqr": [Tag.F_SQR, "sqr", True],
    "sqrt": [Tag.F_SQRT, "sqrt", True],
    "pi": [Tag.DOUBLE, math.pi, True],
}

stream = None
line = 1
column = 0
char = " "


def next_char():
    global stream, line, column, char
    char = stream.read(1).lower()
    column += 1
    if char == "\n":
        column = 0
        line += 1


def get_number():
    num = ""
    while char.isdigit():
        num += char
        next_char()

    # number is decimal?
    if char == ".":
        next_char()
        if char.isdigit():
            num += "."
            while char.isdigit():
                num += char
                next_char()
        else:
            print_error(
                ErrorType.LEXICAL,
                line,
                "Error while reading number",
                "No number after '.'",
            )
            exit(1)

    try:
        int(num)
        return num, False
    except ValueError:
        try:
            float(num)
            return num, True
        except ValueError:
            print_error(ErrorType.LEXICAL, line, "Number has wrong format")
            exit(1)


def is_reserved(lexeme):
    if lexeme in symbol_table:
        return True


def get_token():
    while char.isspace():
        next_char()

    # end of stream?
    if not len(char):
        return Token("$", Tag.END_OF_STREAM, None, True)

    # parentheses?
    elif char == "(":
        next_char()
        return Token("(", Tag.LEFT_PRT, "(", True)
    elif char == ")":
        next_char()
        return Token(")", Tag.RIGHT_PRT, ")", True)

    # single-char operator / comments?
    elif char in symbol_table:
        # div or comment?
        if char == "/":
            next_char()
            if char == "/":  # comment until the end of the line:
                while char != "\n":
                    next_char()
                    if not len(char):
                        return Token("$", Tag.END_OF_STREAM, None, True)
                return None
            elif char == "*":  # comment until */:
                get_next_chr = True
                while True:
                    if get_next_chr:
                        next_char()
                    get_next_chr = True
                    if not len(char):
                        print_error(
                            ErrorType.LEXICAL,
                            line,
                            "Multiline comment was not closed",
                            "*/ was expected",
                        )
                        exit(1)
                    if char == "*":
                        next_char()
                        get_next_chr = False
                        if char == "/":
                            next_char()
                            return None
            else:
                return Token("/", Tag.DIVIDE, "/", True)

        else:
            i = char
            next_char()
            return Token(i, symbol_table[i][0], symbol_table[i][1], symbol_table[i][2])

    # integer or decimal?
    elif char.isdigit():
        num, is_decimal = get_number()
        if is_decimal:
            return Token(num, Tag.DOUBLE, num, False)
        else:
            return Token(num, Tag.INTEGER, num, False)

    # reserved and identifiers?
    else:
        lexeme = ""
        if char.isalnum() or char == "_":
            lexeme = char
        else:
            print_error(ErrorType.LEXICAL, line, "Character not allowed in identifier")
            exit(1)
        while True:
            next_char()
            if not len(char):
                if not lexeme:
                    return Token("$", Tag.END_OF_STREAM, None, True)
                else:
                    return Token(lexeme, Tag.IDENTIFIER, None, False)
            else:
                if char.isalnum() or char == "_":
                    lexeme += char
                    if is_reserved(lexeme):
                        next_char()
                        if (
                            char.isspace()
                            or char in symbol_table
                            or char in ")(/*"
                            or not len(char)
                        ):
                            return Token(
                                lexeme,
                                symbol_table[lexeme][0],
                                symbol_table[lexeme][1],
                                symbol_table[lexeme][2],
                            )
                        else:
                            lexeme += char
                elif (
                    char.isspace() or char in symbol_table or char in ")(/*"
                ):  # new identifier:
                    if is_reserved(lexeme):
                        return Token(
                            lexeme,
                            symbol_table[lexeme][0],
                            symbol_table[lexeme][1],
                            symbol_table[lexeme][2],
                        )
                    else:
                        return Token(lexeme, Tag.IDENTIFIER, None, False)
                else:
                    print_error(ErrorType.LEXICAL, line, "Identifier has wrong format")
                    exit(1)


def lex(input_stream):
    global stream
    stream = input_stream
    tokens = []
    left_prt_count = 0
    right_prt_count = 0
    while True:
        token = get_token()
        if token is not None:
            if token.tag == Tag.END_OF_STREAM:
                tokens.append(token)
                break
            else:
                if token.tag == Tag.LEFT_PRT:
                    left_prt_count += 1
                elif token.tag == Tag.RIGHT_PRT:
                    right_prt_count += 1
                tokens.append(token)
    if left_prt_count != right_prt_count:
        print_error(
            ErrorType.LEXICAL, line, "Left and right parentheses numbers don't match"
        )
        exit(1)
    return tokens
