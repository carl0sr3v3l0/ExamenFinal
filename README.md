# 📊 Sistema de Monitoreo IoT - Potenciómetro con ESP32 y Flask

Este proyecto consiste en un sistema de adquisición, almacenamiento, procesamiento estadístico y visualización de datos en tiempo real provenientes de un sensor analógico (potenciómetro) conectado a un módulo ESP32. Los datos son enviados mediante comunicación serial a una aplicación web desarrollada en Python con Flask.

---

## 🛠️ Descripción del Hardware

- **Microcontrolador:** ESP32 (NodeMCU)
- **Sensor:** Potenciómetro lineal de 10kΩ
- **Conexión de pines:**
  - VCC del potenciómetro → Pin 3.3V del ESP32
  - GND del potenciómetro → Pin GND del ESP32
  - Señal del potenciómetro → Pin ADC (GPIO 34 / A2) del ESP32
- **Protocolo de comunicación:** UART (Comunicación Serial a USB) configurada a **115200 baudios**

---

## 📦 Dependencias del Sistema

El proyecto requiere **Python 3.13** o superior y las siguientes librerías:

- **Flask:** Servidor web para la interfaz de usuario
- **Pandas & NumPy:** Procesamiento estadístico (Promedio, Máximo, Mínimo, Desviación Estándar)
- **Matplotlib:** Generación automática de gráficas dinámicas
- **PySerial:** Escucha activa del puerto serial COM

---

## 📂 Estructura del Proyecto

```
FinalAP/
├── App.py               # Servidor Flask y escucha del hilo Serial (COM3)
├── analyzer.py          # Lógica de procesamiento estadístico con Pandas
├── plotter.py           # Renderizado de gráficas con Matplotlib
├── config.py            # Rutas relativas y absolutas del sistema
├── requirements.txt     # Listado de librerías necesarias
├── README.md            # Documentación del proyecto
├── data/
│   └── datos_sensor.csv # Historial base de datos local en texto plano
└── templates/
    └── index.html       # Panel web de visualización (Dashboard)
```

---

## ⚙️ Instrucciones de Instalación y Ejecución

Como la consola integrada del entorno de desarrollo se encuentra en mantenimiento, la ejecución se realiza de manera nativa a través del **Símbolo del Sistema (CMD)** de Windows.

### 1. Instalación de librerías

```bash
cd C:\Users\revel\OneDrive\Documentos\FinalAP
pip install -r requirements.txt
```

### 2. Ejecución del servidor

Asegúrese de conectar el ESP32 al puerto `COM3` y luego ejecute:

```bash
python App.py
```

### 3. Uso de la aplicación

1. Abra su navegador e ingrese a: `http://127.0.0.1:5000/`
2. Mueva la perilla del potenciómetro. La página se actualizará automáticamente mostrando el estado (**BAJO**, **NORMAL**, **ALTO**), el voltaje en tiempo real y las gráficas de comportamiento.

---

## 🛡️ Seguridad y Claves Privadas

Este desarrollo utiliza exclusivamente comunicación por hardware local mediante el protocolo UART. El sistema **no expone API Keys, contraseñas de redes Wi-Fi, ni credenciales privadas** en ninguno de los scripts cargados en este repositorio público.

---

## 📸 Evidencia de Funcionamiento

```
Dato recibido -> Tiempo: 743010ms, ADC: 3673, V: 2.96V
Dato recibido -> Tiempo: 744010ms, ADC: 3662, V: 2.95V
DEBUG: Enviando a la web -> {'muestras': 374, 'estado': 'ALTO', 'promedio': 1.77, 'max': 3.3}
```

### 📊 Gráficas Generadas (Análisis de Señal)

![Dashboard](assets/dashboard.png)
![Gráfica de señal](assets/grafica_senal.png)
