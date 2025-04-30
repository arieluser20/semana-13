from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Configuración inicial
DRIVER_PATH = 'chromedriver.exe'
PROXY = "IP:PUERTO"  # Opcional para evitar bloqueos
TIKTOK_URL = "https://www.tiktok.com"

def check_xss_vulnerability():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(TIKTOK_URL)
    
    # Simula inyección XSS en campos de búsqueda (ejemplo teórico)
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('<script>alert("Prueba XSS")</script>')
    search_box.submit()
    
    time.sleep(3)
    driver.quit()

def test_api_endpoints():
    # Verifica endpoints expuestos (ej: ads.tiktok.com vulnerable en [2])
    endpoints = ["https://ads.tiktok.com", "https://api.tiktok.com"]
    for endpoint in endpoints:
        response = requests.get(endpoint)
        if "X-Frame-Options" not in response.headers:
            print(f"Posible vulnerabilidad en {endpoint} [2][8]")

if __name__ == "__main__":
    check_xss_vulnerability()
    test_api_endpoints()
