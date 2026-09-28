# ============================================================
# ONLINE RETAIL ANALYTICS
# DATA PROFILING USING PYTHON, PANDAS AND NUMPY
# ============================================================

import pandas as pd
import numpy as np
import os


# ============================================================
# 1. FILE PATH
# ============================================================

file_path = r"D:\online_retail_II project folder\online_retail_II.xlsx"


print("=" * 70)
print("ONLINE RETAIL ANALYTICS - DATA PROFILING")
print("=" * 70)


# ============================================================
# 2. CHECK FILE
# ============================================================

print("\n[1] Checking file...")

if os.path.exists(file_path):
    print("Excel file found successfully!")
else:
    print("ERROR: Excel file not found.")
    print("Check the file path.")
    exit()


# ============================================================
# 3. LOAD EXCEL FILE
# ============================================================

print("\n[2] Loading Excel workbook...")

excel_file = pd.ExcelFile(file_path)

print("\nAvailable Sheets:")
print(excel_file.sheet_names)


# ============================================================
# 4. LOAD 2009-2010 DATA
# ============================================================

print("\n[3] Loading 2009-2010 data...")

df_2009 = pd.read_excel(
    file_path,
    sheet_name="Year 2009-2010"
)

print("2009-2010 loaded successfully!")


# ============================================================
# 5. LOAD 2010-2011 DATA
# ============================================================

print("\n[4] Loading 2010-2011 data...")

df_2010 = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011"
)

print("2010-2011 loaded successfully!")


# ============================================================
# 6. BASIC INFORMATION - 2009-2010
# ============================================================

print("\n" + "=" * 70)
print("2009-2010 DATASET INFORMATION")
print("=" * 70)

print("\nDataset Shape:")
print(df_2009.shape)

print("\nNumber of Rows:")
print(df_2009.shape[0])

print("\nNumber of Columns:")
print(df_2009.shape[1])

print("\nColumn Names:")
print(df_2009.columns.tolist())


# ============================================================
# 7. BASIC INFORMATION - 2010-2011
# ============================================================

print("\n" + "=" * 70)
print("2010-2011 DATASET INFORMATION")
print("=" * 70)

print("\nDataset Shape:")
print(df_2010.shape)

print("\nNumber of Rows:")
print(df_2010.shape[0])

print("\nNumber of Columns:")
print(df_2010.shape[1])

print("\nColumn Names:")
print(df_2010.columns.tolist())


# ============================================================
# 8. FIRST 5 ROWS
# ============================================================

print("\n" + "=" * 70)
print("FIRST 5 ROWS - 2009-2010")
print("=" * 70)

print(df_2009.head())


print("\n" + "=" * 70)
print("FIRST 5 ROWS - 2010-2011")
print("=" * 70)

print(df_2010.head())


# ============================================================
# 9. LAST 5 ROWS
# ============================================================

print("\n" + "=" * 70)
print("LAST 5 ROWS - 2009-2010")
print("=" * 70)

print(df_2009.tail())


print("\n" + "=" * 70)
print("LAST 5 ROWS - 2010-2011")
print("=" * 70)

print(df_2010.tail())


# ============================================================
# 10. DATA TYPES
# ============================================================

print("\n" + "=" * 70)
print("DATA TYPES - 2009-2010")
print("=" * 70)

print(df_2009.dtypes)


print("\n" + "=" * 70)
print("DATA TYPES - 2010-2011")
print("=" * 70)

print(df_2010.dtypes)


# ============================================================
# 11. DATASET INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("INFO - 2009-2010")
print("=" * 70)

df_2009.info()


print("\n" + "=" * 70)
print("INFO - 2010-2011")
print("=" * 70)

df_2010.info()


# ============================================================
# 12. MISSING VALUES - 2009-2010
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUES - 2009-2010")
print("=" * 70)

missing_2009 = df_2009.isnull().sum()

print(missing_2009)

print("\nMissing values only:")

print(
    missing_2009[
        missing_2009 > 0
    ]
)


# ============================================================
# 13. MISSING VALUES - 2010-2011
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUES - 2010-2011")
print("=" * 70)

missing_2010 = df_2010.isnull().sum()

print(missing_2010)

print("\nMissing values only:")

print(
    missing_2010[
        missing_2010 > 0
    ]
)


# ============================================================
# 14. MISSING VALUE PERCENTAGE
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUE PERCENTAGE")
print("=" * 70)


missing_percentage_2009 = (
    df_2009.isnull().mean() * 100
)

print("\n2009-2010:")

print(
    missing_percentage_2009[
        missing_percentage_2009 > 0
    ].round(2)
)


missing_percentage_2010 = (
    df_2010.isnull().mean() * 100
)

print("\n2010-2011:")

print(
    missing_percentage_2010[
        missing_percentage_2010 > 0
    ].round(2)
)


# ============================================================
# 15. DUPLICATE ROWS
# ============================================================

print("\n" + "=" * 70)
print("DUPLICATE ROW ANALYSIS")
print("=" * 70)


duplicates_2009 = df_2009.duplicated().sum()

duplicates_2010 = df_2010.duplicated().sum()


print("\n2009-2010 duplicate rows:")
print(duplicates_2009)

print("\n2010-2011 duplicate rows:")
print(duplicates_2010)


# ============================================================
# 16. DUPLICATE PERCENTAGE
# ============================================================

duplicate_percentage_2009 = (
    duplicates_2009 / len(df_2009)
) * 100


duplicate_percentage_2010 = (
    duplicates_2010 / len(df_2010)
) * 100


print("\n2009-2010 duplicate percentage:")
print(round(duplicate_percentage_2009, 2), "%")


print("\n2010-2011 duplicate percentage:")
print(round(duplicate_percentage_2010, 2), "%")


# ============================================================
# 17. UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("UNIQUE VALUES")
print("=" * 70)


for column in df_2009.columns:

    print(
        f"\n{column}:",
        df_2009[column].nunique()
    )


# ============================================================
# 18. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS - 2009-2010")
print("=" * 70)

print(
    df_2009.describe(
        include="all"
    ).transpose()
)


print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS - 2010-2011")
print("=" * 70)

print(
    df_2010.describe(
        include="all"
    ).transpose()
)


# ============================================================
# 19. NUMERIC COLUMN ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("NUMERIC COLUMN ANALYSIS")
print("=" * 70)


numeric_columns = df_2009.select_dtypes(
    include=np.number
).columns


print("\nNumeric columns:")

print(
    numeric_columns.tolist()
)


# ============================================================
# 20. NEGATIVE QUANTITY
# ============================================================

print("\n" + "=" * 70)
print("NEGATIVE QUANTITY ANALYSIS")
print("=" * 70)


negative_quantity_2009 = (
    df_2009["Quantity"] < 0
).sum()


negative_quantity_2010 = (
    df_2010["Quantity"] < 0
).sum()


print(
    "\n2009-2010 negative quantity rows:",
    negative_quantity_2009
)

print(
    "2010-2011 negative quantity rows:",
    negative_quantity_2010
)


# ============================================================
# 21. ZERO QUANTITY
# ============================================================

print("\n" + "=" * 70)
print("ZERO QUANTITY ANALYSIS")
print("=" * 70)


zero_quantity_2009 = (
    df_2009["Quantity"] == 0
).sum()


zero_quantity_2010 = (
    df_2010["Quantity"] == 0
).sum()


print(
    "\n2009-2010 zero quantity rows:",
    zero_quantity_2009
)

print(
    "2010-2011 zero quantity rows:",
    zero_quantity_2010
)


# ============================================================
# 22. NEGATIVE PRICE
# ============================================================

print("\n" + "=" * 70)
print("NEGATIVE PRICE ANALYSIS")
print("=" * 70)


negative_price_2009 = (
    df_2009["Price"] < 0
).sum()


negative_price_2010 = (
    df_2010["Price"] < 0
).sum()


print(
    "\n2009-2010 negative price rows:",
    negative_price_2009
)

print(
    "2010-2011 negative price rows:",
    negative_price_2010
)


# ============================================================
# 23. ZERO PRICE
# ============================================================

print("\n" + "=" * 70)
print("ZERO PRICE ANALYSIS")
print("=" * 70)


zero_price_2009 = (
    df_2009["Price"] == 0
).sum()


zero_price_2010 = (
    df_2010["Price"] == 0
).sum()


print(
    "\n2009-2010 zero price rows:",
    zero_price_2009
)

print(
    "2010-2011 zero price rows:",
    zero_price_2010
)


# ============================================================
# 24. UNIQUE PRODUCTS
# ============================================================

print("\n" + "=" * 70)
print("PRODUCT ANALYSIS")
print("=" * 70)


print(
    "\nUnique products - 2009-2010:",
    df_2009["StockCode"].nunique()
)

print(
    "Unique products - 2010-2011:",
    df_2010["StockCode"].nunique()
)


# ============================================================
# 25. UNIQUE CUSTOMERS
# ============================================================

print("\n" + "=" * 70)
print("CUSTOMER ANALYSIS")
print("=" * 70)


print(
    "\nUnique customers - 2009-2010:",
    df_2009["Customer ID"].nunique()
)

print(
    "Unique customers - 2010-2011:",
    df_2010["Customer ID"].nunique()
)


# ============================================================
# 26. UNIQUE COUNTRIES
# ============================================================

print("\n" + "=" * 70)
print("COUNTRY ANALYSIS")
print("=" * 70)


print(
    "\nUnique countries - 2009-2010:",
    df_2009["Country"].nunique()
)

print(
    "Unique countries - 2010-2011:",
    df_2010["Country"].nunique()
)


# ============================================================
# 27. TOP COUNTRIES
# ============================================================

print("\n" + "=" * 70)
print("TOP 10 COUNTRIES - 2009-2010")
print("=" * 70)

print(
    df_2009["Country"]
    .value_counts()
    .head(10)
)


print("\n" + "=" * 70)
print("TOP 10 COUNTRIES - 2010-2011")
print("=" * 70)

print(
    df_2010["Country"]
    .value_counts()
    .head(10)
)


# ============================================================
# 28. TOP PRODUCTS
# ============================================================

print("\n" + "=" * 70)
print("TOP 10 PRODUCTS BY TRANSACTION COUNT")
print("=" * 70)


print(
    df_2009["StockCode"]
    .value_counts()
    .head(10)
)


# ============================================================
# 29. INVOICE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("INVOICE ANALYSIS")
print("=" * 70)


print(
    "\nUnique invoices - 2009-2010:",
    df_2009["Invoice"].nunique()
)

print(
    "Unique invoices - 2010-2011:",
    df_2010["Invoice"].nunique()
)


# ============================================================
# 30. CANCELLED INVOICES
# ============================================================

print("\n" + "=" * 70)
print("CANCELLED INVOICE ANALYSIS")
print("=" * 70)


cancelled_2009 = (
    df_2009["Invoice"]
    .astype(str)
    .str.startswith("C")
    .sum()
)


cancelled_2010 = (
    df_2010["Invoice"]
    .astype(str)
    .str.startswith("C")
    .sum()
)


print(
    "\nCancelled invoice rows - 2009-2010:",
    cancelled_2009
)

print(
    "Cancelled invoice rows - 2010-2011:",
    cancelled_2010
)


# ============================================================
# 31. DATE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("DATE ANALYSIS")
print("=" * 70)


df_2009["InvoiceDate"] = pd.to_datetime(
    df_2009["InvoiceDate"],
    errors="coerce"
)


df_2010["InvoiceDate"] = pd.to_datetime(
    df_2010["InvoiceDate"],
    errors="coerce"
)


print(
    "\n2009-2010 minimum date:",
    df_2009["InvoiceDate"].min()
)

print(
    "2009-2010 maximum date:",
    df_2009["InvoiceDate"].max()
)


print(
    "\n2010-2011 minimum date:",
    df_2010["InvoiceDate"].min()
)

print(
    "2010-2011 maximum date:",
    df_2010["InvoiceDate"].max()
)


# ============================================================
# 32. MISSING DATE VALUES
# ============================================================

print("\n" + "=" * 70)
print("MISSING DATE ANALYSIS")
print("=" * 70)


print(
    "\nMissing InvoiceDate - 2009-2010:",
    df_2009["InvoiceDate"].isnull().sum()
)

print(
    "Missing InvoiceDate - 2010-2011:",
    df_2010["InvoiceDate"].isnull().sum()
)


# ============================================================
# 33. BASIC REVENUE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("REVENUE ANALYSIS")
print("=" * 70)


df_2009["Revenue"] = (
    df_2009["Quantity"] *
    df_2009["Price"]
)


df_2010["Revenue"] = (
    df_2010["Quantity"] *
    df_2010["Price"]
)


print(
    "\nTotal Revenue - 2009-2010:",
    round(df_2009["Revenue"].sum(), 2)
)


print(
    "Total Revenue - 2010-2011:",
    round(df_2010["Revenue"].sum(), 2)
)


# ============================================================
# 34. POSITIVE SALES REVENUE
# ============================================================

print("\n" + "=" * 70)
print("POSITIVE SALES REVENUE")
print("=" * 70)


positive_sales_2009 = df_2009[
    (df_2009["Quantity"] > 0) &
    (df_2009["Price"] > 0)
]


positive_sales_2010 = df_2010[
    (df_2010["Quantity"] > 0) &
    (df_2010["Price"] > 0)
]


print(
    "\nPositive sales rows - 2009-2010:",
    len(positive_sales_2009)
)

print(
    "Positive sales rows - 2010-2011:",
    len(positive_sales_2010)
)


print(
    "\nPositive sales revenue - 2009-2010:",
    round(
        positive_sales_2009["Revenue"].sum(),
        2
    )
)


print(
    "Positive sales revenue - 2010-2011:",
    round(
        positive_sales_2010["Revenue"].sum(),
        2
    )
)


# ============================================================
# 35. COMBINE DATA FOR OVERALL PROFILE
# ============================================================

print("\n" + "=" * 70)
print("COMBINING DATASETS")
print("=" * 70)


df = pd.concat(
    [df_2009, df_2010],
    ignore_index=True
)


print(
    "\nCombined dataset shape:",
    df.shape
)


# ============================================================
# 36. OVERALL MISSING VALUES
# ============================================================

print("\n" + "=" * 70)
print("OVERALL MISSING VALUES")
print("=" * 70)


overall_missing = df.isnull().sum()

print(
    overall_missing[
        overall_missing > 0
    ]
)


# ============================================================
# 37. OVERALL DUPLICATES
# ============================================================

print("\n" + "=" * 70)
print("OVERALL DUPLICATE ANALYSIS")
print("=" * 70)


overall_duplicates = df.duplicated().sum()

print(
    "Total duplicate rows:",
    overall_duplicates
)


# ============================================================
# 38. OVERALL DATA TYPES
# ============================================================

print("\n" + "=" * 70)
print("OVERALL DATA TYPES")
print("=" * 70)

print(df.dtypes)


# ============================================================
# 39. OVERALL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("OVERALL DATASET SUMMARY")
print("=" * 70)


print("\nTotal Rows:")
print(len(df))


print("\nTotal Columns:")
print(len(df.columns))


print("\nUnique Products:")
print(df["StockCode"].nunique())


print("\nUnique Customers:")
print(df["Customer ID"].nunique())


print("\nUnique Countries:")
print(df["Country"].nunique())


print("\nUnique Invoices:")
print(df["Invoice"].nunique())


print("\nTotal Quantity:")
print(df["Quantity"].sum())


print("\nTotal Revenue:")
print(round(df["Revenue"].sum(), 2))


# ============================================================
# 40. SAVE PROFILE REPORT
# ============================================================

print("\n" + "=" * 70)
print("SAVING PROFILE REPORT")
print("=" * 70)


output_folder = r"D:\online_retail_II project folder\output"

os.makedirs(
    output_folder,
    exist_ok=True
)


profile_report = pd.DataFrame({

    "Metric": [
        "Total Rows",
        "Total Columns",
        "Duplicate Rows",
        "Missing Description",
        "Missing Customer ID",
        "Missing Invoice Date",
        "Negative Quantity",
        "Zero Quantity",
        "Negative Price",
        "Zero Price",
        "Unique Products",
        "Unique Customers",
        "Unique Countries",
        "Unique Invoices",
        "Total Quantity",
        "Total Revenue"
    ],

    "Value": [

        len(df),

        len(df.columns),

        df.duplicated().sum(),

        df["Description"].isnull().sum(),

        df["Customer ID"].isnull().sum(),

        df["InvoiceDate"].isnull().sum(),

        (df["Quantity"] < 0).sum(),

        (df["Quantity"] == 0).sum(),

        (df["Price"] < 0).sum(),

        (df["Price"] == 0).sum(),

        df["StockCode"].nunique(),

        df["Customer ID"].nunique(),

        df["Country"].nunique(),

        df["Invoice"].nunique(),

        df["Quantity"].sum(),

        round(df["Revenue"].sum(), 2)

    ]

})


report_path = os.path.join(
    output_folder,
    "data_profiling_report.csv"
)


profile_report.to_csv(
    report_path,
    index=False
)


print(
    "\nProfile report saved successfully!"
)

print(
    report_path
)


# ============================================================
# 41. FINAL MESSAGE
# ============================================================

print("\n")
print("=" * 70)
print("DATA PROFILING COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nNext step:")
print("Use the profiling results to perform data cleaning.")

print("\nOutput file:")
print("data_profiling_report.csv")

print("=" * 70)