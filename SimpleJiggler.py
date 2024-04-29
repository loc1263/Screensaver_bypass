# Screensaver F Jiggler
# Use: python SimpleJiggler.py <minutos>
# Ejemplo: python SimpleJiggler.py 5

import pyautogui
import time
import sys

Minutos = int(sys.argv[1])
ciclos = 0

print("Script run.... ")

while True:
    ciclos += 1
    time.sleep(Minutos * 60)
    pyautogui.keyUp("shift")

    now = time.strftime("%H:%M:%S")
    print("Ciclo: ", ciclos, "- Hora: ", now)
