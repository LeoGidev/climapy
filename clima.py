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