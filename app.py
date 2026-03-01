from flask import Flask, request, render_template, session
from operators import add, subtract, multiply, divide

app = Flask(__name__)
app.secret_key = "calculator-dev-secret"

OPS = {
    '+': add,
    '-': subtract,
    '**': lambda a, b: a ** b,
    '*': multiply,
    '/': divide,
}


def _parse_signed_number(token: str) -> float:
    """Parse numbers with repeated unary +/- signs, e.g. --2, ---2, +--2."""
    if not token:
        raise ValueError("operands must be numbers")

    sign = 1
    i = 0
    while i < len(token) and token[i] in "+-":
        if token[i] == "-":
            sign *= -1
        i += 1

    core = token[i:]
    if not core:
        raise ValueError("operands must be numbers")

    try:
        return sign * float(core)
    except ValueError:
        raise ValueError("operands must be numbers")


def _find_binary_operator(s: str):
    op_pos = -1
    op_len = 0
    op_char = None
    i = 0

    # Find one binary operator and allow unary + / - signs for operands.
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

    return op_pos, op_len, op_char


def _evaluate(expr: str):
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")
    op_pos, op_len, op_char = _find_binary_operator(s)

    if op_pos == -1:
        return _parse_signed_number(s), None, None

    if op_pos <= 0 or op_pos >= len(s) - op_len:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos + op_len:]

    a = _parse_signed_number(left)
    b = _parse_signed_number(right)
    return OPS[op_char](a, b), op_char, b


def calculate(expr: str):
    """Evaluate a simple arithmetic expression with two operands and one operator."""
    result, _, _ = _evaluate(expr)
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route: show form and evaluate submitted expression."""
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            compact = expression.replace(" ", "")
            is_number_only = _find_binary_operator(compact)[0] == -1

            if (
                is_number_only
                and "last_operator" in session
                and "last_operand" in session
            ):
                current = _parse_signed_number(compact)
                result = OPS[session["last_operator"]](current, session["last_operand"])
            else:
                result, op_char, right_operand = _evaluate(expression)
                if op_char is not None:
                    session["last_operator"] = op_char
                    session["last_operand"] = right_operand
                else:
                    session.pop("last_operator", None)
                    session.pop("last_operand", None)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
