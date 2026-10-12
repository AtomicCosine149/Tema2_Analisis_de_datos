import os
import numpy as np
datos= np.array([17, 21, 21 ,21 ,21, 21, 21, 21, 21, 21,
               21, 22, 22, 23, 23, 23, 24, 24, 25, 30])
Q1=np.percentile(datos, 25) #los numeros se manejan en porcentaje
Q3=np.percentile(datos, 75)
IQR=Q3-Q1
Li=Q1-1.5*IQR
Ls=Q3+1.5*IQR
#Q1 es la parte baja de la cajita
#Q3 es la parte arriba
atipicos=datos[
    (datos<Li)|(datos>Ls)]
print(atipicos)