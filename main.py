#Instalamos las librerias con 'pip install numpy pandas matplotlib seaborn'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8-darkgrid")  # Stylizar el grafico

notas = np.random.randint(50, 100, size=20)  # Array con notas random

print("notas ", notas)  # Array aleatorio

#Calcular medidas estidisticas basicas
#Utilizamos numpy
media = np.mean(notas)
mediana = np.median(notas)
varianza = np.var(notas)
desviacion_estandar = np.std(notas)
rango = np.max(notas) - np.min(notas)

#Percentiles, utilizamos Numpy
Q1 = np.percentile(notas, 25)  # percentil 25
Q2 = np.percentile(notas, 50)  # percentil 50
Q3 = np.percentile(notas, 75)  # percentil 75

#Utilizamos Pandas para calcular la moda
moda = pd.Series(notas).mode()[0]

#Mostramos los datos que conseguimos
print("Media ", media)
print("Mediana ", mediana)
print("Moda ", moda)
print("Varianza ", varianza)
print("Desviacion ", desviacion_estandar)
print("Rango ", rango)
print("Percientil 25 ", Q1)
print("Percientil 50 ", Q2)
print("Percientil 75 ", Q3)

#Histograma de Frecuencia
#Configuraciones
#.hist es para hacer este tipo de graficos, luego agregarmos las configuraciones basicas como color,borde, cant_datos y array
plt.hist(notas, bins=10, color="red", edgecolor="black")
plt.title("Distribucion de notas", fontsize=14)  # Titulo
#Determinamos Eje X e Y
plt.xlabel("Notas", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.show()  # Mostrar grafico determinado