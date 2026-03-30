"""
M2S08 - Dashboard de Vendas
DEVinHouse 2025

Exercicios implementados:
- Ex. 1: Scorecard com total de vendas em R$
- Ex. 2: Grafico de barras com evolucao mensal de vendas
- Ex. 3: Filtros de controle (sidebar) e filtro na base de dados
- Ex. 4: Campo calculado de data para agrupamento correto por mes
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuracao da pagina
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="M2S08 - Dashboard de Vendas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Estilo customizado
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        font-size: 0.95rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #495057;
        border-left: 4px solid #1f77b4;
        padding-left: 0.6rem;
        margin-bottom: 1rem;
    }
    .exercise-tag {
        background-color: #e8f4f8;
        color: #1f77b4;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        font-size: 0.78rem;
        font-weight: 600;
    }
    [data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Carregamento dos dados
# ---------------------------------------------------------------------------
DATA_PATH = (
    Path(__file__).parent.parent.parent
    / "data/input/csv/base_vendas_luis_gustavo_de_matos_dos_santos.csv"
)


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["data_venda"])
    # Ex. 3 - Filtro na base de dados: remove registros invalidos
    df = df[df["valor_total"] > 0].copy()
    # Ex. 4 - Campo calculado: mes_venda no formato YYYY-MM para ordem cronologica correta
    df["mes_venda"] = df["data_venda"].dt.to_period("M").astype(str)
    return df


df_raw = load_data(DATA_PATH)

# ---------------------------------------------------------------------------
# Sidebar - Ex. 3: Filtros de controle
# ---------------------------------------------------------------------------
st.sidebar.markdown("## Filtros")
st.sidebar.caption("Ex. 3 — Filtros de controle")

st.sidebar.markdown("---")

categorias_disponiveis = sorted(df_raw["categoria"].unique())
categorias_sel = st.sidebar.multiselect(
    "Categoria",
    options=categorias_disponiveis,
    default=categorias_disponiveis,
    help="Filtre por categoria de produto",
)

estados_disponiveis = sorted(df_raw["estado"].unique())
estados_sel = st.sidebar.multiselect(
    "Estado",
    options=estados_disponiveis,
    default=estados_disponiveis,
    help="Filtre por estado de venda",
)

produtos_disponiveis = sorted(df_raw["produto"].unique())
produtos_sel = st.sidebar.multiselect(
    "Produto",
    options=produtos_disponiveis,
    default=produtos_disponiveis,
    help="Filtre por tipo de produto",
)

periodo_min = df_raw["data_venda"].min().date()
periodo_max = df_raw["data_venda"].max().date()
periodo_sel = st.sidebar.date_input(
    "Periodo",
    value=(periodo_min, periodo_max),
    min_value=periodo_min,
    max_value=periodo_max,
    help="Filtre por periodo de venda",
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small>**Filtro na base de dados** (Ex. 3):<br>"
    "Registros com `valor_total ≤ 0` excluidos automaticamente na carga.</small>",
    unsafe_allow_html=True,
)

# Aplica filtros de controle
df = df_raw.copy()

if categorias_sel:
    df = df[df["categoria"].isin(categorias_sel)]
if estados_sel:
    df = df[df["estado"].isin(estados_sel)]
if produtos_sel:
    df = df[df["produto"].isin(produtos_sel)]
if len(periodo_sel) == 2:
    df = df[
        (df["data_venda"].dt.date >= periodo_sel[0])
        & (df["data_venda"].dt.date <= periodo_sel[1])
    ]

# ---------------------------------------------------------------------------
# Cabecalho
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="main-title">📊 Dashboard de Vendas</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="subtitle">DEVinHouse 2025 &mdash; M2S08 | '
    "Luis Gustavo de Matos dos Santos</p>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Ex. 1 - Scorecard com total de vendas em R$
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="section-header">'
    '<span class="exercise-tag">Ex. 1</span>&nbsp; Scorecard de Vendas'
    "</p>",
    unsafe_allow_html=True,
)

total_vendas = df["valor_total"].sum()
qtd_registros = len(df)
ticket_medio = total_vendas / qtd_registros if qtd_registros > 0 else 0
qtd_clientes = df["cliente"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total de Vendas",
        value=f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        help="Soma de valor_total — Ex. 1",
    )
with col2:
    st.metric(
        label="Quantidade de Pedidos",
        value=f"{qtd_registros:,}".replace(",", "."),
        help="Total de registros apos filtros",
    )
with col3:
    st.metric(
        label="Ticket Medio",
        value=f"R$ {ticket_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        help="Media de valor_total por pedido",
    )
with col4:
    st.metric(
        label="Clientes Unicos",
        value=f"{qtd_clientes:,}".replace(",", "."),
        help="Numero de clientes distintos",
    )

st.markdown("---")

# ---------------------------------------------------------------------------
# Ex. 2 e Ex. 4 - Grafico de barras: evolucao mensal (com campo calculado)
# ---------------------------------------------------------------------------
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown(
        '<p class="section-header">'
        '<span class="exercise-tag">Ex. 2 + Ex. 4</span>&nbsp; '
        "Evolucao Mensal de Vendas"
        "</p>",
        unsafe_allow_html=True,
    )

    if df.empty:
        st.warning("Nenhum dado disponivel com os filtros selecionados.")
    else:
        # Ex. 4: usa mes_venda (campo calculado) como dimensao
        df_mensal = (
            df.groupby("mes_venda", as_index=False)["valor_total"]
            .sum()
            .sort_values("mes_venda")
        )

        fig = px.bar(
            df_mensal,
            x="mes_venda",
            y="valor_total",
            labels={
                "mes_venda": "Mes",
                "valor_total": "Total de Vendas (R$)",
            },
            color_discrete_sequence=["#1f77b4"],
            text_auto=".2s",
        )

        fig.update_layout(
            xaxis_title="Mes",
            yaxis_title="Total de Vendas (R$)",
            plot_bgcolor="white",
            paper_bgcolor="white",
            yaxis=dict(gridcolor="#e9ecef"),
            xaxis=dict(tickangle=-45),
            margin=dict(t=30, b=40),
            height=380,
        )

        fig.update_traces(
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>R$ %{y:,.2f}<extra></extra>",
        )

        st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Ex. 4: dimensao usa campo calculado `mes_venda = data_venda.dt.to_period('M')` "
        "para garantir ordem cronologica correta."
    )

with col_right:
    st.markdown(
        '<p class="section-header">'
        '<span class="exercise-tag">Distribuicoes</span>'
        "</p>",
        unsafe_allow_html=True,
    )

    if not df.empty:
        # Vendas por categoria
        df_cat = (
            df.groupby("categoria", as_index=False)["valor_total"]
            .sum()
            .sort_values("valor_total", ascending=False)
        )
        fig_cat = px.pie(
            df_cat,
            names="categoria",
            values="valor_total",
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig_cat.update_layout(
            margin=dict(t=10, b=10, l=10, r=10),
            height=180,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.3),
        )
        fig_cat.update_traces(
            hovertemplate="<b>%{label}</b><br>R$ %{value:,.2f}<extra></extra>"
        )
        st.caption("Vendas por Categoria")
        st.plotly_chart(fig_cat, use_container_width=True)

        # Vendas por estado
        df_est = (
            df.groupby("estado", as_index=False)["valor_total"]
            .sum()
            .sort_values("valor_total", ascending=False)
        )
        fig_est = px.bar(
            df_est,
            x="estado",
            y="valor_total",
            color_discrete_sequence=["#2ca02c"],
            labels={"estado": "Estado", "valor_total": "Total (R$)"},
        )
        fig_est.update_layout(
            margin=dict(t=10, b=10),
            height=180,
            plot_bgcolor="white",
            yaxis=dict(gridcolor="#e9ecef"),
            showlegend=False,
        )
        fig_est.update_traces(
            hovertemplate="<b>%{x}</b><br>R$ %{y:,.2f}<extra></extra>"
        )
        st.caption("Vendas por Estado")
        st.plotly_chart(fig_est, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Tabela de dados filtrados
# ---------------------------------------------------------------------------
with st.expander("Ver dados filtrados"):
    st.dataframe(
        df[["id_venda", "data_venda", "mes_venda", "cliente", "estado",
            "produto", "categoria", "quantidade", "valor_unitario", "valor_total"]]
        .sort_values("data_venda"),
        use_container_width=True,
        hide_index=True,
    )
    st.caption(f"{len(df):,} registros exibidos".replace(",", "."))

# ---------------------------------------------------------------------------
# Rodape
# ---------------------------------------------------------------------------
st.markdown(
    "<small style='color:#adb5bd;'>Fonte: base_vendas_luis_gustavo_de_matos_dos_santos.csv "
    "| DEVinHouse 2025 M2S08</small>",
    unsafe_allow_html=True,
)
