import requests
import matplotlib.pyplot as plt
import datetime

# Clave de API de OpenWeatherMap
api_key = 'API_KEY'
ciudad = 'Ciudad'

# Cantidad de horas de pronóstico a obtener (ejemplo: 5 horas)
cantidad_horas = 5

# URL de la API para obtener el pronóstico
url = f'http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}&units=metric'

# Hacer la solicitud
respuesta = requests.get(url)
datos = respuesta.json()

# Lista para almacenar las temperaturas y los tiempos
temperaturas = []
tiempos = []

# Procesar los datos para las próximas `cantidad_horas` horas
for i in range(cantidad_horas):
    tiempo = datetime.datetime.now() + datetime.timedelta(hours=i)
    temperatura = datos['list'][i]['main']['temp']
    
    tiempos.append(tiempo)
    temperaturas.append(temperatura)

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f'Temperatura promedio en {ciudad}: {promedio}°C')

# Generar el gráfico
plt.plot(tiempos, temperaturas, marker='o')
plt.title(f'Temperatura en {ciudad} a lo largo del tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()
