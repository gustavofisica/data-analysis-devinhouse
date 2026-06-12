"""
[M3S05] - Ex. 1 - Leitura de Planilha com Pandas

Lê a planilha de amostra da tabela CMED (Câmara de Regulação do Mercado
de Medicamentos) e cria um DataFrame para análise exploratória básica.

A planilha contém dados públicos de preços de medicamentos registrados
na ANVISA, incluindo substância, produto, apresentação, laboratório,
preço fábrica (PF) e preço máximo ao consumidor (PMC).

Fonte dos dados: Tabela CMED / ANVISA (amostra ilustrativa)

Uso:
    python scripts/M3S05/read_cmed_spreadsheet.py
"""

from pathlib import Path

import pandas as pd

# ── Caminhos ─────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
PLANILHA = ROOT / "data" / "input" / "xlsx" / "medicamentos_cmed_amostra.xlsx"

# ════════════════════════════════════════════════════════════
# FASE 1 — Leitura da planilha
# ════════════════════════════════════════════════════════════
print("=" * 70)
print("[M3S05] Ex. 1 - Leitura de Planilha CMED com Pandas")
print("=" * 70)

if not PLANILHA.exists():
    raise FileNotFoundError(f"Planilha não encontrada: {PLANILHA}")

df = pd.read_excel(PLANILHA, sheet_name="CMED_Amostra", engine="openpyxl")

print(f"\nArquivo: {PLANILHA.name}")
print(f"Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")

# ════════════════════════════════════════════════════════════
# FASE 2 — Visão geral do DataFrame
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 70)
print("PRIMEIRAS 10 LINHAS (.head(10)):")
print("-" * 70)
print(df.head(10).to_string(index=False))

print("\n" + "-" * 70)
print("INFORMAÇÕES DO DATAFRAME (.info()):")
print("-" * 70)
df.info()

print("\n" + "-" * 70)
print("ESTATÍSTICAS NUMÉRICAS (.describe()):")
print("-" * 70)
print(df.describe().to_string())

# ════════════════════════════════════════════════════════════
# FASE 3 — Análise básica: contagens e rankings
# ════════════════════════════════════════════════════════════
print("\n" + "-" * 70)
print("CONTAGEM POR TIPO DE MEDICAMENTO:")
print("-" * 70)
print(df["TIPO"].value_counts().to_string())

print("\n" + "-" * 70)
print("CONTAGEM POR LABORATÓRIO (top 10):")
print("-" * 70)
print(df["LABORATÓRIO"].value_counts().head(10).to_string())

print("\n" + "-" * 70)
print("MEDICAMENTOS MAIS CAROS (PMC - top 5):")
print("-" * 70)
top_caros = df.nlargest(5, "PMC_18%")[["PRODUTO", "SUBSTÂNCIA", "PMC_18%", "LABORATÓRIO"]]
print(top_caros.to_string(index=False))

print("\n" + "-" * 70)
print("MEDICAMENTOS MAIS BARATOS (PMC - top 5):")
print("-" * 70)
top_baratos = df.nsmallest(5, "PMC_18%")[["PRODUTO", "SUBSTÂNCIA", "PMC_18%", "LABORATÓRIO"]]
print(top_baratos.to_string(index=False))

print("\n" + "-" * 70)
print("PREÇO MÉDIO POR TIPO:")
print("-" * 70)
preco_medio = df.groupby("TIPO")["PMC_18%"].mean().round(2)
print(preco_medio.to_string())

print("\n" + "=" * 70)
print("Leitura e análise concluídas com sucesso!")
print("=" * 70)
