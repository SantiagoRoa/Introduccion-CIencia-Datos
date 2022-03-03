import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://www.nrcan.gc.ca/sites/nrcan/files/oee/files/csv/MY2021%20Fuel%20Consumption%20Ratings.csv

# Nelson Santiago Roa Garzón - 20172020099

# Se carga el dataframe
df = pd.read_csv('MY2021 Fuel Consumption Ratings.csv', sep=",", encoding='cp1252', low_memory=False)

# Se elimina la primera fila del dataframe y se recortan los primeros 100 registros
datos = df[['Make', 'Model', 'Engine Size', 'Cylinders', 'Fuel Consumption', 'CO2 Emissions']].drop([0], axis=0).iloc[0:100]

# Se convierten los tipos de las columnas seleccionadas a numéricos
datos[["Engine Size", "Fuel Consumption", "CO2 Emissions"]] = datos[["Engine Size", "Fuel Consumption", "CO2 Emissions"]].apply(pd.to_numeric)

# Se muestran los primeros 20 registros
print("\nDatos de consumo de combustible y emisiones de carbono de vehículos en el 2021:\n")
print(datos.head(20))

# Gráfica
datos.sort_values(by=['CO2 Emissions']).plot(y="Fuel Consumption", x="CO2 Emissions")

# Diagrama de barras
datos.iloc[0:20].sort_values(by="Engine Size").plot.bar(x="Fuel Consumption", y="Engine Size")

# Diagrama de area
datos.sort_values(by=['CO2 Emissions']).plot.area(x="Make", y=["Fuel Consumption", "CO2 Emissions"])

# Histograma
datos[["CO2 Emissions"]].plot.hist()

# Diagrama de caja
datos[["CO2 Emissions"]].plot.box()

# Diagrama de dispersión
datos.plot.scatter("Engine Size", "CO2 Emissions")

# Matriz de dispersión
pd.plotting.scatter_matrix(datos, alpha=0.2)

# Multidimensional
#pd.plotting.radviz(datos, 'Make')

plt.show()