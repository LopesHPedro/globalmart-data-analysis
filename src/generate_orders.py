import pandas as pd
import numpy as np

np.random.seed(42) # For reproducibility

N_ORDERS = 30_000

order_id = [f"ORD-{str(i).zfill(5)}" for i in range(1, N_ORDERS + 1)]

order_dates = pd.date_range(start="2023-01-01", end="2026-06-05")
order_date_selected = np.random.choice(order_dates, size=N_ORDERS)

order_status = np.random.choice(["Completed", "Pending", "Cancelled"], size=N_ORDERS, p=[0.7, 0.2, 0.1])
payment_method = np.random.choice(["Credit Card", "PayPal", "Bank Transfer"], size=N_ORDERS, p=[0.5, 0.3, 0.2])

customers_df = pd.read_csv("data/raw/customers.csv")
customer_ids = customers_df["customer_id"].tolist()

order_customer_ids = np.random.choice(
    customer_ids,
    size=N_ORDERS,
    replace=True
)

orders_df = pd.DataFrame({
    "order_id": order_id,
    "customer_id": order_customer_ids,
    "order_date": order_date_selected,
    "order_status": order_status,
    "payment_method": payment_method
})

print(orders_df.head())
print(orders_df.shape)
print(orders_df.isna().sum())

orders_df.to_csv("data/raw/orders.csv", index=False)

print("Orders dataset generated and saved to data/raw/orders.csv")