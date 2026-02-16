from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple avec deux opérandes et un opérateur.
    Cette fonction recupère l'expression sous forme de chaîne de caractères, extrait 
    les opérandes et l'opérateur (+, -, *, /), puis effectue le calcul correspondant.
    
    Args:
        expr (str): Expression arithmétique à évaluer (ex: "5 + 3", "10*2")
    
    Returns:
        float: Résultat du calcul

    Raises:
        ValueError: Si l'expression est vide, invalide, contient plus d'un opérateur,
                        ou si les opérandes ne sont pas des nombres valides
    
    Examples:
    >>> calculate("5 + 3")      retourne 8.0
    >>> calculate("10 * 2")     retourne 20.0
    >>> calculate("15/3")       retourne 5.0
    """
    
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur unique dans la liste de OPS
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Extraction des nombres à gauche de l'opérateur et à sa droite
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application calculatrice Flask. Elle gère l'affichage de
    la page d'accueil ainsi que le traitement des expressions arithmétiques soumises
    par l'utilisateur via un formulaire HTML.

    GET : affiche le formulaire de la calculatrice.
    POST : récupère l'expression saisie, l'évalue via calculate() et renvoie
    le résultat ou un message d'erreur.

    Returns:
        str (HTML): rendue avec le résultat du calcul.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)