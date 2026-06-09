"""
[M3S04] - Ex. 6 - Enviando o E-mail Final

Lê o e-mail gerado pelo Ex. 5 (email_gerado.txt), exibe para confirmação
e envia via Gmail SMTP.

Pré-requisitos:
  - Arquivo .env com GMAIL_USER e GMAIL_APP_PASSWORD
  - App Password do Gmail gerada em:
    https://myaccount.google.com/apppasswords
  - Ex. 5 executado (email_gerado.txt presente nesta pasta)

Uso:
    python send_email.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv
import os

# ── Carregar variáveis de ambiente ──────────────────────────────────────────
load_dotenv()

GMAIL_USER         = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

for var, nome in [
    (GMAIL_USER,         "GMAIL_USER"),
    (GMAIL_APP_PASSWORD, "GMAIL_APP_PASSWORD"),
]:
    if not var:
        raise EnvironmentError(f"Variável {nome} não encontrada. Configure o arquivo .env")

# ════════════════════════════════════════════════════════════
# FASE 1 — Ler e-mail gerado pelo Ex. 5
# ════════════════════════════════════════════════════════════
arquivo = Path(__file__).parent / "email_gerado.txt"
if not arquivo.exists():
    raise FileNotFoundError("email_gerado.txt não encontrado. Execute o Ex. 5 primeiro.")

conteudo = arquivo.read_text(encoding="utf-8")

# Extrair cabeçalhos salvos pelo Ex. 5
linhas = conteudo.splitlines()
destinatario = linhas[0].replace("DESTINATÁRIO: ", "").strip()
assunto      = linhas[1].replace("ASSUNTO: ", "").strip()
corpo        = "\n".join(linhas[3:])   # pula separador "==="

# ════════════════════════════════════════════════════════════
# FASE 2 — Confirmação antes do envio
# ════════════════════════════════════════════════════════════
print("=" * 60)
print(f"DESTINATÁRIO : {destinatario}")
print(f"ASSUNTO      : {assunto}")
print("CORPO:")
print("-" * 60)
print(corpo)
print("=" * 60)

confirmacao = input("\nEnviar o e-mail acima? (s/n): ").strip().lower()
if confirmacao != "s":
    print("Envio cancelado.")
    exit(0)

# ════════════════════════════════════════════════════════════
# FASE 3 — Envio via Gmail SMTP
# ════════════════════════════════════════════════════════════
print("\nEnviando via Gmail SMTP...")

msg = MIMEMultipart("alternative")
msg["Subject"] = assunto
msg["From"]    = GMAIL_USER
msg["To"]      = destinatario
msg.attach(MIMEText(corpo, "plain", "utf-8"))

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    smtp.sendmail(GMAIL_USER, destinatario, msg.as_string())

print("E-mail enviado com sucesso!")
