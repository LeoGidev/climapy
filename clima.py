import requests
import matplotlib.pyplot as plt
import datetime

# Clave de API de OpenWeatherMap
api_key = 'API_KEY'
ciudad = 'Ciudad'
# Lista para almacenar las temperaturas
temperaturas = []

# URL de la API para obtener el clima actual
url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

# Hacer la solicitud
respuesta = requests.get(url)
datos = respuesta.json()

# Extraer la temperatura
temperatura_actual = datos['main']['temp']
print(f'Temperatura actual en {ciudad}: {temperatura_actual}°C')

# Simulación de múltiples llamadas a la API (usando datos actuales repetidos como ejemplo)
for i in range(5):
    
    temperaturas.append(datos['main']['temp'])

# Calcular el promedio de las temperaturas
promedio = sum(temperaturas) / len(temperaturas)
print(f'Temperatura promedio en {ciudad}: {promedio}°C')

# Simulando tiempos (fechas o horas)
tiempos = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(len(temperaturas))]

plt.plot(tiempos, temperaturas, marker='o')
plt.title(f'Temperatura en {ciudad} a lo largo del tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()