# Data Cleaning Report

## Dataset Overview
- Rows: 9994 → 9877 after cleaning
- Columns: 13

## Issues Identified
- 17 duplicate rows
- Inconsistent column naming
- Postal code treated as numeric
- Extreme outliers in sales
- Negative profit values

## Cleaning Steps
- Removed duplicate rows
- Standardized column names
- Converted postal code to string
- Removed top 1% sales outliers

## Key Insights
- ~18% of transactions resulted in loss
- Dataset is now clean and analysis-ready