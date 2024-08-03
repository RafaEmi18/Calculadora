import sympy as sp

def integrate_function(expr):
    """
    Integra la expresión dada con respecto a la variable 'x'.
    
    Parameters:
    expr (str): La expresión a integrar.
    
    Returns:
    str: El resultado de la integral en formato LaTeX.
    """
    variable = sp.Symbol('x')
    try:
        expr = expr.replace(" ", "")
        sym_expr = sp.sympify(expr, locals={"x": variable})
        result = sp.integrate(sym_expr, variable)
        return sp.latex(result)
    except (sp.SympifyError, TypeError, SyntaxError) as e:
        return ""