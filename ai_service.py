import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_summary(df):

    # find numeric columns automatically
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) == 0:
        return "No numeric sales data found in the CSV."

    sales_col = numeric_cols[0]

    total_sales = df[sales_col].sum()
    avg_sales = df[sales_col].mean()

    # choose product column if exists
    if "Product" in df.columns:
        product_sales = df.groupby("Product")[sales_col].sum()
    else:
        product_sales = df.groupby(df.columns[0])[sales_col].sum()

    top_product = product_sales.idxmax()

    os.makedirs("charts", exist_ok=True)

    plt.figure()
    product_sales.plot(kind="bar")
    plt.title("Sales by Product")

    chart_path = "charts/sales_chart.png"
    plt.savefig(chart_path)

    summary = f"""
Sales Performance Summary

Total Revenue: {total_sales}
Average Sale Value: {avg_sales:.2f}
Top Performing Item: {top_product}

Chart generated successfully.
"""

    return summary