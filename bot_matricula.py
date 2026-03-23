import os
import time
import random
import requests
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# ==========================================
# --- CONFIGURACIÓN ---
# ==========================================
# Ahora las credenciales se leen de forma segura, ¡fuera del código fuente!
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

URL_MATRICULA = "https://www.cgeonline.com.ar/tramites/citas/varios/cita-varios.html?t=4"
TEXTO_SIN_CITAS = "En este momento no hay citas disponibles."

# Simulamos ser un navegador común y corriente
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# ==========================================

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': mensaje, 'parse_mode': 'HTML'}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error enviando a Telegram: {e}")

def run_bot():
    print("🤖 Bot de Matrícula Iniciado (Modo Ultra-Ligero)...")
    enviar_telegram("✅ Bot de Matrícula iniciado en el servidor nube.")
    
    while True:
        print(f"[{time.strftime('%H:%M:%S')}] Verificando Alta de Matrícula...")
        try:
            # Hacemos la consulta web directamente
            response = requests.get(URL_MATRICULA, headers=HEADERS, timeout=15)
            
            if TEXTO_SIN_CITAS not in response.text:
                msg = f"🚨 <b>¡CITAS DISPONIBLES!</b> 🚨\nTrámite: <b>Alta de Matrícula</b>\nLink: {URL_MATRICULA}"
                print("¡Turno encontrado!")
                enviar_telegram(msg)
                
                # Pausa de 30 min si encuentra turno para no hacer spam de mensajes
                time.sleep(1800) 
            else:
                print("  Sin citas disponibles.")
        
        except Exception as e:
            print(f"  Error en la conexión: {e}")
        
        # Espera aleatoria entre 3 y 6 minutos para parecer humanos
        tiempo_espera = random.randint(180, 360)
        print(f"Esperando {tiempo_espera // 60} minutos...\n")
        time.sleep(tiempo_espera)

if __name__ == "__main__":
    run_bot()