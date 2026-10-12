import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Conjunto de datos
calificaciones = [6,7,7,7,7,8,8,8,8,8,
                  9,9,9,9,9,10,10,10,10,10]
#Convertir a series de pandas
datos=pd.Series(calificaciones)
#Estadisticas descriptivos
media=datos.mean()
mediana=datos.median()
moda = datos.mode()[0]
#Asemetria
asimetria=datos.skew
#Curtosis
curtosis=datos.kurt()

print("====== ANALISIS ESTADISTICO ======")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Asimetria: {asimetria:.4f}")
print(f"Curtosis: {curtosis:.4f}")


#Interpretacion
if asimetria > 0:
    print("La distribución presenta asimetria positiva")
elif asimetria < 0:
    print("La distribución presenta asimetria negativa")
else:
    print("La distribución es aproximadamente simetrica")

if curtosis > 0:
    print("La distribución es leptocúrtica")
elif curtosis < 0:
    print("La distribución es platicúrtica")
else:
    print("La distribución es mesocúrtica")

#Histograma + curva de densidad
sns.histplot(
    datos,
    kde=True,
    bins=5
)

plt.axvline(
    media,
    linewidth=2,
    linestyle="--",
    color="red",
    label=f"Media: {media:.2f}"
)
plt.axvline(
    mediana,
    linewidth=2,
    linestyle="--",
    color="yellow",
    label=f"Mediana: {mediana:.2f}"
)


plt.title("Distribución de las calificaciones")
plt.xlabel("calificación")
plt.ylabel("Frecuencia")
plt.legend()