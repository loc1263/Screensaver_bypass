# Screensaver F Jiggler
# Use: python SimpleJiggler.py <minutos>
# Ejemplo: python SimpleJiggler.py 5

import ctypes
import time
import sys

VK_SHIFT = 0x10
KEYEVENTF_KEYUP = 0x0002


def press_shift():
    ctypes.windll.user32.keybd_event(VK_SHIFT, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0)


def main():
    if len(sys.argv) > 1:
        try:
            minutos = int(sys.argv[1])
        except ValueError:
            print("El parámetro debe ser un número entero. Usando 5 minutos por defecto.")
            minutos = 5
    else:
        print("Usando 5 minutos por defecto.")
        minutos = 5

    ciclos = 0

    print("Script run.... ")

    try:
        while True:
            ciclos += 1
            time.sleep(minutos * 60)
            press_shift()

            now = time.strftime("%H:%M:%S")
            print("Ciclo: ", ciclos, "- Hora: ", now)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")


if __name__ == "__main__":
    main()
