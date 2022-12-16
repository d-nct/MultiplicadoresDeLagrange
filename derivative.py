def derivada(f, x: float, y: float, parcial: str, h: float=1e-10):
    """Retorna a derivada numérica central de  f  no ponto  (x,y), com aproximação de  h.
    
    Parameters
    ----------
    f : function
        Função a ser derivada em  x.
    x, y : float
        Ponto em que  f  será derivada.
    parcial : str
        Variável em que a derivada será calculada. Por exemplo, "x" ou "y".
    h : float, optional
        Equivalente ao dh da derivada. Não utilize h <= 1e-16. O padrão é 1e-10.
    
    Returns
    -------
    p: float
        p é o valor da derivada numérica central f'(x).
    """
    if parcial != "x" and parcial != "y":
        raise ValueError("Parâmetro 'parcial' deve ser 'x' ou 'y'.")

    switch={
        'x': (f(x + h, y) - f(x - h, y)) / (2 * h),
        'y': (f(x, y + h) - f(x, y - h)) / (2 * h),
        }

    return switch.get(parcial, "Parâmetro 'parcial' deve ser 'x' ou 'y'.")

def derivadaFunc(f, parcial: str, h: float=1e-10):
    """Retorna a função derivada de  f  em  parcial, com aproximação de  h.
    
    Parameters
    ----------
    f : function
        Função a ser derivada em  x.
    parcial : str
        Variável em que a derivada será calculada. Por exemplo, "x" ou "y".
    h : float, optional
        Equivalente ao dh da derivada. Não utilize h <= 1e-16. O padrão é 1e-10.
    
    Returns
    -------
    p: float
        p é o valor da derivada numérica central f'(x).
    """
    if (parcial != "x") and (parcial != "y"):
        raise ValueError("Parâmetro 'parcial' deve ser 'x' ou 'y'.")

    switch={
        'x': lambda x,y: (f(x + h, y) - f(x - h, y)) / (2 * h),
        'y': lambda x,y: (f(x, y + h) - f(x, y - h)) / (2 * h),
        }

    return switch.get(parcial, "Parâmetro 'parcial' deve ser 'x' ou 'y'.")

def gradiente(f, x: float, y: float, h: float=1e-10):
    """Retorna o gradiente numérico central de  f  no ponto  (x,y), com aproximação de  h.
    
    Parameters
    ----------
    f : function
        Função a ser derivada em  x.
    x, y : float
        Ponto em que  f  será derivada.
    h : float, optional
        Equivalente ao dh da derivada. Não utilize h <= 1e-16. O padrão é 1e-10.
    
    Returns
    -------
    p: float
        p é o valor do gradiente numérico central f'(x).
    """
    return (derivada(f, x, y, "x", h), derivada(f, x, y, "y", h))

def gradienteFunc(f, h: float=1e-10):
    """Retorna a função gradiente de  f  em  parcial, com aproximação de  h.
    
    Parameters
    ----------
    f : function
        Função a ser derivada em  x.
    h : float, optional
        Equivalente ao dh da derivada. Não utilize h <= 1e-16. O padrão é 1e-10.
    
    Returns
    -------
    p: float
        p é o valor da derivada numérica central f'(x).
    """
    g = lambda x, y: (derivadaFunc(f, "x", h)(x, y), derivadaFunc(f, "y", h)(x, y))
    return g
