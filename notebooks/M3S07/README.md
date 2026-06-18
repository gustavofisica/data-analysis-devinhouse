# M3S07 — Mini-Projeto: Análise Preditiva de Custos Médicos

Mini-Projeto do Módulo 3, Semana 7 — DEVinHouse [Clamed] V4. Análise exploratória completa e modelagem preditiva dos custos médicos individuais do dataset *Medical Cost Personal Datasets* (Kaggle).

## Notebook

| Arquivo | Descrição |
|---|---|
| `medical_cost_prediction.ipynb` | Pipeline completo: EDA, limpeza, feature engineering, treinamento e comparação de 5 modelos (Linear, Linear + interação, Árvore, Random Forest, Gradient Boosting), validação cruzada k-fold, GridSearchCV e simulação de perfis típicos. |

## Base de dados utilizada

`data/input/csv/insurance.csv` — 1.338 registros, 7 colunas (`age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`).
Fonte: [Kaggle — Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance).

## Estrutura do notebook

1. Importação de bibliotecas e carregamento dos dados
2. Exploração inicial e qualidade dos dados (nulos, duplicatas, tipos)
3. Tradução e padronização (renomeação de colunas e categorias)
4. Análise estatística descritiva (tendência central, dispersão, forma)
5. Tratamento de outliers — decisão metodológica (caracterização do perfil clínico)
6. Análise demográfica (sexo, faixa etária, região)
7. Análise de custos por variáveis categóricas (univariada)
8. Correlações entre variáveis numéricas (Pearson)
9. Visualizações comparativas e cruzamentos: interação `Fumante × IMC`
10. Regressão Linear Múltipla (baseline)
11. Comparação com Árvore de Decisão + simulação de 5 perfis típicos
12. Extensões: feature engineering (`Fumante_Obeso`), Árvore visualizada, k-fold CV, ensembles (RF, GB), GridSearchCV e simulação dos perfis com todos os modelos
13. Conclusão e interpretação dos resultados

## Resultado principal

Modelo recomendado: **Regressão Linear Múltipla + `Fumante_Obeso`** com R² = 0,9057, MAE = USD 2.392, RMSE = USD 4.163 — superior a Random Forest e Gradient Boosting com a vantagem da interpretabilidade direta dos coeficientes.

## Dependências

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```
