from tag import Tag
from error import *
from token_ import *
from math import *

TERM = "TERM"
RULE = "NONT"

# terminals are Tags:
# SEMICOLON = 12
# ASSIGN = 13
# PLUS = 10
# MINUS = 11
# MULTIPLY = 6
# DIVIDE = 7
# DIV = 9
# MOD = 8
# POWER = 5
# F_SIN = 15
# F_COS = 16
# F_TAN = 17
# F_COT = 18
# F_SINH = 19
# F_COSH = 20
# F_LOG = 21
# F_EXP = 22
# F_SQR = 23
# F_SQRT = 24
# LEFT_PRT = 3
# RIGHT_PRT = 4
# END_OF_STREAM = 14
# DOUBLE = 2
# INTEGER = 1
# IDENTIFIER = 0

# non-terminals:
S = 0
PR = 1
ST = 2
AS1 = 3
AS2 = 4
P1 = 5
R1 = 6
P2 = 7
R2 = 8
P3 = 9
R3 = 10
P4 = 11
P5 = 12
F = 13
Num = 14

PARSE_TABLE = [
    # 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
    [
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 0
    [
        1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 1
    [
        2,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 2
    [
        3,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 3
    [
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        4,
        5,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 4
    [
        6,
        6,
        6,
        6,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        6,
        -1,
        -1,
        -1,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
    ],  # 5
    [
        -1,
        -1,
        -1,
        -1,
        9,
        -1,
        -1,
        -1,
        -1,
        -1,
        7,
        8,
        -1,
        9,
        9,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 6
    [
        10,
        10,
        10,
        10,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        10,
        -1,
        -1,
        -1,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ],  # 7
    [
        -1,
        -1,
        -1,
        -1,
        15,
        -1,
        11,
        12,
        13,
        14,
        15,
        15,
        -1,
        -1,
        15,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 8
    [
        16,
        16,
        16,
        16,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        16,
        -1,
        -1,
        -1,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
    ],  # 9
    [
        -1,
        -1,
        -1,
        -1,
        18,
        17,
        18,
        18,
        18,
        18,
        18,
        18,
        -1,
        -1,
        18,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 10
    [
        29,
        29,
        29,
        29,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        29,
        -1,
        -1,
        -1,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
    ],  # 11
    [
        30,
        30,
        30,
        32,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        31,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 12
    [
        34,
        33,
        33,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 13
    [
        -1,
        35,
        36,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
    ],  # 14
]

RULES = [
    [(RULE, PR)],  # 0
    [(RULE, ST)],  # 1
    [(RULE, AS1)],  # 2
    [(TERM, Tag.IDENTIFIER.value), (RULE, AS2)],  # 3
    [(TERM, Tag.ASSIGN.value), (RULE, P1), (RULE, AS2)],  # 4
    [(TERM, Tag.END_OF_STREAM.value)],  # 5
    [(RULE, P2), (RULE, R1)],  # 6
    [(TERM, Tag.PLUS.value), (RULE, P2), (RULE, R1)],  # 7
    [(TERM, Tag.MINUS.value), (RULE, P2), (RULE, R1)],  # 8
    [(TERM, Tag.END_OF_STREAM.value)],  # 9
    [(RULE, P3), (RULE, R2)],  # 10
    [(TERM, Tag.MULTIPLY.value), (RULE, P3), (RULE, R2)],  # 11
    [(TERM, Tag.DIVIDE.value), (RULE, P3), (RULE, R2)],  # 12
    [(TERM, Tag.MOD.value), (RULE, P3), (RULE, R2)],  # 13
    [(TERM, Tag.DIV.value), (RULE, P3), (RULE, R2)],  # 14
    [(TERM, Tag.END_OF_STREAM.value)],  # 15
    [(RULE, P4), (RULE, R3)],  # 16
    [(TERM, Tag.POWER.value), (RULE, P4), (RULE, R3)],  # 17
    [(TERM, Tag.END_OF_STREAM.value)],  # 18
    [
        (TERM, Tag.F_SIN.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 19
    [
        (TERM, Tag.F_COS.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 20
    [
        (TERM, Tag.F_TAN.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 21
    [
        (TERM, Tag.F_COT.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 22
    [
        (TERM, Tag.F_SINH.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 23
    [
        (TERM, Tag.F_COSH.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 24
    [
        (TERM, Tag.F_LOG.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 25
    [
        (TERM, Tag.F_EXP.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 26
    [
        (TERM, Tag.F_SQR.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 27
    [
        (TERM, Tag.F_SQRT.value),
        (TERM, Tag.LEFT_PRT.value),
        (RULE, P4),
        (TERM, Tag.RIGHT_PRT.value),
    ],  # 28
    [(RULE, P5)],  # 29
    [(RULE, F)],  # 30
    [(TERM, Tag.MINUS.value)],  # 31
    [(TERM, Tag.LEFT_PRT.value), (RULE, P1), (TERM, Tag.RIGHT_PRT.value)],  # 32
    [(RULE, Num)],  # 33
    [(TERM, Tag.IDENTIFIER.value)],  # 34
    [(TERM, Tag.INTEGER.value)],  # 35
    [(TERM, Tag.DOUBLE.value)],  # 36
]

STACK = [(TERM, Tag.END_OF_STREAM.value), (RULE, S)]

precedence = {
    Tag.END_OF_STREAM: -1,
    Tag.ASSIGN: 0,
    Tag.F_SQRT: 5,
    Tag.F_SQR: 5,
    Tag.F_EXP: 5,
    Tag.F_LOG: 5,
    Tag.F_COSH: 5,
    Tag.F_COS: 5,
    Tag.F_SINH: 5,
    Tag.F_SIN: 5,
    Tag.F_COT: 5,
    Tag.F_TAN: 5,
    Tag.POWER: 4,
    Tag.MULTIPLY: 3,
    Tag.MOD: 3,
    Tag.DIVIDE: 3,
    Tag.DIV: 3,
    Tag.PLUS: 2,
    Tag.MINUS: 2,
    Tag.LEFT_PRT: 1,
    Tag.RIGHT_PRT: 1,
}


def postfix(tokens):
    result = []
    stack = []
    for token in tokens:
        if token.tag in [Tag.IDENTIFIER, Tag.INTEGER, Tag.DOUBLE]:
            result.append(token)
        elif token.tag is Tag.LEFT_PRT:
            stack.append(token)
        elif token.tag is Tag.RIGHT_PRT:
            top = stack.pop()
            while top.tag is not Tag.LEFT_PRT:
                result.append(top)
                top = stack.pop()
        else:
            while (len(stack) > 0) and (
                precedence[stack[-1].tag] >= precedence[token.tag]
            ):
                result.append(stack.pop())
            stack.append(token)

    while len(stack) > 0:
        result.append(stack.pop())

    return result


def ll1_parser(tokens):
    if len(tokens) <= 3:
        print_error(
            ErrorType.SEMANTIC, cause="Input rejected", handle="Not enough tokens"
        )
        exit(1)
    index = 0
    while len(STACK):
        (ttype, tvalue) = STACK.pop()
        token = tokens[index]
        if ttype == TERM:
            if tvalue == Tag.END_OF_STREAM.value:
                print("pop:", Tag.END_OF_STREAM)
                pass
            elif tvalue == token.tag.value:
                index += 1
                print("pop:", token.tag)
            else:
                print_error(
                    ErrorType.SEMANTIC,
                    cause="Input rejected",
                    handle="Error while creating AST",
                )
                exit(1)
        elif ttype == RULE:
            print("tvalue:", tvalue, "token:", token.tag.value, token.tag)
            rule = PARSE_TABLE[tvalue][token.tag.value]
            print("rule:", rule)
            for r in reversed(RULES[rule]):
                STACK.append(r)
        else:
            print_error(ErrorType.SEMANTIC, cause="Invalid TERM / NONT")
            exit(1)
        print("STACK:", STACK)
    return True


def evaluate(pf):
    table = {}
    for t in pf:
        table[t.id] = t

    flag = True
    for t in table:
        token = table[t]
        if token.value is None:
            if token.tag == Tag.END_OF_STREAM:
                continue
            if flag:
                print("\nEnter value(s) for identifiers:")
                flag = False
            print("id: {} tag: {}".format(token.id, token.tag))
            token.value = input("> ")
            try:
                token.value = float(token.value)
            except:
                print_error(ErrorType.IOError, cause="Entered value is not a number")
                exit(1)

    index = 0
    stack = [pf[index]]
    index += 1
    while len(stack):
        if index < len(pf):
            stack.append(pf[index])
            index += 1

        if stack[-1].tag == Tag.PLUS:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            res = float(a.value) + float(b.value)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.MINUS:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            res = float(b.value) - float(a.value)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.MULTIPLY:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            res = float(b.value) * float(a.value)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.DIVIDE:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            if float(b.value) == 0:
                print_error(ErrorType.SEMANTIC, cause="Zero division")
                exit(1)
            res = float(b.value) // float(a.value)
            res = round(res)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.DIV:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            if float(b.value) == 0:
                print_error(ErrorType.SEMANTIC, cause="Zero division")
                exit(1)
            res = float(b.value) / float(a.value)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.MOD:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            if float(b.value) == 0:
                print_error(ErrorType.SEMANTIC, cause="Zero division")
                exit(1)
            res = float(b.value) % float(a.value)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.POWER:
            stack.pop()
            a = table[stack.pop().id]
            b = table[stack.pop().id]
            res = float(b.value) ** float(a.value)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_SIN:
            stack.pop()
            a = table[stack.pop().id]
            res = sin(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_COS:
            stack.pop()
            a = table[stack.pop().id]
            res = cos(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_TAN:
            stack.pop()
            a = table[stack.pop().id]
            res = tan(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_COT:
            stack.pop()
            a = table[stack.pop().id]
            res = 1 / tan(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_SINH:
            stack.pop()
            a = table[stack.pop().id]
            res = sinh(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_COSH:
            stack.pop()
            a = table[stack.pop().id]
            res = cosh(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_SQRT:
            stack.pop()
            a = table[stack.pop().id]
            res = sqrt(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_SQR:
            stack.pop()
            a = table[stack.pop().id]
            res = pow(float(a.value), 2)
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_LOG:
            stack.pop()
            a = table[stack.pop().id]
            res = log10(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.F_EXP:
            stack.pop()
            a = table[stack.pop().id]
            res = exp(float(a.value))
            table[res] = Token(res, Tag.DOUBLE, res)
            stack.append(table[res])

        elif stack[-1].tag == Tag.ASSIGN:
            stack.pop()
            b = table[stack.pop().id]
            a = table[stack.pop().id]
            a.value = b.value
        elif stack[-1].tag == Tag.END_OF_STREAM:
            stack.pop()
            break

    print("\nIdentifiers:")
    for i in table:
        token = table[i]
        if token.tag == Tag.IDENTIFIER:
            print(token.id, token.tag, token.value)


def parse(tokens):
    print()
    print("Infix:")
    for i in tokens:
        print(i.id, end=" ")
    print()

    print()
    print("Tokens:")
    for i, token in enumerate(tokens):
        print(
            "{}:\t{}, {}, {}, {}".format(
                i, token.id, token.tag.name, token.value, token.readonly
            )
        )
    print()
    _tokens = []
    for token in tokens:
        if token.tag == Tag.LEFT_PRT or token.tag == Tag.RIGHT_PRT:
            _tokens.append(token)
            _tokens.append(token)
        else:
            _tokens.append(token)
    tokens = _tokens
    if ll1_parser(tokens):
        print("\n\033[92m" + "Input Accepted!" + "\x1b[39m")
    print()
    pf = postfix(tokens)
    print("Postfix:")
    for i, token in enumerate(pf):
        print(token.id, end=" ")
    print()
    evaluate(pf)
