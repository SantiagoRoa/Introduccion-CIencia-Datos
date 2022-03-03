import pandas as pd
import dateutil


# 1. Cargar el CSV phone_data y convertir la columna date de string a tiempo
data = pd.read_csv('phone_data.csv', index_col='index')
data['date'] = data['date'].apply(dateutil.parser.parse)

# 2. ¿Cuál fue el ítem (llamada/datos) de mayor duración?
maxItem = data['duration'].max()
#print('Item de mayor duración: ', maxItem)

# ¿Cuál fue la llamada de mayor duración?
#maxCall = data[data['item']=='call'][data['duration'] == data['duration'].max()]
#print('Llamada de mayor duración: ', maxCall)

# ¿Cuál fue el evento de datos de mayor duración?
#maxDataEvent = data[data['item']=='data'][data['duration'] == data['duration'].max()]
#print('Evento de datos de mayor duración: ', maxDataEvent)

# 3. ¿Cual fue el total de segundos de todas las llamadas?
allCallsTime = data['duration'][data['item']=='call'].sum()
#print('Total de segundos de todas las llamadas: ',allCalls)

# ¿Cuál fue el total de segundos entre sms y eventos de datos?
allSmsTime =  data['duration'][data['item']=='sms'].sum()
allDataEventTime = data['duration'][data['item']=='data'].sum()
allTime = allSmsTime + allDataEventTime
#print('Total de segundos entre sms y eventos de datos: ',allTime)

# 4. ¿Cuantas entradas hay por cada uno de los meses?
monthColumnCount = data['month'].value_counts()
#print(monthColumn)

# ¿Cuantas entradas de datos hay por cada uno de las redes?
dataColumnCount = data['network'][data['item']=='data'].value_counts()
#print('Total de datos por cada una de las redes: ',dataColumnCount)

# ¿Cuantas entradas de llamada hay por cada una de las redes?
callColumnCount = data['network'][data['item']=='call'].value_counts()
#print('Total de llamadas por cada una de las redes: ',callColumnCount)

# 5. Obtener la suma de la duración por més
data['duration'].sum()
data.groupby('month')['duration'].sum()