import derivative as df
from rootfinding import newton

def lagrangeMultipliers(f, restricao, x0: float=0, y0: float=0, tol: float=1e-10, maxIter: int=1000):
    """Retorna o ponto de mínimo de  f  sob a restrição  restricao.
    
    Parameters
    ----------
    f : function
        Função a ser derivada em  x.
    restricao : function
        Função que representa a restrição.
    x0, y0 : float, optional
        Ponto inicial para o método de Newton. O padrão é 0.
    tol : float, optional
        Tolerância para o método de Newton. O padrão é 1e-10.
    maxIter : int, optional
        Número máximo de iterações para o método de Newton. O padrão é 1000.
    
    Returns
    -------
    p: float
        p é o valor do ponto de mínimo de  f  sob a restrição  restricao.
    """
    gradF = df.gradienteFunc(f)
    gradR = df.gradienteFunc(restricao)

    # Agora é montar um sistema nao linear com lambda para encontrar os candidatos
    # a minimos locais de f(x, y) sob a restricao r(x, y) = 0
    
    # Ideia0: usar o método de Newton para resolver o sistema
    # Ideia1: aproximar as equações do sistema por polinômios (vira sist. linear)
    
    # Ideia0
    # Montando o sistema : Duas equações da incógnita (x, y) e uma equação da restricao
    eq1 = lambda x, y, l: gradF(x, y)[0] + l * gradR(x, y)[0]
    eq2 = lambda x, y, l: gradF(x, y)[1] + l * gradR(x, y)[1]
    eq3 = lambda x, y: restricao(x, y)

    # Resolvendo o sistema
    x, y = newton(eq1, x0, tol, tol, maxIter), newton(eq2, y0, tol, tol, maxIter)
    if np.isclose(eq3(x, y), 0):
        return x, y
    else:
        return None


# Referências
# Aulas de Cálculo 2 - UFRJ - 2022.2 do Prof. Adriano Cruz
# https://www.statology.org/solve-system-of-equations-in-python/
