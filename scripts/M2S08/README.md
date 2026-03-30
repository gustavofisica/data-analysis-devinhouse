# M2S08 - Dashboard de Vendas (Streamlit)

Dashboard interativo desenvolvido com Streamlit para os exercícios da semana 8 do Módulo 2 do DEVinHouse 2025.

## Exercícios Implementados

| Exercício | Componente | Localização no dashboard |
|---|---|---|
| Ex. 1 | Scorecard com total de vendas em R$ | Painel superior (4 métricas) |
| Ex. 2 | Gráfico de barras — evolução mensal | Coluna principal central |
| Ex. 3 | Filtros de controle (sidebar) + filtro na base | Sidebar esquerda |
| Ex. 4 | Campo calculado `mes_venda` para agrupamento correto | Dimensão do gráfico de barras |

## Fonte de Dados

```
data/input/csv/base_vendas_luis_gustavo_de_matos_dos_santos.csv
```

- 10.000 registros de vendas
- Período: 2025 (março a dezembro)
- Campos principais: `valor_total`, `data_venda`, `categoria`, `estado`, `produto`

## Como Executar

### Pré-requisitos

```bash
# Ativar o ambiente virtual do projeto
source .venv/bin/activate

# Instalar dependências (caso ainda não instaladas)
pip install streamlit plotly
```

### Rodar o Dashboard

```bash
# A partir da raiz do projeto
streamlit run scripts/M2S08/dashboard.py
```

O dashboard abrirá automaticamente em `http://localhost:8501`.

## Observações Técnicas

### Ex. 3 — Dois tipos de filtro

- **Filtro de controle** (sidebar): multiselect de `categoria`, `estado`, `produto` e seletor de período — manipulados pelo usuário em tempo real
- **Filtro na base de dados**: aplicado na carga (`valor_total > 0`), equivalente a um filtro permanente na fonte de dados do Looker Studio

### Ex. 4 — Campo calculado de data

```python
df["mes_venda"] = df["data_venda"].dt.to_period("M").astype(str)
# Resultado: "2025-03", "2025-04", ..., "2025-12"
```

Garante ordenação cronológica correta no eixo X do gráfico, equivalente ao campo calculado `FORMAT_DATETIME("%Y-%m", data_venda)` do Looker Studio.

## Entrega no Looker Studio

Link do dashboard (Looker Studio): _a ser preenchido após configuração_

> O dashboard Streamlit serve como referência visual e evidência técnica no repositório.
> A entrega oficial do exercício é feita via Looker Studio conforme orientação do curso.
