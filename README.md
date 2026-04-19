# Bot Monitor de Turnos - Consulado de España

![Status: Maintained](https://img.shields.io/badge/Status-Maintained-brightgreen?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Requests](https://img.shields.io/badge/Library-Requests-green.svg)
![Telegram API](https://img.shields.io/badge/API-Telegram-blue.svg)

Un script automatizado y ligero en Python diseñado para monitorear en tiempo real la disponibilidad de turnos (específicamente *Alta de Matrícula*) en el portal de citas del Consulado de España (`cgeonline.com.ar`). 

Cuando el sistema detecta la apertura de nuevas citas, envía una alerta inmediata a través de un bot de Telegram.

## 🚀 Características Principales

* **Monitoreo Continuo:** Realiza peticiones HTTP periódicas al servidor del consulado.
* **Alertas en Tiempo Real:** Integración directa con la API de Telegram para notificaciones push al celular.
* **Evasión de Bloqueos (Anti-Ban):** Implementa rotación de tiempos de espera (aleatorios) y falsificación de User-Agent para simular tráfico humano legítimo.
* **Ultra-Ligero:** Utiliza únicamente la librería `requests` de Python, eliminando la necesidad de levantar navegadores pesados (Selenium/Chrome), ideal para servidores VPS con recursos limitados (ej. Google Cloud e2-micro).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Librerías:** `requests`, `time`, `random`
* **Infraestructura:** Despliegue en Google Cloud Platform (Ubuntu Linux) utilizando `tmux` para ejecución 24/7 en segundo plano.

## ⚙️ Instalación y Configuración Local

**1. Clonar el repositorio:**
   ```bash
   git clone https://github.com/jlandaa/Bot-Monitor-Turnos
   cd bot-turnos-consulado
   ```
**2. Crear y activar un entorno virtual (Recomendado):**
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```
**3. Instalar dependencias:**
```bash
pip install requests
```
**4. Configurar credenciales:**
Abre el archivo bot.py y reemplaza las variables de configuración con los datos de tu bot de Telegram:
```python
TELEGRAM_TOKEN = 'TU_TOKEN_DE_BOT_AQUI'
CHAT_ID = 'TU_CHAT_ID_AQUI'
```

**☁️ Despliegue en Servidor VPS (Linux 24/7)**
Para que el bot funcione ininterrumpidamente en un servidor (como GCP o AWS):

**1. Sube el script al servidor y configura el entorno Python.**

**2. Inicia una sesión de multiplexor de terminal:**
```bash
tmux new -s bot_consulado
```
**3. Ejecuta el script:**
```python
python3 bot_matricula.py
```
**4. Desconéctate de la sesión de forma segura presionando Ctrl + B, soltando, y luego presionando D. El bot quedará ejecutándose en segundo plano.**

**⚠️ Aviso Legal / Disclaimer**
Este proyecto fue desarrollado con fines estrictamente educativos y de uso personal para automatizar una tarea repetitiva. No realiza ataques de denegación de servicio (DDoS) ni evade sistemas CAPTCHA obligatorios para la creación de cuentas. Se recomienda configurar tiempos de espera (sleep) prudentes para no saturar los servidores gubernamentales.

## 👨‍💻 Sobre mí
**Juan Manuel Landa**
* **Ingeniero en Computación** | **Data Analyst & BI Consultant**
* 📍 Quilmes, Buenos Aires, Argentina
* 💼 [LinkedIn](https://ar.linkedin.com/in/juan-manuel-landa/en)
* 🌐 [Portfolio Personal](https://juan-manuel-landa.netlify.app/)

Este proyecto forma parte de mi búsqueda activa de nuevas oportunidades en el área de **Data & Business Intelligence**.
