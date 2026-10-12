import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

calificaciones=[61,64,65,67,70,72,76,76,77,77,
                78,84,85,87,90,92,96,96,97,97]
intervalos=[60,70,80,90,101]
etiquetas=["60-69","70-79","80-89","90-99"]
rangos = pd.cut(
    calificaciones,
    bins=intervalos,
    labels=etiquetas,
    right=False 
)

frecuencia_absoluta= rangos.value_counts().sort_index()
print(frecuencia_absoluta)

frecuencia_relativa= frecuencia_absoluta/len(calificaciones)
print(frecuencia_relativa)

frecuencia_porcentaje= frecuencia_relativa * 100
print(frecuencia_porcentaje)

tabla = pd.DataFrame({
    "Frecuencia absoluta": frecuencia_absoluta,
    "Frecuencia relativa": frecuencia_relativa,
    "frecuencia porcentaje": frecuencia_porcentaje
})

#Grafica:
plt.bar(
    etiquetas,
    frecuencia_relativa,
    edgecolor="black"
)

plt.xlabel("Rango de calificación")
plt.ylabel("Frecuencia relativa")
plt.title("Frecuencia relativa de las calificaciones")

#muestra los valores sobre la barra
for i, valor in enumerate(frecuencia_relativa):
    plt.text(
        i,
        valor + 0.01,
        f"{valor:.2%}",
        ha="center"#esto se puede poner como left o como right
    )
#el ylim sirve para especificar el limite de una grafica
    plt.ylim(0, max(frecuencia_relativa) + 0.1)
    plt.grid(axis="y", alpha=0.3)
#el grid
    plt.show()