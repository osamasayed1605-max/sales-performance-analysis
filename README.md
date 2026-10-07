# Sales Performance Analysis

## Project Overview

This project analyzes sales performance data using Python and Pandas.

The main objective is to clean raw sales data, analyze employee, department, product, and monthly performance, and generate useful business insights.

The final results are exported into a structured Excel report containing multiple analysis sheets.

## Tools Used

- Python
- Pandas
- Microsoft Excel
- Visual Studio Code

## Data Cleaning

The dataset was cleaned before analysis by:

- Removing duplicate orders.
- Converting the order date to datetime format.
- Cleaning text columns and removing extra spaces.
- Handling missing discount values.
- Handling missing working hours.
- Filling missing employee names using employee codes.
- Handling missing city values.

## Analysis Performed

The analysis includes:

- Total and average sales analysis.
- Employee performance analysis.
- Department performance analysis.
- Product sales and quantity analysis.
- Category, sales channel, and city analysis.
- Monthly sales performance.
- Top 10 orders by sales.
- Sales classification into High and Normal orders.

## Business Insights

- Youssef Adel achieved the highest total sales with 39,225, while Omar Khaled recorded the highest sales per working hour. This shows that total sales performance and hourly productivity should be evaluated separately.

- Healthy Box was the top-performing product, generating 69,306.30 in total sales from 184 units sold, making it a key contributor to overall sales performance.

- August was the strongest sales month, generating 120,521.30 in total sales, making it the highest-performing month in the analyzed period.

- Cairo was the highest-performing city, generating 102,527 in total sales, making it the strongest geographical market in the dataset.

- Marketplace was the highest-performing sales channel, generating 80,601 in total sales, making it the leading channel by revenue.

## Project Files

- `sales_analysis.py` - Python script used for data cleaning and analysis.
- `Sales_Performance_Portfolio_Project.xlsx` - Raw dataset used in the project.
- `Sales_Final_Report.xlsx` - Final Excel report containing the cleaned data and analysis results.
- `README.md` - Project documentation.