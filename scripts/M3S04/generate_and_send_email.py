"""
[M3S04] - Ex. 5 - Gerando e Preenchendo o E-mail Final

Fluxo completo de automação:
  1. Lê o conteúdo da Gupy já copiado pelo Ex. 4 (ou copia novamente)
  2. Abre o ChatGPT, cola o conteúdo + prompt de análise e aguarda resposta
  3. Copia a resposta do ChatGPT
  4. Abre o Gmail, compõe e envia o e-mail com a análise

Uso:
    1. Execute o Ex. 4 (copy_page_content.py) para copiar o conteúdo da Gupy.
    2. Use o Ex. 2 (mouse_coordinates.py) para capturar as coordenadas abaixo.
    3. Garanta que está logado no ChatGPT e no Gmail no navegador.
    4. Rode: python generate_and_send_email.py

Para encerrar em caso de emergência: mova o mouse para qualquer canto da tela.
"""

import pyautogui
import pyperclip
import time

# ── Configurações de segurança ──────────────────────────────────────────────
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# ── Configurações — ajustar conforme necessário ──────────────────────────────
EMAIL_DESTINATARIO = "lucas.ribeiro.lima@edu.sc.senai.br"
EMAIL_ASSUNTO      = "[M3S04] Ex. 5 - Análise de Vagas Remotas - Gupy"

PROMPT_ANALISE = (
    "Com base nas vagas abaixo extraídas da plataforma Gupy, "
    "faça um resumo das principais oportunidades remotas disponíveis, "
    "destacando: cargo, empresa, requisitos principais e diferenciais. "
    "Apresente em formato de lista organizada.\n\n"
    "Vagas:\n"
)

# ── Coordenadas — ajustar com o mouse_coordinates.py (Ex. 2) ────────────────
CAMPO_CHATGPT_X    = 760    # campo de texto do ChatGPT
CAMPO_CHATGPT_Y    = 900
BOTAO_COMPOSE_X    = 120    # botão "Escrever" do Gmail
BOTAO_COMPOSE_Y    = 200
CAMPO_PARA_X       = 700    # campo destinatário do Gmail
CAMPO_PARA_Y       = 320
CAMPO_ASSUNTO_X    = 700    # campo assunto do Gmail
CAMPO_ASSUNTO_Y    = 360
CORPO_EMAIL_X      = 700    # corpo do e-mail do Gmail
CORPO_EMAIL_Y      = 450


def abrir_nova_aba(url: str, tempo_espera: int = 5) -> None:
    """Abre uma nova aba e navega para a URL informada."""
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "l")   # foca a barra de endereços
    time.sleep(0.3)
    pyperclip.copy(url)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(tempo_espera)


# ════════════════════════════════════════════════════════════
# FASE 1 — Recuperar conteúdo da Gupy do clipboard
# ════════════════════════════════════════════════════════════
conteudo_gupy = pyperclip.paste()
if not conteudo_gupy:
    print("Clipboard vazio. Execute o Ex. 4 (copy_page_content.py) primeiro.")
    exit(1)

print(f"Conteúdo da Gupy disponível no clipboard ({len(conteudo_gupy)} caracteres).")
print("Iniciando automação em 3 segundos... (mova o mouse a um canto para cancelar)")
time.sleep(3)

# ════════════════════════════════════════════════════════════
# FASE 2 — ChatGPT: colar conteúdo + prompt e copiar resposta
# ════════════════════════════════════════════════════════════
print("\n[1/3] Abrindo ChatGPT...")
abrir_nova_aba("https://chatgpt.com", tempo_espera=5)

print("Clicando no campo de texto do ChatGPT...")
pyautogui.click(CAMPO_CHATGPT_X, CAMPO_CHATGPT_Y, clicks=3, interval=0.1)
time.sleep(0.5)

print("Colando prompt + conteúdo das vagas...")
mensagem_completa = PROMPT_ANALISE + conteudo_gupy[:8000]  # limite seguro de tokens
pyperclip.copy(mensagem_completa)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

print("Enviando para o ChatGPT...")
pyautogui.press("enter")

print("Aguardando resposta do ChatGPT (30s)...")
time.sleep(30)

print("Copiando resposta do ChatGPT...")
pyautogui.hotkey("ctrl", "a")
time.sleep(0.3)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

resposta_chatgpt = pyperclip.paste()
print(f"Resposta copiada ({len(resposta_chatgpt)} caracteres).")

# ════════════════════════════════════════════════════════════
# FASE 3 — Gmail: compor e enviar e-mail
# ════════════════════════════════════════════════════════════
print("\n[2/3] Abrindo Gmail...")
abrir_nova_aba("https://mail.google.com", tempo_espera=5)

print("Clicando no botão Escrever (Compose)...")
pyautogui.click(BOTAO_COMPOSE_X, BOTAO_COMPOSE_Y)
time.sleep(1.5)

print("Preenchendo destinatário...")
pyautogui.click(CAMPO_PARA_X, CAMPO_PARA_Y)
time.sleep(0.3)
pyperclip.copy(EMAIL_DESTINATARIO)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(0.3)

print("Preenchendo assunto...")
pyautogui.click(CAMPO_ASSUNTO_X, CAMPO_ASSUNTO_Y)
time.sleep(0.3)
pyperclip.copy(EMAIL_ASSUNTO)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)

print("Colando análise no corpo do e-mail...")
pyautogui.click(CORPO_EMAIL_X, CORPO_EMAIL_Y)
time.sleep(0.3)
pyperclip.copy(resposta_chatgpt)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

print("Enviando e-mail...")
pyautogui.hotkey("ctrl", "enter")
time.sleep(1)

print("\n[3/3] E-mail enviado com sucesso!")
