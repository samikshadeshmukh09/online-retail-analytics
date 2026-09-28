
import pandas as pd
import numpy as np
import os

# ============================================================
# ONLINE RETAIL ANALYTICS - DATA CLEANING
# ============================================================

print("=" * 70)
print("ONLINE RETAIL ANALYTICS - DATA CLEANING")
print("=" * 70)


# ============================================================
# 1. FILE PATHS
# ============================================================

file_path = r"D:\online_retail_II project folder\online_retail_II.xlsx"

output_folder = r"D:\online_retail_II project folder\output"

os.makedirs(output_folder, exist_ok=True)


# ============================================================
# 2. CHECK FILE
# ============================================================

print("\n[1] Checking Excel file...")

if not os.path.exists(file_path):
    print("ERROR: Excel file not found.")
    print("Check the file path.")
    exit()

print("Excel file found successfully!")


# ============================================================
# 3. LOAD BOTH EXCEL SHEETS
# ============================================================

print("\n[2] Loading Excel sheets...")

df_2009 = pd.read_excel(
    file_path,
    sheet_name="Year 2009-2010"
)

df_2010 = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011"
)

print("2009-2010 loaded:", df_2009.shape)
print("2010-2011 loaded:", df_2010.shape)


# ============================================================
# 4. COMBINE BOTH YEARS
# ============================================================

print("\n[3] Combining both years...")

df = pd.concat(
    [df_2009, df_2010],
    ignore_index=True
)

original_row_count = len(df)

print("Combined dataset shape:", df.shape)


# ============================================================
# 5. STANDARDIZE COLUMN NAMES
# ============================================================

print("\n[4] Standardizing column names...")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

# Convert invoicedate -> invoice_date
if "invoicedate" in df.columns:

    df.rename(
        columns={
            "invoicedate": "invoice_date"
        },
        inplace=True
    )

print("Final standardized columns:")

print(df.columns.tolist())


# ============================================================
# 6. CLEAN TEXT COLUMNS
# ============================================================

print("\n[5] Cleaning text columns...")

text_columns = [
    "invoice",
    "stockcode",
    "description",
    "country"
]

for col in text_columns:

    if col in df.columns:

        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
        )

print("Text columns cleaned.")


# ============================================================
# 7. CONVERT NUMERIC COLUMNS
# ============================================================

print("\n[6] Converting numeric columns...")

numeric_columns = [
    "quantity",
    "price",
    "customer_id"
]

for col in numeric_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

print("Numeric columns converted.")


# ============================================================
# 8. CONVERT INVOICE DATE
# ============================================================

print("\n[7] Converting InvoiceDate...")

df["invoice_date"] = pd.to_datetime(
    df["invoice_date"],
    errors="coerce"
)

print("InvoiceDate converted successfully.")


# ============================================================
# 9. CHECK DUPLICATES BEFORE ADDING ROW ID
# ============================================================

print("\n[8] Checking exact duplicate rows...")

duplicate_count = df.duplicated().sum()

print(
    "Exact duplicate rows found:",
    duplicate_count
)

if duplicate_count > 0:

    df = df.drop_duplicates(
        keep="first"
    )

    print(
        "Duplicate rows removed:",
        duplicate_count
    )

else:

    print("No exact duplicate rows found.")


# ============================================================
# 10. CREATE ORIGINAL ROW ID
# ============================================================

print("\n[9] Creating original row ID...")

df["original_row_id"] = range(
    1,
    len(df) + 1
)

print("Original row ID created.")


# ============================================================
# 11. MISSING VALUE ANALYSIS
# ============================================================

print("\n[10] Checking missing values...")

missing_description = df["description"].isna().sum()

missing_customer = df["customer_id"].isna().sum()

missing_report = pd.DataFrame({

    "column": df.columns,

    "missing_count":
        df.isnull().sum().values,

    "missing_percentage":
        (
            df.isnull().sum().values
            / len(df)
            * 100
        )
})

missing_report = missing_report[
    missing_report["missing_count"] > 0
]

if len(missing_report) > 0:

    print(
        missing_report.to_string(
            index=False
        )
    )

else:

    print("No missing values found.")


# ============================================================
# 12. HANDLE MISSING DESCRIPTIONS
# ============================================================

print("\n[11] Handling missing descriptions...")

df["description"] = df["description"].fillna(
    "Unknown Product"
)

print(
    "Missing descriptions replaced:",
    missing_description
)


# ============================================================
# 13. HANDLE CUSTOMER ID
# ============================================================

print("\n[12] Handling Customer ID...")

# Customer ID is not required for every transaction.
# Therefore, we keep missing Customer IDs.

df["customer_id"] = df["customer_id"].astype("Int64")

print(
    "Missing Customer IDs retained:",
    missing_customer
)


# ============================================================
# 14. CREATE DATE FEATURES
# ============================================================

print("\n[13] Creating date features...")

df["year"] = df["invoice_date"].dt.year

df["month"] = df["invoice_date"].dt.month

df["month_name"] = df["invoice_date"].dt.month_name()

df["day"] = df["invoice_date"].dt.day

df["day_name"] = df["invoice_date"].dt.day_name()

df["hour"] = df["invoice_date"].dt.hour

print("Date features created.")


# ============================================================
# 15. IDENTIFY CANCELLED INVOICES
# ============================================================

print("\n[14] Identifying cancelled invoices...")

df["is_cancelled"] = (
    df["invoice"]
    .str.upper()
    .str.startswith("C", na=False)
)

cancelled_count = df["is_cancelled"].sum()

print(
    "Cancelled transaction rows:",
    cancelled_count
)


# ============================================================
# 16. IDENTIFY RETURNS
# ============================================================

print("\n[15] Identifying returns...")

df["is_return"] = (
    df["quantity"] < 0
)

return_count = df["is_return"].sum()

print(
    "Rows with negative quantity:",
    return_count
)


# ============================================================
# 17. IDENTIFY INVALID PRICES
# ============================================================

print("\n[16] Checking invalid prices...")

df["is_invalid_price"] = (
    df["price"] <= 0
)

invalid_price_count = (
    df["is_invalid_price"].sum()
)

print(
    "Rows with zero/negative price:",
    invalid_price_count
)


# ============================================================
# 18. IDENTIFY INVALID QUANTITY
# ============================================================

print("\n[17] Checking invalid quantity...")

df["is_invalid_quantity"] = (
    df["quantity"] <= 0
)

invalid_quantity_count = (
    df["is_invalid_quantity"].sum()
)

print(
    "Rows with zero/negative quantity:",
    invalid_quantity_count
)


# ============================================================
# 19. CREATE TRANSACTION TYPE
# ============================================================

print("\n[18] Creating transaction type...")

conditions = [

    # Cancellation
    df["is_cancelled"],

    # Return
    (~df["is_cancelled"]) &
    (df["quantity"] < 0),

    # Invalid transaction
    (df["quantity"] <= 0) |
    (df["price"] <= 0)
]

choices = [
    "Cancelled",
    "Return",
    "Invalid"
]

df["transaction_type"] = np.select(
    conditions,
    choices,
    default="Sale"
)

print("\nTransaction type distribution:")

print(
    df["transaction_type"]
    .value_counts()
)


# ============================================================
# 20. CALCULATE REVENUE
# ============================================================

print("\n[19] Calculating revenue...")

df["revenue"] = (
    df["quantity"] *
    df["price"]
)

print("Revenue column created.")


# ============================================================
# 21. HANDLE INFINITE VALUES
# ============================================================

print("\n[20] Checking infinite values...")

df = df.replace(
    [np.inf, -np.inf],
    np.nan
)

print("Infinite values handled.")


# ============================================================
# 22. REMOVE CRITICAL MISSING VALUES
# ============================================================

print("\n[21] Removing rows with critical missing values...")

critical_columns = [
    "invoice",
    "stockcode",
    "quantity",
    "invoice_date",
    "price",
    "country"
]

before_critical_filter = len(df)

df = df.dropna(
    subset=critical_columns
)

after_critical_filter = len(df)

critical_rows_removed = (
    before_critical_filter
    - after_critical_filter
)

print(
    "Rows removed:",
    critical_rows_removed
)


# ============================================================
# 23. CREATE DASHBOARD SALES DATA
# ============================================================

print("\n[22] Creating dashboard sales dataset...")

dashboard_sales = df[
    (df["transaction_type"] == "Sale") &
    (df["quantity"] > 0) &
    (df["price"] > 0)
].copy()

print(
    "Dashboard sales rows:",
    len(dashboard_sales)
)


# ============================================================
# 24. REMOVE SPECIAL TRANSACTION CODES
# ============================================================

print("\n[23] Removing special transaction codes...")

special_codes = [
    "POST",
    "DOT",
    "M",
    "D",
    "S",
    "AMAZONFEE",
    "BANK CHARGES",
    "CRUK",
    "C2"
]

dashboard_sales = dashboard_sales[
    ~dashboard_sales["stockcode"]
    .str.upper()
    .isin(special_codes)
].copy()

print(
    "Dashboard rows after special-code removal:",
    len(dashboard_sales)
)


# ============================================================
# 25. CREATE CUSTOMER STATUS
# ============================================================

print("\n[24] Creating customer status...")

dashboard_sales["customer_status"] = np.where(

    dashboard_sales["customer_id"].isna(),

    "Unknown Customer",

    "Identified Customer"
)

print(
    dashboard_sales["customer_status"]
    .value_counts()
)


# ============================================================
# 26. SORT DATA
# ============================================================

print("\n[25] Sorting data...")

df = df.sort_values(
    by="invoice_date"
)

dashboard_sales = dashboard_sales.sort_values(
    by="invoice_date"
)

print("Data sorted by Invoice Date.")


# ============================================================
# 27. FINAL VALIDATION
# ============================================================

print("\n[26] FINAL DATA VALIDATION")

print("-" * 70)

print(
    "Original combined rows:",
    original_row_count
)

print(
    "Duplicate rows removed:",
    duplicate_count
)

print(
    "Final cleaned rows:",
    len(df)
)

print(
    "Dashboard sales rows:",
    len(dashboard_sales)
)

print(
    "Columns in cleaned dataset:",
    len(df.columns)
)

print(
    "Columns in dashboard dataset:",
    len(dashboard_sales.columns)
)

print(
    "Remaining duplicate rows:",
    df.duplicated().sum()
)

print(
    "Remaining missing Invoice:",
    df["invoice"].isna().sum()
)

print(
    "Remaining missing StockCode:",
    df["stockcode"].isna().sum()
)

print(
    "Remaining missing Quantity:",
    df["quantity"].isna().sum()
)

print(
    "Remaining missing Price:",
    df["price"].isna().sum()
)

print(
    "Remaining missing Invoice Date:",
    df["invoice_date"].isna().sum()
)


# ============================================================
# 28. CREATE DATA QUALITY REPORT
# ============================================================

print("\n[27] Creating data quality report...")

quality_report = pd.DataFrame({

    "Metric": [

        "Original Combined Rows",

        "Duplicate Rows Found",

        "Duplicate Rows Removed",

        "Final Cleaned Rows",

        "Dashboard Sales Rows",

        "Cancelled Rows",

        "Return Rows",

        "Invalid Price Rows",

        "Invalid Quantity Rows",

        "Missing Description Initially",

        "Missing Customer ID Initially",

        "Critical Rows Removed"
    ],

    "Value": [

        original_row_count,

        duplicate_count,

        duplicate_count,

        len(df),

        len(dashboard_sales),

        cancelled_count,

        return_count,

        invalid_price_count,

        invalid_quantity_count,

        missing_description,

        missing_customer,

        critical_rows_removed
    ]
})

print("\nData Quality Report:")

print(
    quality_report.to_string(
        index=False
    )
)


# ============================================================
# 29. EXPORT FULL CLEANED DATA AS CSV
# ============================================================

print("\n[28] Exporting full cleaned dataset...")

cleaned_csv = os.path.join(
    output_folder,
    "cleaned_online_retail.csv"
)

dashboard_csv = os.path.join(
    output_folder,
    "dashboard_sales.csv"
)

quality_csv = os.path.join(
    output_folder,
    "data_quality_report.csv"
)

df.to_csv(
    cleaned_csv,
    index=False
)

print(
    "Cleaned CSV created:"
)

print(cleaned_csv)


# ============================================================
# 30. EXPORT DASHBOARD DATA AS CSV
# ============================================================

print("\n[29] Exporting dashboard sales data...")

dashboard_sales.to_csv(
    dashboard_csv,
    index=False
)

print(
    "Dashboard CSV created:"
)

print(dashboard_csv)


# ============================================================
# 31. EXPORT DATA QUALITY REPORT
# ============================================================

print("\n[30] Exporting data quality report...")

quality_report.to_csv(
    quality_csv,
    index=False
)

print(
    "Quality report created:"
)

print(quality_csv)


# ============================================================
# 32. CREATE SMALL EXCEL SUMMARY FILE
# ============================================================

print("\n[31] Creating Excel summary file...")

summary_excel = os.path.join(
    output_folder,
    "online_retail_summary.xlsx"
)

# Create smaller summary tables
transaction_summary = (
    df["transaction_type"]
    .value_counts()
    .reset_index()
)

transaction_summary.columns = [
    "Transaction Type",
    "Count"
]

country_summary = (
    dashboard_sales
    .groupby("country")
    .agg(
        Total_Revenue=("revenue", "sum"),
        Total_Quantity=("quantity", "sum"),
        Transactions=("invoice", "nunique")
    )
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
    .reset_index()
)

monthly_summary = (
    dashboard_sales
    .groupby(
        ["year", "month", "month_name"]
    )
    .agg(
        Revenue=("revenue", "sum"),
        Quantity=("quantity", "sum"),
        Transactions=("invoice", "nunique")
    )
    .reset_index()
)

top_products = (
    dashboard_sales
    .groupby(
        ["stockcode", "description"]
    )
    .agg(
        Revenue=("revenue", "sum"),
        Quantity=("quantity", "sum"),
        Transactions=("invoice", "nunique")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(100)
    .reset_index()
)

# Write only small summary tables to Excel
with pd.ExcelWriter(
    summary_excel,
    engine="openpyxl"
) as writer:

    quality_report.to_excel(
        writer,
        sheet_name="Data Quality",
        index=False
    )

    transaction_summary.to_excel(
        writer,
        sheet_name="Transactions",
        index=False
    )

    country_summary.to_excel(
        writer,
        sheet_name="Country Summary",
        index=False
    )

    monthly_summary.to_excel(
        writer,
        sheet_name="Monthly Summary",
        index=False
    )

    top_products.to_excel(
        writer,
        sheet_name="Top 100 Products",
        index=False
    )

print(
    "Excel summary created:"
)

print(summary_excel)


# ============================================================
# 33. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 70)

print("DATA CLEANING COMPLETED SUCCESSFULLY!")

print("=" * 70)

print("\nFiles created inside:")

print(output_folder)

print("\n1. cleaned_online_retail.csv")
print("2. dashboard_sales.csv")
print("3. data_quality_report.csv")
print("4. online_retail_summary.xlsx")

print("\nNext step:")
print("SQL DATABASE CREATION AND DATA LOADING")

print("=" * 70)
