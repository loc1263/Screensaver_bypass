# Screensaver F Jiggler
# Ejemplo python SimpleJiggler 1

import pyautogui
import time
import sys
from datetime import datetime

Minutos = int(sys.argv[1])
ciclos = 0
Tiempo = 0

print("Script run.... ")

while True:
    ciclos += 1
    time.sleep(Minutos * 60)
    Tiempo = Tiempo + (Minutos * 60)
    pyautogui.keyUp('shift')
    tiempo_formateado = datetime.utcfromtimestamp(Tiempo).strftime('%H:%M:%S')
    print("Ciclo: ", ciclos, "Tiempo: ", tiempo_formateado)
