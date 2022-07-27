# Screensaver F Jiggler

import pyautogui
import time
import sys

Minutos = int(sys.argv[1])
ciclos = 0
print("Script run.... ")

while True:
    ciclos += 1
    time.sleep(Minutos * 60)
    pyautogui.keyUp('shift')
    print("Ciclo: ", ciclos)
