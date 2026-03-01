from operators import add, subtract, multiply, divide

OPS = {
    '+': add,
    '-': subtract,
    '**': lambda a, b: a ** b,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Evaluate a simple arithmetic expression with one binary operator."""
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_len = 0
    op_char = None
    i = 0

    while i < len(s):
        if s[i] == '*' and i + 1 < len(s) and s[i + 1] == '*':
            if i == 0 or s[i - 1] in "+-*/":
                raise ValueError("invalid expression format")
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_len = 2
            op_char = '**'
            i += 2
            continue

        if s[i] in '+-*/':
            is_unary_sign = s[i] in '+-' and (i == 0 or s[i - 1] in '+-*/')
            if not is_unary_sign:
                if op_pos != -1:
                    raise ValueError("only one operator is allowed")
                op_pos = i
                op_len = 1
                op_char = s[i]
        i += 1

    if op_pos <= 0 or op_pos >= len(s) - op_len:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos + op_len:]

    try:
        a = float(left)
        b = float(right)
    except ValueError as exc:
        raise ValueError("operands must be numbers") from exc

    return OPS[op_char](a, b)
