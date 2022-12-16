# Nesse arquivo, estão contidos testes para os Multiplicadores de Lagrange

from lagrangeMultipliers import lagrangeMultipliers
import numpy as np

# Definindo a função f(x, y) = x^2 + y^2
f = lambda x, y: x**2 + y**2
f = np.vectorize(f)

# Definindo a restrição r(x, y) = x^2 + y^2 - 1
restricao = lambda x, y: x**2 + y**2 - 1

# Definindo o intervalo de x e y
xs = np.linspace(-1.5, 1.5, 100)

# Definindo o intervalo de y
ys = np.linspace(-1.5, 1.5, 100)

# Definindo a grade de pontos
X, Y = np.meshgrid(xs, ys)

# Definindo o ponto de mínimo de f(x, y) sob a restrição r(x, y) = 0
pontoMinimo = lagrangeMultipliers(f, restricao)

# Plotando a função f(x, y)
plt.contour(X, Y, Z, 20)
plt.colorbar()

# Plotando a função r(x, y)
plt.contour(X, Y, R, 20)
plt.colorbar()

# Plotando o ponto de mínimo de f(x, y) sob a restrição r(x, y) = 0
plt.plot(pontoMinimo[0], pontoMinimo[1], 'ro')

plt.show()


# Referências
# https://en.wikipedia.org/wiki/Lagrange_multiplier
# https://en.wikipedia.org/wiki/Newton%27s_method
# https://en.wikipedia.org/wiki/Polynomial
# https://en.wikipedia.org/wiki/Linear_system
# https://en.wikipedia.org/wiki/Root-finding_algorithm
# https://en.wikipedia.org/wiki/Gradient
