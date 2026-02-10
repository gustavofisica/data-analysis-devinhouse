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

### 2. **sales_data_checkup.ipynb** ✨ NEW
   - **Objective**: Comprehensive sales data quality control and validation
   - **Topics covered**:
     - Dataset check-up with `.info()` analysis
     - Data type conversion (ORDERNUMBER → object)
     - Null value auditing and validation
     - Financial data manipulation with mock data experiments
     - Statistical outlier detection with IQR method
     - Z-Score analysis for identifying "Whale" customers (VIP clients)
     - Data visualization with boxplot analysis

## Datasets

- **Source 1**: Chipotle Mexican Grill orders dataset
  - **File**: `../../data/input/csv/chipotle_modificado.csv`
  - **Description**: Real-world restaurant order data requiring comprehensive cleaning

- **Source 2**: Sales transaction dataset
  - **File**: `../../data/input/csv/sales_data_sample.csv`
  - **Description**: Sales transactions with customer, product, and financial data for statistical analysis

## Prerequisites

Ensure you have the necessary libraries installed:
```bash
pip install pandas numpy matplotlib seaborn scipy
```

## Key Learning Outcomes

### Data Quality & Validation
- Advanced data cleaning techniques
- Real-world data quality assessment  
- Data preprocessing best practices
- Working with messy financial data (prices with special characters)
- Data type conversion and optimization strategies

### Statistical Analysis & Outlier Detection
- Interquartile Range (IQR) method for outlier detection
- Z-Score analysis for extreme value identification
- Statistical validation of business data patterns
- VIP customer identification using statistical criteria

### Data Manipulation & Experimentation
- Mock data insertion and cleanup strategies
- Null value auditing and pattern recognition
- DataFrame manipulation for quality control
- Financial data validation techniques

### Data Visualization
- Boxplot interpretation for outlier analysis
- Statistical visualization best practices
- Seaborn and Matplotlib integration

## How to run

1. **Start Jupyter from project root:**
   ```bash
   cd /path/to/data-analysis-devinhouse
   jupyter lab
   ```

2. **Navigate to desired notebook** and execute cells sequentially

3. **Data dependencies:** 
   - `chipotle_data_cleaning.ipynb` requires `chipotle_modificado.csv` in `../../data/input/csv/`
   - `sales_data_checkup.ipynb` requires `sales_data_sample.csv` in `../../data/input/csv/`

4. **Notebook execution order:** Both notebooks are independent and can be run in any order

## Exercise Progression

**Recommended learning path:**
1. Start with `chipotle_data_cleaning.ipynb` for fundamental data cleaning concepts
2. Progress to `sales_data_checkup.ipynb` for advanced statistical analysis and quality control techniques

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)