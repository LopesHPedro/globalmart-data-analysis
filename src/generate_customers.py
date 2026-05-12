import pandas as pd
import numpy as np
from faker import Faker
from uuid import uuid4 # use uuid4 to generate unique customer IDs

fake = Faker()

np.random.seed(42) # for reproducibility

N_CUSTOMERS = 10_000

customers_ids = [str(uuid4()) for _ in range(N_CUSTOMERS)]
customers_names = [fake.name() for _ in range(N_CUSTOMERS)]
customers_emails = [fake.email() for _ in range(N_CUSTOMERS)]

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

customers_registration_dates = [
    fake.date_between(start_date="-3y", end_date="today")
    for _ in range(N_CUSTOMERS)
]

print(customers_birth_dates[:5])
print()
print(customers_registration_dates[:5])