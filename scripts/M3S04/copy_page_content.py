"""
[M3S04] - Ex. 4 - Copiar Informações de uma Página Utilizando PyAutoGUI

Abre o navegador, acessa a página de vagas da Gupy e copia todo o
conteúdo para o clipboard, para uso posterior no ChatGPT (Ex. 5).

Uso:
    1. Use o Ex. 2 (mouse_coordinates.py) para capturar a coordenada
       da barra de endereços do seu navegador e ajuste BARRA_ENDERECO_Y.
    2. Rode: python copy_page_content.py

Para encerrar em caso de emergência: mova o mouse para qualquer canto da tela.
"""

import pyautogui
import pyperclip
import time
import webbrowser

# ── Configurações de segurança ──────────────────────────────────────────────
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# ── URL alvo ─────────────────────────────────────────────────────────────────
URL_VAGAS = "https://portal.gupy.io/job-search/sortBy=publishedDate&workplaceTypes[]=remote"

# ── Coordenadas — ajustar com o mouse_coordinates.py (Ex. 2) ────────────────
BARRA_ENDERECO_X = 700      # coordenada X da barra de endereços do navegador
BARRA_ENDERECO_Y = 45       # coordenada Y da barra de endereços do navegador

# ── Automação ────────────────────────────────────────────────────────────────
print("Abrindo navegador...")
webbrowser.open(URL_VAGAS)
time.sleep(5)   # aguardar carregamento da página

print("Selecionando todo o conteúdo da página...")
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)

print("Copiando conteúdo para o clipboard...")
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Verificar se algo foi copiado
conteudo = pyperclip.paste()
if conteudo:
    print(f"Conteúdo copiado com sucesso! ({len(conteudo)} caracteres)")
    print("Prévia (primeiros 300 caracteres):")
    print("-" * 45)
    print(conteudo[:300])
    print("-" * 45)
else:
    print("Aviso: nada foi copiado. Verifique se a página carregou corretamente.")
