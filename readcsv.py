import pandas as pd

# Load the CSV files
customers_df = pd.read_csv("customers.csv")
products_df = pd.read_csv("products.csv")
sales_df = pd.read_csv("sales.csv")

# Display the data
print(customers_df.head())
print(products_df.head())
print(sales_df.head())
