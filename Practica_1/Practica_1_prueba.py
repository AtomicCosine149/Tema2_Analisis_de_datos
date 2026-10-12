import os
import pandas as pd 

os.system("clear")
df=pd.read_csv("urgencias_hospital_1000.csv")
print(df)



Edad = df['Edad']
intervalos = [18,30,45,60,91]
etiquetas = ["18-29", "30-44", "45-59", "60-90"]

rangos = pd.cut(
    Edad,
    bins=intervalos,
    labels=etiquetas,
    right=False
)

#Frecuenacia absouta
frecuencia_absoluta= rangos.value_counts().sort_index()
print(frecuencia_absoluta)

#Frecuencia relativa
frecuencia_relativa= frecuencia_absoluta/len(Edad)
print(frecuencia_relativa)

#Frecuencia porcentaje
frecuencia_porcentaje= frecuencia_relativa * 100
print(frecuencia_porcentaje)

#Media de tendencia central de Edad
print(df["Edad"].mean())
print(df["Edad"].median())
print(df["Edad"].mode())

#Media de tendencia central de Tiempo_Espera_Min
print(df["Tiempo_Espera_Min"].mean())
print(df["Tiempo_Espera_Min"].median())
print(df["Tiempo_Espera_Min"].mode())

#Media de tendencia central de Costo_Atencion_USD
print(df["Costo_Atencion_USD"].mean())
print(df["Costo_Atencion_USD"].median())
print(df["Costo_Atencion_USD"].mode())

#Medias de la posición
print(df["Edad"].min())
print(df["Edad"].max())
