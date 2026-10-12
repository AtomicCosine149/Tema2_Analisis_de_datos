import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats iqr 
# NOMBRE DE LA PRACTICA: ESTADISTICA DESCRIPTIVA
#TEMA: ESTADISTICA Y CIENCIA DE DATOS
#SUBTEMA ESTADISTICA DESCRIPTIVA Y VISUALIZACION DE DATOS 2.2

os.system("cls")

ruta = r"C:\Users\gp_pe\Downloads\CIENCIA DE DATOS\tema 2 temporada 2\urgencias_hospital_1000.csv"
df = pd.read_csv(ruta)

# head() muestra los primeros 5 registros para revisar que se leyó bien.
print("PRIMEROS REGISTROS")
print(df.head())

# shape devuelve (filas, columnas): aquí son 1000 pacientes y 8 variables.
print("\nTamaño de la tabla (filas, columnas):", df.shape)

# ============================================================
# 4.1 ANÁLISIS DE VARIABLES CUALITATIVAS (Nivel_Triage)
# ============================================================

# ------------------------------------------------------------
# Paso 3. Tabla de frecuencia absoluta
# ------------------------------------------------------------
# value_counts() cuenta cuántos pacientes hay en cada nivel de triage.
# sort_index() los ordena del nivel 1 al 4 (así la acumulada tiene sentido).
frec_abs = df["Nivel_Triage"].value_counts().sort_index()
print("\n4.1 FRECUENCIA ABSOLUTA - Nivel_Triage")
print(frec_abs)

# ------------------------------------------------------------
# Paso 4. Tabla de frecuencia relativa (%)
# ------------------------------------------------------------
# Se divide cada frecuencia entre el total de pacientes y se multiplica por 100.
frec_rel = (frec_abs / len(df) * 100).round(2)
print("\nFRECUENCIA RELATIVA (%) - Nivel_Triage")
print(frec_rel)

# ------------------------------------------------------------
# Paso 5. Frecuencia acumulada
# ------------------------------------------------------------
# cumsum() va sumando las frecuencias de arriba hacia abajo.
# Aplica porque el nivel de triage tiene un orden (1 = más grave, 4 = menor).
frec_acum = frec_abs.cumsum()
frec_rel_acum = frec_rel.cumsum().round(2)

# Se juntan las cuatro columnas en una sola tabla resumen.
tabla_triage = pd.DataFrame({
    "Frecuencia absoluta": frec_abs,
    "Frecuencia relativa (%)": frec_rel,
    "Frecuencia acumulada": frec_acum,
    "Frecuencia acumulada (%)": frec_rel_acum,
})
print("\nTABLA COMPLETA DE FRECUENCIAS - Nivel_Triage")
print(tabla_triage)






# ------------------------------------------------------------
# Paso 6. Diagrama de pastel
# ------------------------------------------------------------
# Muestra qué porción del total representa cada nivel de triage.
# autopct escribe el porcentaje dentro de cada rebanada.
plt.figure(figsize=(7, 7))
plt.pie(frec_abs, labels=frec_abs.index, autopct="%1.1f%%", startangle=90)
plt.title("Distribución de pacientes por Nivel de Triage")
plt.show()






# ------------------------------------------------------------
# Paso 7. Gráfica de barras
# ------------------------------------------------------------
# Compara la cantidad de pacientes de cada nivel de triage.
plt.figure(figsize=(8, 5))
plt.bar(frec_abs.index, frec_abs.values, edgecolor="black")
plt.title("Pacientes por Nivel de Triage")
plt.xlabel("Nivel de triage")
plt.ylabel("Número de pacientes")
plt.show()





# ------------------------------------------------------------
# Paso 8. Interpretación de la distribución
# ------------------------------------------------------------
# Se obtiene automáticamente la categoría más y menos frecuente.
mas_frecuente = frec_abs.idxmax()
menos_frecuente = frec_abs.idxmin()
print("\nINTERPRETACIÓN")
print(f"- La categoría más frecuente es '{mas_frecuente}' con "
      f"{frec_abs.max()} pacientes ({frec_rel.max()} %).")
print(f"- La categoría menos frecuente es '{menos_frecuente}' con "
      f"{frec_abs.min()} pacientes ({frec_rel.min()} %).")
print(f"- Los niveles 1, 2 y 3 juntos suman {frec_rel_acum.iloc[2]} % de los "
      f"pacientes; solo {frec_rel.iloc[3]} % son casos menores.")


# ============================================================
# 4.2 ANÁLISIS DE VARIABLES CUANTITATIVAS
# ============================================================

# Lista de las variables numéricas que se van a analizar.
variables = ["Edad", "Tiempo_Espera_Min", "Costo_Atencion_USD"]

# ------------------------------------------------------------
# Paso 9. Medidas de tendencia central
# ------------------------------------------------------------
# Media: promedio de todos los valores.
# Mediana: valor que queda en medio al ordenar los datos.
# Moda: valor que más se repite (puede haber más de una).
print("\n4.2 MEDIDAS DE TENDENCIA CENTRAL")
for var in variables:
    serie = df[var]
    modas = serie.mode()
    print(f"\n{var}")
    print("  Media  :", round(serie.mean(), 2))
    print("  Mediana:", round(serie.median(), 2))
    if len(modas) == 1:
        print("  Moda   :", modas.iloc[0])
    else:
        # Si varios valores empatan, se avisa que la variable es multimodal.
        print(f"  Moda   : multimodal ({len(modas)} valores), "
              f"el primero es {modas.iloc[0]}")
        
        
        
        
        
        

# ------------------------------------------------------------
# Paso 10. Medidas de posición
# ------------------------------------------------------------
# Mínimo y máximo: valores extremos.
# Q1 (25 %), Q2 (50 %, igual a la mediana) y Q3 (75 %): cuartiles que
# dividen los datos ordenados en cuatro partes iguales.
print("\n4.2 MEDIDAS DE POSICIÓN")
for var in variables:
    serie = df[var]
    print(f"\n{var}")
    print("  Mínimo:", round(serie.min(), 2))
    print("  Q1    :", round(serie.quantile(0.25), 2))
    print("  Q2    :", round(serie.quantile(0.50), 2), "(mediana)")
    print("  Q3    :", round(serie.quantile(0.75), 2))
    print("  Máximo:", round(serie.max(), 2))



# ------------------------------------------------------------
# Paso 11. Medidas de dispersión
# ------------------------------------------------------------
# Indican qué tan separados están los datos entre sí.
# Rango: máximo - mínimo.
# Varianza: promedio de las distancias al cuadrado respecto a la media.
# Desviación estándar: raíz de la varianza (en las mismas unidades del dato).
# IQR: Q3 - Q1, el rango del 50 % central de los datos.
# Coeficiente de variación: desviación / media * 100, permite comparar
# variables con unidades distintas (años, minutos, dólares).
print("\n4.2 MEDIDAS DE DISPERSIÓN")
for var in variables:
    serie = df[var]
    rango = serie.max() - serie.min()
    varianza = serie.var()
    desviacion = serie.std()
    iqr = serie.quantile(0.75) - serie.quantile(0.25)
    cv = desviacion / serie.mean() * 100
    print(f"\n{var}")
    print("  Rango                  :", round(rango, 2))
    print("  Varianza               :", round(varianza, 2))
    print("  Desviación estándar    :", round(desviacion, 2))
    print("  IQR (Q3 - Q1)          :", round(iqr, 2))
    print("  Coef. de variación (%) :", round(cv, 2))
    
    
    
    

# ------------------------------------------------------------
# Paso 12. Resumen general con describe()
# ------------------------------------------------------------
# describe() calcula de un solo golpe conteo, media, desviación, mínimo,
# cuartiles y máximo. Sirve para verificar los resultados de los pasos
# anteriores.
print("\nRESUMEN CON describe()")
print(df[variables].describe().round(2))