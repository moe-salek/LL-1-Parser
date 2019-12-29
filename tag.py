from enum import Enum


class Tag(Enum):
    SEMICOLON = 12
    ASSIGN = 13
    PLUS = 10
    MINUS = 11
    MULTIPLY = 6
    DIVIDE = 7
    DIV = 9
    MOD = 8
    POWER = 5
    F_SIN = 15
    F_COS = 16
    F_TAN = 17
    F_COT = 18
    F_SINH = 19
    F_COSH = 20
    F_LOG = 21
    F_EXP = 22
    F_SQR = 23
    F_SQRT = 24
    LEFT_PRT = 3
    RIGHT_PRT = 4
    END_OF_STREAM = 14
    DOUBLE = 2
    INTEGER = 1
    IDENTIFIER = 0
