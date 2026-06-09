"""
[M3S04] - Ex. 6 - Script Final RPA: Copiar Vagas → Analisar → Enviar E-mail

Script único que executa todo o fluxo de ponta a ponta:
  1. Abre o navegador e acessa a página de vagas da Gupy
  2. Copia o conteúdo da página (ctrl+a, ctrl+c)
  3. Envia o conteúdo para o Google Gemini e obtém análise
  4. Exibe o e-mail para confirmação
  5. Envia o e-mail com a análise e este script anexado

Pré-requisitos:
  - Arquivo .env com:
      GEMINI_API_KEY      → https://aistudio.google.com/apikey (gratuito)
      GMAIL_USER          → seu e-mail Gmail
      GMAIL_APP_PASSWORD  → https://myaccount.google.com/apppasswords
      EMAIL_DESTINATARIO  → destinatário do e-mail
  - pip install pyautogui pyperclip google-genai python-dotenv

Uso:
    python rpa_final.py

Para encerrar em caso de emergência: mova o mouse para qualquer canto da tela.
"""

import os
import smtplib
import textwrap
import time
import webbrowser
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import pyautogui
import pyperclip
from dotenv import load_dotenv
from google import genai

# ── Carregar variáveis de ambiente ──────────────────────────────────────────
load_dotenv()

GEMINI_API_KEY     = os.getenv("GEMINI_API_KEY")
GMAIL_USER         = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

for var, nome in [
    (GEMINI_API_KEY,     "GEMINI_API_KEY"),
    (GMAIL_USER,         "GMAIL_USER"),
    (GMAIL_APP_PASSWORD, "GMAIL_APP_PASSWORD"),
    (EMAIL_DESTINATARIO, "EMAIL_DESTINATARIO"),
]:
    if not var:
        raise EnvironmentError(f"Variável {nome} não encontrada. Configure o arquivo .env")

# ── Configurações ─────────────────────────────────────────────────────────────
URL_VAGAS     = "https://portal.gupy.io/job-search/sortBy=publishedDate&workplaceTypes[]=remote"
EMAIL_ASSUNTO = "[M3S04] Ex. 6 - RPA Final: Análise de Vagas Remotas - Gupy"

PROMPT_ANALISE = textwrap.dedent("""\
    Com base nas vagas abaixo extraídas da plataforma Gupy, faça um resumo \
    das principais oportunidades remotas disponíveis, destacando: cargo, \
    empresa, requisitos principais e diferenciais. \
    Apresente em formato de lista organizada.

    Vagas:
    """)

pyautogui.FAILSAFE = True
pyautogui.PAUSE    = 0.1

# ════════════════════════════════════════════════════════════
# FASE 1 — Capturar conteúdo da Gupy via PyAutoGUI
# ════════════════════════════════════════════════════════════
print("=" * 60)
print("[1/4] Abrindo navegador e acessando Gupy...")
webbrowser.open(URL_VAGAS)
time.sleep(5)

print("      Selecionando todo o conteúdo (ctrl+a)...")
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)

print("      Copiando para o clipboard (ctrl+c)...")
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

conteudo_gupy = pyperclip.paste()
if not conteudo_gupy.strip():
    raise RuntimeError("Clipboard vazio após ctrl+c. Verifique se a página carregou.")

print(f"      Conteúdo capturado: {len(conteudo_gupy)} caracteres.")

# ════════════════════════════════════════════════════════════
# FASE 2 — Análise via Google Gemini
# ════════════════════════════════════════════════════════════
print("\n[2/4] Enviando para o Google Gemini (gemini-2.5-flash-lite)...")

client = genai.Client(api_key=GEMINI_API_KEY)
resposta = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=PROMPT_ANALISE + conteudo_gupy[:8000],
)
analise = resposta.text
print(f"      Análise gerada: {len(analise)} caracteres.")

# ════════════════════════════════════════════════════════════
# FASE 3 — Confirmação antes do envio
# ════════════════════════════════════════════════════════════
print("\n[3/4] Prévia do e-mail:")
print("=" * 60)
print(f"DESTINATÁRIO : {EMAIL_DESTINATARIO}")
print(f"ASSUNTO      : {EMAIL_ASSUNTO}")
print(f"ANEXO        : {Path(__file__).name}")
print("CORPO:")
print("-" * 60)
print(analise)
print("=" * 60)

confirmacao = input("\nEnviar o e-mail acima? (s/n): ").strip().lower()
if confirmacao != "s":
    print("Envio cancelado.")
    raise SystemExit(0)

# ════════════════════════════════════════════════════════════
# FASE 4 — Envio via Gmail SMTP com script anexado
# ════════════════════════════════════════════════════════════
print("\n[4/4] Enviando via Gmail SMTP...")

msg = MIMEMultipart()
msg["Subject"] = EMAIL_ASSUNTO
msg["From"]    = GMAIL_USER
msg["To"]      = EMAIL_DESTINATARIO

msg.attach(MIMEText(analise, "plain", "utf-8"))

# Anexar este próprio script ao e-mail
script_path = Path(__file__)
with open(script_path, "rb") as f:
    anexo = MIMEApplication(f.read(), Name=script_path.name)
    anexo["Content-Disposition"] = f'attachment; filename="{script_path.name}"'
    msg.attach(anexo)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    smtp.sendmail(GMAIL_USER, EMAIL_DESTINATARIO, msg.as_string())

print(f"\nE-mail enviado com sucesso para {EMAIL_DESTINATARIO}!")
print(f"Script '{script_path.name}' anexado ao e-mail.")
