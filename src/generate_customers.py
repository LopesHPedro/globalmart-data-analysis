import pandas as pd
import numpy as np
from faker import Faker
from uuid import uuid4 # use uuid4 to generate unique customer IDs

fake = Faker()

np.random.seed(42) # for reproducibility

N_CUSTOMERS = 10_000

customers_ids = [str(uuid4()) for _ in range(N_CUSTOMERS)]
customers_names = [fake.name() for _ in range(N_CUSTOMERS)]
