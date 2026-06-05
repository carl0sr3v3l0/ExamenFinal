import os

# Determina la ruta automática de la carpeta del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define dónde se guardará el archivo CSV (dentro de una carpeta llamada 'data')
CSV_PATH = os.path.join(BASE_DIR, 'data', 'datos_sensor.csv')