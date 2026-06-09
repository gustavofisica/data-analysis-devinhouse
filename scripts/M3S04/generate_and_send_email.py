"""
[M3S04] - Ex. 5 - Gerando o E-mail com Análise das Vagas

Fluxo:
  1. Lê o conteúdo da Gupy do clipboard (saída do Ex. 4)
  2. Envia para o Google Gemini e obtém análise das vagas
  3. Exibe o e-mail gerado e o salva em email_gerado.txt
     (para uso no Ex. 6 — envio)

Pré-requisitos:
  - Arquivo .env com GEMINI_API_KEY e EMAIL_DESTINATARIO
  - Chave gratuita em: https://aistudio.google.com/apikey
  - Ex. 4 executado (conteúdo da Gupy no clipboard)

Uso:
    python generate_and_send_email.py
"""

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_TXT = ROOT / "data" / "output" / "txt"

from google import genai
import pyperclip
from dotenv import load_dotenv
import os

# ── Carregar variáveis de ambiente ──────────────────────────────────────────
load_dotenv()

GEMINI_API_KEY     = os.getenv("GEMINI_API_KEY")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

for var, nome in [
    (GEMINI_API_KEY,     "GEMINI_API_KEY"),
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
# FASE 2 — Análise via Google Gemini
# ════════════════════════════════════════════════════════════
print("\nEnviando para o Google Gemini...")

client = genai.Client(api_key=GEMINI_API_KEY)

resposta = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=PROMPT_ANALISE + conteudo_gupy[:8000],
)

analise = resposta.text
print(f"Análise gerada ({len(analise)} caracteres).")

# ════════════════════════════════════════════════════════════
# FASE 3 — Exibir e salvar o e-mail gerado
# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print(f"DESTINATÁRIO : {EMAIL_DESTINATARIO}")
print(f"ASSUNTO      : {EMAIL_ASSUNTO}")
print("CORPO:")
print("-" * 60)
print(analise)
print("=" * 60)

saida = OUTPUT_TXT / "email_gerado.txt"
OUTPUT_TXT.mkdir(parents=True, exist_ok=True)
saida.write_text(
    f"DESTINATÁRIO: {EMAIL_DESTINATARIO}\n"
    f"ASSUNTO: {EMAIL_ASSUNTO}\n"
    f"{'=' * 60}\n"
    f"{analise}",
    encoding="utf-8",
)
print(f"\nE-mail salvo em: {saida}")
print("Execute o Ex. 6 (send_email.py) para enviar.")

