# Online Retail Analytics

An end-to-end data analytics project using Python, MySQL, and Power BI to analyze online retail transactions, sales performance, customer behavior, product performance, and geographical sales.

## Project Overview

This project uses the **Online Retail II** dataset, which contains transaction-level sales data from a UK-based online retail business.

The dataset includes information such as:

- Invoice number
- Product code
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

The project follows a complete analytics workflow:

**Raw Data → Python Data Cleaning → MySQL Analysis → Power BI Dashboard**

## Tools & Technologies

- **Python** – Data profiling, cleaning, transformation and feature creation
- **Pandas** – Data manipulation and analysis
- **MySQL** – Data storage and SQL-based business analysis
- **Power BI** – Interactive dashboard and data visualization
- **Excel** – Initial data source and data review

## Dataset

The project uses the publicly available **Online Retail II** dataset.

The original dataset contains approximately **1.07 million transaction records** across two periods:

- 2009–2010
- 2010–2011

After data cleaning and duplicate removal, the project contains **1,033,036 cleaned records**.

A separate sales dataset containing **1,003,484 records** was created for the main dashboard and SQL analysis.

## Data Cleaning & Preparation

Python was used to prepare the dataset before analysis.

Key steps included:

1. Loading both yearly datasets
2. Combining the two datasets
3. Standardizing column names
4. Cleaning text fields
5. Converting numeric columns
6. Converting invoice dates
7. Identifying and removing exact duplicate rows
8. Handling missing product descriptions
9. Retaining missing Customer IDs for valid transaction analysis
10. Identifying cancelled invoices and returns
11. Identifying invalid prices and quantities
12. Creating transaction types
13. Calculating revenue
14. Creating date-based features
15. Creating customer status
16. Preparing the final dashboard dataset

## SQL Analysis

The cleaned sales data was imported into MySQL for further analysis.

SQL analysis includes:

- Overall sales KPIs
- Monthly revenue and order analysis
- Top products by revenue
- Top products by quantity
- Top customers by revenue
- Customer order analysis
- Repeat customer analysis
- Revenue by country
- Sales by hour and day
- Transaction analysis
- Customer status analysis

## Power BI Dashboard

The Power BI dashboard provides an interactive view of the retail business.

### Key KPIs

- Total Revenue
- Total Orders
- Total Quantity
- Total Customers
- Average Order Value

### Dashboard Analysis

The dashboard includes:

- Monthly Revenue Trend
- Top 10 Products by Revenue
- Revenue by Country
- Customer Status Analysis
- Sales by Hour
- Monthly Orders vs Revenue
- Interactive filters for year, month, country and customer status

### Dashboard Preview

![Online Retail Dashboard](online_retail_dashboard.png)

## Project Structure

```text
online-retail-analytics/
│
├── README.md
│
├── 01_data_profiling.py
├── 02_data_cleaning.py
│
├── retail_analysis.sql
│
├── Online_Retail_Analytics.pbix
│
├── online_retail_dashboard.png
│
└── output/
    ├── dashboard_sales.csv
    ├── cleaned_online_retail.csv
    └── data_quality_report.csv

## Skills Demonstrated

- Python
- Pandas
- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL
- MySQL
- Power BI
- DAX
- Data Visualization
- Business Analysis
- Dashboard Development
