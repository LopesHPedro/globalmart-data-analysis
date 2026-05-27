import pandas as pd
import numpy as np
from faker import Faker
from uuid import uuid4 # use uuid4 to generate unique customer IDs

def generate_email_from_name(name):
    # Generate an email address based on the customer's name
    username = name.lower().replace(" ", np.random.choice([".", "_", ""]))
    domain = np.random.choice(["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"])
    return f"{username}@{domain}"

fake = Faker()

np.random.seed(42) # for reproducibility

N_CUSTOMERS = 10_000

customers_ids = [str(uuid4()) for _ in range(N_CUSTOMERS)]
customers_names = [fake.name() for _ in range(N_CUSTOMERS)]
customers_emails = [generate_email_from_name(name) for name in customers_names]

# To make more realistic, we can introduce some invalid email addresses
invalid_emails = [fake.word() for _ in range(int(N_CUSTOMERS * 0.05))] # 5% invalid emails

# Now we randomly replace some of the valid emails with invalid ones
for i in np.random.choice(N_CUSTOMERS, size=int(N_CUSTOMERS * 0.05), replace=False):
    customers_emails[i] = np.random.choice(invalid_emails)


countries = ["Brazil", "United States", "Canada", "France", "Spain"]
country_weights = [0.4, 0.3, 0.1, 0.1, 0.1] # Brazil is more likely to be the country of residence

customers_countries = np.random.choice(
    countries,
    size=N_CUSTOMERS,
    p=country_weights
)

customers_birth_dates = [
    fake.date_of_birth(minimum_age=18, maximum_age=80)
    for _ in range(N_CUSTOMERS)
]

MISSING_BIRTH_DATES = int(N_CUSTOMERS * 0.03) # 3% missing birth dates

missing_birth_date_index = np.random.choice(N_CUSTOMERS, size=int(MISSING_BIRTH_DATES), replace=False)

for i in missing_birth_date_index:
    customers_birth_dates[i] = None

customers_registration_dates = [
    fake.date_between(start_date="-3y", end_date="today")
    for _ in range(N_CUSTOMERS)
]

"""
print(customers_birth_dates[:5])
print()
print(customers_registration_dates[:5])
"""

customers_df = pd.DataFrame({"customer_id": customers_ids, "customer_name": customers_names, "customer_email": customers_emails,
                              "customer_country": customers_countries, "customer_birth_date": customers_birth_dates,
                              "customer_registration_date": customers_registration_dates})

customers_df.to_csv("data/raw/customers.csv", index=False)
print("customers.csv generated successfully!")
