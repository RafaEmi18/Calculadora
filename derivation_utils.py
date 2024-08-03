import sympy as sp

def derive_function(expr):
    """
    Deriva la expresión dada con respecto a la variable 'x'.
    
    Parametros:
    expr (str): La expresión a derivar.
    
    Regresa:
    str: El resultado de la derivada en formato LaTeX.
    """
    variable = sp.Symbol('x')
    try:
        expr = expr.replace(" ", "")
        sym_expr = sp.sympify(expr, locals={"x": variable})
        result = sp.diff(sym_expr, variable)
        return sp.latex(result)
    except (sp.SympifyError, TypeError, SyntaxError) as e:
        return ""