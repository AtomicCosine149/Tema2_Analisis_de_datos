import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Conjunto de datos
calificaciones = [
    6, 7, 7, 7, 8, 8, 8, 8, 8,
    9, 9, 9, 9, 9, 9, 10, 10, 10
]

# Convertir a Series de Pandas
datos = pd.Series(calificaciones)

# 2. Estadísticas descriptivas
media = datos.mean()
mediana = datos.median()
moda = datos.mode()[0]  # Cálculo de la moda

# Asimetría
asimetria = datos.skew()

# 3. Curtosis
curtosis = datos.kurt()

print("====== ANALISIS ESTADISTICO ======")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Asimetria: {asimetria:.4f}")
print(f"Curtosis: {curtosis:.4f}")

# 3. Interpretación
# ---------------------------------------------
if asimetria > 0:
    print("La distribución presenta asimetría positiva.")
elif asimetria < 0:
    print("La distribución presenta asimetría negativa.")
else:
    print("La distribución es aproximadamente simétrica.")
    
if curtosis > 0:
    print("La distribución es leptocúrtica.")
elif curtosis < 0:
    print("La distribución es platicúrtica.")
else:
    print("La distribución es mesocúrtica.")
    
# 4. HISTOGRAMA + CURVA DE DENSIDAD
sns.histplot(
    datos,
    kde=True,
    bins=5
)

plt.axvline(
    media,
    linestyle="--",
    color="green",
    linewidth=2.5,  # <--- Grosor de la línea de la media
    label=f"media={media:.2f}"
)

plt.axvline(
    mediana,
    linestyle=":",
    color="orange",
    linewidth=2.5,  # <--- Grosor de la línea de la mediana
    label=f"mediana={mediana:.2f}"
)

plt.axvline(
    moda,
    linestyle="-.",
    color="red",
    linewidth=2.5, 
    label=f"moda={moda:.2f}"
)

plt.title("Distribución de las calificaciones")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()