# 📊 Data Cleaning Pipeline for Sales Data

## 📌 Project Overview
Raw sales data is often inconsistent and not ready for analysis.  
This project builds a structured data cleaning pipeline to transform messy data into a clean, reliable dataset.

---

## 🎯 Objective
- Clean raw data  
- Ensure data quality  
- Prepare dataset for analysis / ML  

---

## 🗂️ Project Structure

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

## ⚙️ Key Features
- Removed duplicate records (17 rows)
- Standardized column names
- Converted postal code to categorical format
- Handled outliers (top 1% removed)
- Performed validation checks

---

## 📊 Data Cleaning Steps
1. Data exploration  
2. Duplicate removal  
3. Column name standardization  
4. Data type correction  
5. Outlier removal  
6. Data validation  

---

## 📈 Results
- Original dataset: 9994 rows  
- Cleaned dataset: 9877 rows  
- No duplicate data  
- Clean and consistent structure  

---

## 🔍 Key Insight
Approximately 18% of transactions resulted in negative profit, indicating potential inefficiencies in pricing or discount strategy.

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## 🚀 How to Run

git clone https://github.com/vijayalakshmipokala/data-cleaning-pipeline.git  
cd data-cleaning-pipeline  
pip install -r requirements.txt  

Run notebook:
notebooks/1_exploration.ipynb

---

## 📁 Output
data/processed/cleaned_sales_data.csv

---

## 📌 Future Improvements
- Build dashboard (Power BI / Tableau)  
- Perform SQL analysis  
- Apply machine learning  

---

## 👤 Author
Vijaya Lakshmi Pokala