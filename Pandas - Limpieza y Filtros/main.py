import pandas as pd

# https://www.nrcan.gc.ca/sites/nrcan/files/oee/files/csv/MY2021%20Fuel%20Consumption%20Ratings.csv

# Integrantes
# Nelson Santiago Roa Garzón = 20172020099
# Christian Isaac Gamboa Restrepo = 20172020076


datos = pd.read_csv('MY2021 Fuel Consumption Ratings.csv', sep=",", encoding='cp1252', low_memory=False)
raw = datos[['Make', 'Model', 'Engine Size', 'Cylinders', 'Fuel Consumption', 'CO2 Emissions']]
soloNumeros = datos[['Model', 'Engine Size', 'Cylinders', 'Fuel Consumption', 'CO2 Emissions']]
print('\nDatos iniciales \n')
print(datos)
print('\nSelección de columnas \n')
print(raw.head())

datoVacío = raw.isnull() #True si el dato está vacío, es NaN, o NaT (en formato de fecha).
print('\nDatos NaN \n')
print(datoVacío)

#Remuover filas o columnas que tengan valores NaN
sinNaN = raw.dropna(axis=0, how='any')
sinNaN = sinNaN.dropna(axis=1, how='any')
print('\nEliminación de filas y columnas NaN \n')
print(sinNaN)
#axis 0: Fila; 1:Columna
#how any: remueve axis si hay por lo menos un NaN en axis; all: si todos los valores en axis son NaN
#tresh minima cantidad de valores de NaN para remover axis

print('\nCambio de NaN \n')
datosSinNaN = raw.fillna(value='Dato no especificado') #Cambiar cualquier valor NaN por value
print(datosSinNaN.head())

print('\n Cambio de NaN a promedio de columna \n')
promedioNaN = soloNumeros.fillna(raw.mean(axis=0)) #Cambiar cualquier NaN por el promedio de los valores de la columna
print(promedioNaN.head())

print('\n Cambio de NaN por valor consecutivo \n')
datosSinNaN3 = raw.fillna(method='bfill', limit=1) #Cambiar cualquier el valor del indice consecutivo a este (cuando no se especifica un value)
print(datosSinNaN3.head())

print('\n Filtro 1 \n')
filtro1 = raw['Model'] >= '2015' #Retorna true si se cumple la condición para el valor de la columna dada
print(filtro1)

print('\n Filtro 2 \n')
filtro2 = raw[raw['Make'] == 'Audi'] #Selecciona todas las filas donde se cumple la condicióin de la columna dada
print(filtro2.head())

print('\n Filtro 3 \n')
filtro3 = raw['CO2 Emissions'][raw['CO2 Emissions'] > '220'] #Selecciona la columna con los datos que cumplen la condición de la columna
print(filtro3)

print('\n Filtro 4 \n')
filtro4 = raw[(raw['Make'] == 'Audi') & (raw['CO2 Emissions'] > '280') & (raw['Cylinders'] == 6)] #Selecciona datos que cumplen varias condiciones
print(filtro4)