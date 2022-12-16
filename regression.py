def reg_poly(xs, ys, grau):
    """Retorna a função da regressão polinomial dos pontos (xs,ys).
    """
    vander = np.vander(xs, grau+1) 
    coefs, *_ = np.linalg.lstsq(vander, ys, rcond=None)
    p = np.poly1d(coefs) 
    return p 

def reconstruct(coefs, base):
    """Retorna a função correspondente aos coeficientes e à base escolhida de uma regressão.
    """
    def m(x):   
        ans = 0
        for beta, coef in zip(base, coefs):
            ans += coef * beta(x)
        return ans         
        
    return m
