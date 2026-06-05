import matplotlib
matplotlib.use('Agg') # Evita errores de hilos en servidores web como Flask
import matplotlib.pyplot as plt
import pandas as pd
import os
from config import CSV_PATH

def generar_graficas():
    # Asegura que la carpeta para guardar los gráficos exista
    if not os.path.exists('static/plots'):
        os.makedirs('static/plots')
    
    try:
        if not os.path.exists(CSV_PATH):
            return
            
        df = pd.read_csv(CSV_PATH)
        if len(df) < 2: 
            return 

        # Gráfica 1: Evolución del Voltaje en el tiempo
        plt.figure(figsize=(6,4))
        plt.plot(df['tiempo_ms'], df['voltaje'], color='blue', label='Voltaje')
        plt.title("Voltaje vs Tiempo")
        plt.xlabel("Tiempo (ms)")
        plt.ylabel("Voltaje (V)")
        plt.grid(True)
        plt.savefig('static/plots/sensor_tiempo.png')
        plt.close()

        # Gráfica 2: Histograma de frecuencias
        plt.figure(figsize=(6,4))
        plt.hist(df['voltaje'], bins=15, color='green', edgecolor='black')
        plt.title("Distribución de Voltaje")
        plt.savefig('static/plots/histograma.png')
        plt.close()

        # Gráfica 3: Tendencia con Promedio Móvil
        plt.figure(figsize=(6,4))
        plt.plot(df['voltaje'].rolling(window=10).mean(), color='red')
        plt.title("Promedio Móvil (Suavizado)")
        plt.grid(True)
        plt.savefig('static/plots/promedio_movil.png')
        plt.close()
        
    except Exception as e:
        print(f"Error al generar gráficas: {e}")    