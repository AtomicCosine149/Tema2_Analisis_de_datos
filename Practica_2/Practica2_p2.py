import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

#Parámetros
n = 20
p = 0.10

#Valor concreto de X
x_concreto = 3

#Valores posibles de X
#arange crea una lista que lo determina la cantidad de valores
#Nota: se le pone +1 por que no llega al ultimo valor
x = np.arange(0, n + 1)

#Probabilidades de cada valor de X
#Esta funcion guardara las probabilidades de cada 1
probabilidades = binom.pmf(x, n, p)
#Todo esto se hace para graficar los datos

#probabilidad para el valor concreto
probabilidad_x = binom.cdf(x_concreto, n, p)

print(f"P(x = {x_concreto}) = {probabilidad_x:.4f}")
print(f"Porcentaje = {probabilidad_x * 100:.2f}%")

plt.bar(x, probabilidades)
# Marcar el valor concreto
plt.bar(
   x_concreto,
   probabilidad_x,
   color="red",
   label=f'X = {x_concreto}'
)
# Mostrar el valor de la probabilidad
plt.text(
   x_concreto,
   probabilidad_x,
   f'{probabilidad_x:.4f}',
   ha='center',
   va='bottom',
   fontsize=11
)
plt.xlabel("Número de dispositivos defectuosos (X)")
plt.ylabel("Probabilidad")
plt.title("Distribución Binomial")
plt.xticks(x)
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.show()