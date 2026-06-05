from flask import Flask, render_template
import threading
import os
import serial
import csv
from analyzer import analizar_datos
from plotter import generar_graficas
from config import CSV_PATH

# Inicializamos Flask forzando la ruta de la carpeta que corregiste
directorio_base = os.path.dirname(os.path.abspath(__file__))
ruta_templates = os.path.join(directorio_base, 'templates')
app = Flask(__name__, template_folder=ruta_templates)

def tu_funcion_serial():
    """Hilo secundario: Lee el hardware y genera las gráficas de fondo"""
    if not os.path.exists(os.path.dirname(CSV_PATH)):
        os.makedirs(os.path.dirname(CSV_PATH))
        
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
        with open(CSV_PATH, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['tiempo_ms', 'adc', 'voltaje'])

    try:
        PUERTO_SERIAL = 'COM9' # Asegúrate de que sea tu puerto real
        ser = serial.Serial(PUERTO_SERIAL, 115200, timeout=1)
        print(f"\n🚀 ESCUCHANDO ESP32 EN {PUERTO_SERIAL}...")
        
        contador_para_graficas = 0
        while True:
            linea = ser.readline().decode('utf-8').strip()
            if linea:
                datos = linea.split(',')
                if len(datos) == 3:
                    # Guardamos el dato en el CSV
                    with open(CSV_PATH, 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(datos)
                    print(f"📥 Guardado -> T: {datos[0]}ms, ADC: {datos[1]}, V: {datos[2]}V")
                    
                    # 📊 OPTIMIZACIÓN: Cada 5 datos nuevos, actualiza las imágenes .png
                    contador_para_graficas += 1
                    if contador_para_graficas >= 5:
                        generar_graficas()
                        contador_para_graficas = 0
                        
    except Exception as e:
        print(f"❌ Error en hilo Serial: {e}")

@app.route("/")
def index():
    """Ruta principal: Solo lee los datos procesados y renderiza el HTML instantáneamente"""
    resumen = analizar_datos()
    return render_template("index.html", data=resumen)

if __name__ == "__main__":
    # Arrancamos el hilo del ESP32
    threading.Thread(target=tu_funcion_serial, daemon=True).start()
    
    # ⚠️ CRÍTICO PARA HARDWARE: debug=True con use_reloader=False evita el doble hilo
    app.run(port=5000, debug=True, use_reloader=False)