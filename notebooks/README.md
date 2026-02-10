# Notebooks

This directory contains Jupyter Notebooks organized by module and week, used for exercises, exploratory data analysis, and projects in the DEVinHouse 2025 course.

## Prerequisites

Ensure you have the following installed:
```bash
pip install pandas numpy matplotlib seaborn scipy faker requests jupyter
```

## Subdirectories

- **M1S5/**: Module 1, Week 5 - Data import, exploration, and Pandas/NumPy operations
- **M1S6/**: Module 1, Week 6 - Clamed Data Insights project with machine learning
- **M2S2/**: Module 2, Week 2 - Advanced data cleaning and statistical analysis (Chipotle dataset + Sales data quality control)
- **study_notes/**: Supporting notebooks with study examples and practice exercises

## How to run

1. **Start Jupyter from project root:**
   ```bash
   # Ensure you're in the project root directory
   cd /path/to/data-analysis-devinhouse
   
   # Start Jupyter Lab (recommended)
   jupyter lab
   
   # Or Jupyter Notebook (classic)
   jupyter notebook
   ```

2. **Navigate to desired notebook** and execute cells sequentially

3. **Path references:** All notebooks use relative paths to access data files in `../data/` folder

## Data Dependencies

Notebooks rely on datasets in the `data/input/` directory:
- `clientes.csv`, `pedidos.csv`, `produtos.csv` - Business analysis data
- `healthcare_dataset.csv` - Medical insights analysis
- `chipotle_modificado.csv` - Restaurant chain data cleaning
- `sales_data_sample.csv` - Sales transactions for statistical analysis and outlier detection

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
