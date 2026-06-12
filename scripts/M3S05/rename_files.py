"""
[M3S05] - Ex. 3 - Renomeação Automática de Arquivos

Renomeia automaticamente arquivos em um diretório do repositório,
aplicando um padrão consistente:
    {YYYYMMDD}_{nome_em_snake_case}.{extensão}

Funcionalidades:
    - Converte nomes de arquivo para snake_case
    - Adiciona prefixo com a data atual
    - Preview antes de aplicar (modo interativo)
    - Modo dry-run com flag --dry-run
    - Log de todas as renomeações

Uso:
    python scripts/M3S05/rename_files.py              # interativo
    python scripts/M3S05/rename_files.py --dry-run    # apenas preview
    python scripts/M3S05/rename_files.py --auto       # sem confirmação
"""

import re
import sys
from datetime import datetime
from pathlib import Path

# ── Caminhos ─────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
DIRETORIO_ALVO = ROOT / "data" / "output" / "xlsx"


def para_snake_case(nome: str) -> str:
    """Converte um nome de arquivo para snake_case.

    Remove acentos comuns, substitui espaços e hífens por underscores,
    remove caracteres especiais e converte para minúsculas.

    Args:
        nome: nome original do arquivo (sem extensão).

    Returns:
        Nome em snake_case.
    """
    # Substituições de acentos comuns em português
    substituicoes = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "ô": "o", "õ": "o",
        "ú": "u", "ü": "u",
        "ç": "c",
        "Á": "A", "À": "A", "Ã": "A", "Â": "A",
        "É": "E", "Ê": "E",
        "Í": "I",
        "Ó": "O", "Ô": "O", "Õ": "O",
        "Ú": "U", "Ü": "U",
        "Ç": "C",
    }
    for orig, subst in substituicoes.items():
        nome = nome.replace(orig, subst)

    # Converter CamelCase para separação com underscore
    nome = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", nome)

    # Substituir espaços, hífens e pontos por underscore
    nome = re.sub(r"[\s\-\.]+", "_", nome)

    # Remover caracteres especiais (manter apenas alfanuméricos e underscore)
    nome = re.sub(r"[^a-zA-Z0-9_]", "", nome)

    # Remover underscores duplicados e das extremidades
    nome = re.sub(r"_+", "_", nome).strip("_")

    return nome.lower()


def gerar_renomeacoes(diretorio: Path, prefixo_data: str) -> list[dict]:
    """Gera a lista de renomeações planejadas.

    Args:
        diretorio: caminho do diretório com os arquivos.
        prefixo_data: prefixo de data no formato YYYYMMDD.

    Returns:
        Lista de dicts com 'original', 'novo', 'path_original', 'path_novo'.
    """
    renomeacoes = []

    for arquivo in sorted(diretorio.iterdir()):
        # Ignorar diretórios e arquivos ocultos
        if arquivo.is_dir() or arquivo.name.startswith("."):
            continue

        # Ignorar README.md
        if arquivo.name.lower() == "readme.md":
            continue

        nome_sem_ext = arquivo.stem
        extensao = arquivo.suffix

        # Já tem prefixo de data? (padrão YYYYMMDD_)
        if re.match(r"^\d{8}_", nome_sem_ext):
            continue  # Pular arquivos já renomeados

        novo_nome = f"{prefixo_data}_{para_snake_case(nome_sem_ext)}{extensao}"

        renomeacoes.append({
            "original": arquivo.name,
            "novo": novo_nome,
            "path_original": arquivo,
            "path_novo": arquivo.parent / novo_nome,
        })

    return renomeacoes


def exibir_preview(renomeacoes: list[dict]) -> None:
    """Exibe preview das renomeações planejadas.

    Args:
        renomeacoes: lista de renomeações gerada por gerar_renomeacoes().
    """
    if not renomeacoes:
        print("  Nenhum arquivo para renomear.")
        return

    largura_orig = max(len(r["original"]) for r in renomeacoes)

    for r in renomeacoes:
        print(f"  {r['original']:<{largura_orig}}  →  {r['novo']}")


def aplicar_renomeacoes(renomeacoes: list[dict]) -> int:
    """Aplica as renomeações no sistema de arquivos.

    Args:
        renomeacoes: lista de renomeações a aplicar.

    Returns:
        Número de arquivos renomeados com sucesso.
    """
    sucesso = 0
    for r in renomeacoes:
        try:
            r["path_original"].rename(r["path_novo"])
            print(f"  ✓ {r['original']} → {r['novo']}")
            sucesso += 1
        except OSError as e:
            print(f"  ✗ Erro ao renomear {r['original']}: {e}")
    return sucesso


# ═══════════════════════════════════════════════════════════════
# Execução principal
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    auto = "--auto" in sys.argv

    print("=" * 70)
    print("[M3S05] Ex. 3 - Renomeação Automática de Arquivos")
    print("=" * 70)

    if not DIRETORIO_ALVO.exists():
        print(f"\nDiretório não encontrado: {DIRETORIO_ALVO}")
        print("Criando diretório...")
        DIRETORIO_ALVO.mkdir(parents=True, exist_ok=True)

    prefixo = datetime.now().strftime("%Y%m%d")
    print(f"\nDiretório: {DIRETORIO_ALVO}")
    print(f"Prefixo de data: {prefixo}")
    print(f"Modo: {'DRY-RUN (apenas preview)' if dry_run else 'EXECUÇÃO'}")

    renomeacoes = gerar_renomeacoes(DIRETORIO_ALVO, prefixo)

    print(f"\nArquivos para renomear: {len(renomeacoes)}")
    print("-" * 70)
    exibir_preview(renomeacoes)
    print("-" * 70)

    if dry_run or not renomeacoes:
        print("\nPreview concluído. Nenhuma alteração foi feita.")
    elif auto:
        print("\nAplicando renomeações (modo automático)...")
        total = aplicar_renomeacoes(renomeacoes)
        print(f"\n{total}/{len(renomeacoes)} arquivos renomeados com sucesso.")
    else:
        resposta = input("\nAplicar as renomeações acima? (s/n): ").strip().lower()
        if resposta == "s":
            total = aplicar_renomeacoes(renomeacoes)
            print(f"\n{total}/{len(renomeacoes)} arquivos renomeados com sucesso.")
        else:
            print("\nOperação cancelada.")

    print("\n" + "=" * 70)
    print("Concluído!")
    print("=" * 70)
