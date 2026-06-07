import pandas as pd
import numpy as np

np.random.seed(42)

# First of all I need to load the orders and products

orders_df = pd.read_csv("data/raw/orders.csv")
products_df = pd.read_csv("data/raw/products.csv")

orders_id = orders_df["order_id"].tolist()
products_id = products_df["product_id"].tolist()
