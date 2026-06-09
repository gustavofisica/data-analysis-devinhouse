"""
[M3S04] - Ex. 5 - Gerando e Preenchendo o E-mail Final

Fluxo:
  1. Lê o conteúdo da Gupy do clipboard (saída do Ex. 4)
  2. Envia para a Claude API e obtém análise das vagas
  3. Exibe o e-mail gerado para confirmação
  4. Envia via SMTP do Gmail (App Password)

Pré-requisitos:
  - Arquivo .env com ANTHROPIC_API_KEY, GMAIL_USER,
    GMAIL_APP_PASSWORD e EMAIL_DESTINATARIO
  - Ex. 4 executado (conteúdo da Gupy no clipboard)
  - App Password do Gmail gerada em:
    https://myaccount.google.com/apppasswords

Uso:
    python generate_and_send_email.py
"""

import smtplib
import textwrap
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import anthropic
import pyperclip
from dotenv import load_dotenv
import os

# ── Carregar variáveis de ambiente ──────────────────────────────────────────
load_dotenv()

ANTHROPIC_API_KEY  = os.getenv("ANTHROPIC_API_KEY")
GMAIL_USER         = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

for var, nome in [
    (ANTHROPIC_API_KEY,  "ANTHROPIC_API_KEY"),
    (GMAIL_USER,         "GMAIL_USER"),
    (GMAIL_APP_PASSWORD, "GMAIL_APP_PASSWORD"),
    (EMAIL_DESTINATARIO, "EMAIL_DESTINATARIO"),
]:
    if not var:
        raise EnvironmentError(f"Variável {nome} não encontrada. Configure o arquivo .env")

EMAIL_ASSUNTO = "[M3S04] Ex. 5 - Análise de Vagas Remotas - Gupy"

PROMPT_ANALISE = textwrap.dedent("""\
    Com base nas vagas abaixo extraídas da plataforma Gupy, faça um resumo \
    das principais oportunidades remotas disponíveis, destacando: cargo, \
    empresa, requisitos principais e diferenciais. \
    Apresente em formato de lista organizada.

    Vagas:
    """)

# ════════════════════════════════════════════════════════════
# FASE 1 — Ler conteúdo da Gupy do clipboard
# ════════════════════════════════════════════════════════════
conteudo_gupy = pyperclip.paste()
if not conteudo_gupy.strip():
    raise RuntimeError("Clipboard vazio. Execute o Ex. 4 (copy_page_content.py) primeiro.")

print(f"Conteúdo da Gupy lido do clipboard ({len(conteudo_gupy)} caracteres).")

# ════════════════════════════════════════════════════════════
# FASE 2 — Análise via Claude API
# ════════════════════════════════════════════════════════════
print("\n[1/2] Enviando para a Claude API...")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

mensagem = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": PROMPT_ANALISE + conteudo_gupy[:8000],
        }
    ],
)

analise = mensagem.content[0].text
print(f"Análise gerada ({len(analise)} caracteres).")

# ════════════════════════════════════════════════════════════
# FASE 3 — Confirmação antes do envio
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print(f"DESTINATÁRIO : {EMAIL_DESTINATARIO}")
print(f"ASSUNTO      : {EMAIL_ASSUNTO}")
print("CORPO:")
print("-" * 60)
print(analise)
print("=" * 60)

resposta = input("\nEnviar o e-mail acima? (s/n): ").strip().lower()
if resposta != "s":
    print("Envio cancelado.")
    exit(0)

# ════════════════════════════════════════════════════════════
# FASE 4 — Envio via SMTP
# ════════════════════════════════════════════════════════════
print("\n[2/2] Enviando e-mail via Gmail SMTP...")

msg = MIMEMultipart("alternative")
msg["Subject"] = EMAIL_ASSUNTO
msg["From"]    = GMAIL_USER
msg["To"]      = EMAIL_DESTINATARIO
msg.attach(MIMEText(analise, "plain", "utf-8"))

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    smtp.sendmail(GMAIL_USER, EMAIL_DESTINATARIO, msg.as_string())

print("E-mail enviado com sucesso!")
