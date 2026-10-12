import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
#-----------------------------------------------------
#Respueta de la 1:
#-----------------------------------------------------
mu = 240    #Media
sigma = 35  #Desviacion estandar
x = 200     #Tiempo de respuesta que requerimos

z = (x - mu) / sigma
print("Valor Z:", round(z,4))

probabilidad = norm.cdf(x, loc=mu, scale=sigma)

print("Probabilidad P(X <200):", round(probabilidad, 6))
print("Porcentaje:", round(probabilidad * 100, 2), "%")

valores_x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

#FUncion de densidad normal
valores_y = norm.pdf(valores_x, mu, sigma)

#Dibujar la campana de Gauss
plt.plot(
    valores_x,
    valores_y,
    linewidth=2, color="black",
    label="Distribucion normal"
)

x_sombreado = valores_x[valores_x <= x]
y_sombreado = norm.pdf(x_sombreado, mu, sigma)

plt.fill_between(
    x_sombreado,
    y_sombreado,
    alpha=1, color="red",
    label=f"P(X <200) = {probabilidad*100:.2f}%"
)
#plt.show()

#altura de la curva en x = 200
altura_x = norm.pdf(x,mu,sigma)

#altura de la curva en la media x = 100
altura_media = norm.pdf(mu, mu, sigma)

#vlines traza lineas establecidas
plt.vlines(
    x,
    0,
    altura_x,
    linestyles="--",
    linewidth=2, color="black",
    label="X = 200 ms"
)
#plt.show()

plt.vlines(
    mu,
    0,
    altura_media,
    linestyles="--",
    linewidth=2, color="black",
    label="X = 240 ms"
)
#plt.show()

plt.title(
    "Distribución normal de los tiempos de respuesta",
    fontsize=14
)
plt.xlabel("Tiempo de respuesta (milisegundos)")
plt.ylabel("Densidad de probabilidad")

#plt.legend()
#plt.grid(alpha=0.3)

#plt.show()

#-----------------------------------------------------
#Respuesta 2
#-----------------------------------------------------

x2 = 300

z2 = (x2 + mu) / sigma
print("Valor Z:", round(z2,4))

probabilidad2 = norm.cdf(x2, loc=mu, scale=sigma)

print("Probabilidad P(X <300):", round(probabilidad2, 6))
print("Porcentaje:", round(probabilidad2 * 100, 2), "%")

x_sombreado2 = valores_x[valores_x >= x2]
y_sombreado2 = norm.pdf(x_sombreado2, mu, sigma)

plt.fill_between(
    x_sombreado2,
    y_sombreado2,
    alpha=1, color="green",
    label=f"P(X <300) = {probabilidad2*100:.2f}%"
)

#altura de la curva en x = 300
altura_x2 = norm.pdf(x2,mu,sigma)

plt.vlines(
    x2,
    0,
    altura_x2,
    linestyles="--",
    linewidth=2, color="black",
    label="X = 300 ms"
)

plt.legend()
plt.grid(alpha=0.3)

plt.show()
