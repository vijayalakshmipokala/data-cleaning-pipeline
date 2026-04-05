# 📊 Data Cleaning Pipeline for Sales Data

## Project Overview
Raw sales data is often inconsistent and not ready for analysis.  
This project builds a structured **data cleaning pipeline** to transform messy data into a clean, reliable dataset.

---

## Objective
- Clean raw data  
- Ensure data quality  
- Prepare dataset for analysis / ML  

---

## Project Structure

data-cleaning-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── cleaned_sales_data.csv
│
├── notebooks/
│   └── 1_exploration.ipynb
│
├── src/
│   └── cleaning.py
│
├── reports/
│   └── cleaning_report.md
│
├── requirements.txt
└── README.md

---

## Key Features
- Removed duplicate records (17 rows)
- Standardized column names
- Converted postal code to categorical format
- Handled outliers (top 1% removed)
- Performed validation checks

---

## Data Cleaning Steps
1. Data exploration  
2. Duplicate removal  
3. Column name standardization  
4. Data type correction  
5. Outlier removal  
6. Data validation  

---

## Results
- Original dataset: 9994 rows  
- Cleaned dataset: 9877 rows  
- No duplicate data  
- Clean and consistent structure  

---

## Key Insight
~18% of transactions resulted in negative profit, indicating potential business inefficiencies.

---

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

