# 📊 Sistema de Monitoreo IoT - Potenciómetro con ESP32 y Flask

Este proyecto consiste en un sistema de adquisición, almacenamiento, procesamiento estadístico y visualización de datos en tiempo real provenientes de un sensor analógico (potenciómetro) conectado a un módulo ESP32. Los datos son enviados mediante comunicación serial a una aplicación web desarrollada en Python con Flask.

---

## 🛠️ Descripción del Hardware
* **Microcontrolador:** ESP32 (NodeMCU).
* **Sensor:** Potenciómetro lineal de 10kΩ.
* **Conexión de pines:** * VCC del potenciómetro -> Pin 3.3V del ESP32.
  * GND del potenciómetro -> Pin GND del ESP32.
  * Señal del potenciómetro -> Pin ADC (GPIO 34 / A2) del ESP32.
* **Protocolo de comunicación:** UART (Comunicación Serial a USB) configurada a una velocidad de **115200 baudios**.

---

## 📦 Dependencias del Sistema
El proyecto requiere **Python 3.13** o superior y las siguientes librerías:
* **Flask:** Servidor web para la interfaz de usuario.
* **Pandas & NumPy:** Procesamiento de datos y cálculo de métricas estadísticas (Promedio, Máximo, Mínimo, Desviación Estándar).
* **Matplotlib:** Generación automática de gráficas dinámicas.
* **PySerial:** Escucha activa del puerto serial COM.

---

## 📂 Estructura del Proyecto

```text
FinalAP/
 ├── App.py               # Servidor Flask y escucha del hilo Serial (COM3)
 ├── analyzer.py          # Lógica de procesamiento estadístico con Pandas
 ├── plotter.py           # Renderizado de gráficas con Matplotlib
 ├── config.py            # Rutas relativas y absolutas del sistema
 ├── requirements.txt     # Listado de librerías necesarias
 ├── README.md            # Documentación del proyecto
 ├── data/
 │    └── datos_sensor.csv # Historial base de datos local en texto plano
 └── templates/
      └── index.html      # Panel web de visualización (Dashboard)
