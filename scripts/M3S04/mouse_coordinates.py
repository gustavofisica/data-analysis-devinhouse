"""
[M3S04] - Ex. 2 - Localizando Coordenadas da Tela com Python

Script simples para identificar a posição atual do mouse na tela.
As coordenadas (x, y) são impressas continuamente a cada 0.5 segundo.

Uso:
    python mouse_coordinates.py

Para encerrar: pressione Ctrl+C.
"""

import pyautogui
import time

print("Rastreando posição do mouse... (pressione Ctrl+C para parar)")
print("-" * 45)

try:
    while True:
        x, y = pyautogui.position()
        print(f"x = {x:>5}   y = {y:>5}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print(f"\nCaptura encerrada. Última posição registrada: x={x}, y={y}")
