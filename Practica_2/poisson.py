import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
#Es de las distribuciones de poisson:
#Parámetros
lambda_ = 4

#Valor concreto de X
x_concreto = 2

#Valores posibles de X
#arange crea una lista que lo determina la cantidad de valores
#Nota: se le pone +1 por que no llega al ultimo valor
x = np.arange(0, 16)

#Probabilidades de cada valor de X
#Esta funcion guardara las probabilidades de cada 1
probabilidades = poisson.pmf(x, lambda_)
#Todo esto se hace para graficar los datos

#probabilidad para el valor concreto
probabilidad_x = poisson.cdf(x_concreto, lambda_)

print(f"P(x = {x_concreto}) = {probabilidad_x:.4f}")
print(f"Porcentaje = {probabilidad_x * 100:.2f}%")

plt.bar(x,probabilidades)
plt.bar(
    x_concreto,
    probabilidad_x,
    color="red",
    label=f'X = {x_concreto}'
)
plt.text(
    x_concreto,
    probabilidad_x,
    f'X{probabilidad_x:.4f}',
    ha='center',
    va='bottom',
    fontsize=11
)
plt.show()