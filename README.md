# Screensaver_bypass

Jiggler simple para Windows que evita que se active el protector de pantalla (o el bloqueo por inactividad) simulando la pulsación de la tecla **Shift** a intervalos regulares.
Ideal para el teletrabajo.

## Descripción

El script duerme durante N minutos y luego simula un `keyDown` + `keyUp` de Shift usando la API de Windows (`ctypes` + `user32.dll`). Esto resetea el contador de inactividad del sistema sin depender de librerías externas.

- Solo funciona en **Windows** (usa `ctypes.windll.user32.keybd_event`).
- No requiere permisos de administrador.
- Sin dependencias externas: solo librería estándar de Python.

## Requisitos

- Windows
- Python 3.x

## Uso

```
python SimpleJiggler.py <minutos>
```

Ejemplo (jiggle cada 5 minutos):

```
python SimpleJiggler.py 5
```

Si no se pasa ningún argumento, se usa un valor por defecto de 5 minutos.

Para detener el script, presioná `Ctrl+C` en la terminal.

### Acceso rápido (Windows)

El archivo [`SimpleJiggler.bat`](SimpleJiggler.bat) lanza el script con el valor por defecto (5 minutos) haciendo doble clic, sin necesidad de abrir una terminal.

## Crear ejecutable (opcional)

Podés empaquetar el script como un `.exe` standalone con [PyInstaller](https://pyinstaller.org/):

```bash
pip install -U pyinstaller
pyinstaller SimpleJiggler.py
```

El ejecutable resultante queda en `dist/SimpleJiggler.exe`.
