# Module 2 - Week 2 Exercises

This directory contains Jupyter Notebooks for Module 2, Week 2 of the DEVinHouse 2025 course, focusing on advanced data cleaning and manipulation techniques.

## Exercise List

### 1. **chipotle_data_cleaning.ipynb**
   - **Objective**: Data cleaning and preparation of Chipotle restaurant dataset
   - **Topics covered**:
     - Data quality assessment
     - Handling missing values
     - Data type conversions
     - Price data cleaning (removing '$' symbols, converting to numeric)
     - Duplicate detection and removal
     - Data standardization
     - Exploratory data analysis after cleaning

## Dataset

- **Source**: Chipotle Mexican Grill orders dataset
- **File**: `../../data/input/csv/chipotle_modificado.csv`
- **Description**: Real-world restaurant order data requiring comprehensive cleaning

## Prerequisites

Ensure you have the necessary libraries installed:
```bash
pip install pandas numpy matplotlib seaborn
```

## Key Learning Outcomes

- Advanced data cleaning techniques
- Real-world data quality assessment
- Data preprocessing best practices
- Working with messy financial data (prices with special characters)
- Data validation and quality assurance

## How to run

1. **Start Jupyter from project root:**
   ```bash
   cd /path/to/data-analysis-devinhouse
   jupyter lab
   ```

2. **Navigate to this notebook** and execute cells sequentially

3. **Data dependency**: Requires `chipotle_modificado.csv` in `../../data/input/csv/`

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)