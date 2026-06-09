"""
[M3S04] - Ex. 3 - Automatizando Mouse e Teclado com PyAutoGUI

Automação básica de mouse e teclado para preencher campos de texto.
O script abre o Bloco de Notas (Windows) / gedit (Linux), move o mouse
até a área de texto e preenche o conteúdo automaticamente.

Uso:
    1. Execute o script com a janela do editor já aberta.
    2. Use o Ex. 2 (mouse_coordinates.py) para capturar as coordenadas
       do campo de texto e ajuste as variáveis abaixo.
    3. Rode: python keyboard_mouse_automation.py

Para encerrar em caso de emergência: mova o mouse para qualquer canto da tela.
"""

import pyautogui
import pyperclip
import time

# ── Configurações de segurança ──────────────────────────────────────────────
pyautogui.FAILSAFE = True   # mover o mouse a um canto da tela encerra o script
pyautogui.PAUSE = 0.1       # pausa de 0.1s entre cada comando

# ── Coordenadas — ajustar com o mouse_coordinates.py (Ex. 2) ────────────────
CAMPO_TEXTO_X = 960         # coordenada X do campo de texto
CAMPO_TEXTO_Y = 540         # coordenada Y do campo de texto

# ── Mensagem a ser preenchida ────────────────────────────────────────────────
mensagem = (
    "Automação de RPA com PyAutoGUI\n"
    "Exercício 3 - DEVinHouse\n"
    "Preenchimento automático de campos de texto."
)

# ── Automação ────────────────────────────────────────────────────────────────
print("Iniciando automação em 3 segundos... (mova o mouse a um canto para cancelar)")
time.sleep(3)

# 1. Mover o mouse até o campo de texto e clicar (triplo clique para garantir foco)
print(f"Clicando em ({CAMPO_TEXTO_X}, {CAMPO_TEXTO_Y})...")
pyautogui.click(CAMPO_TEXTO_X, CAMPO_TEXTO_Y, clicks=3, interval=0.1)
time.sleep(0.5)

# 2. Limpar qualquer conteúdo existente
pyautogui.hotkey("ctrl", "a")
time.sleep(0.2)

# 3. Colar a mensagem via clipboard (mais confiável que write() para textos longos
#    e caracteres especiais como acentos)
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

print("Automação concluída.")
