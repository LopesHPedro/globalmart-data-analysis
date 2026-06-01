import pandas as pd
import numpy as np

np.random.seed(42) # For reproducibility

N_PRODUCTS = 500

categories ={
    "Books": ["Novel", "Cookbook", "History Book", "Science Book", "Biography"],
    "Electronics": ["Smartphone", "Laptop", "Headphones", "Smartwatch", "Tablet"],
    "Makeup": ["Lipstick", "Foundation", "Mascara", "Eyeliner", "Blush"],
    "Garden": ["Plant Pot", "Garden Hose", "Flower Seeds", "Pruning Shears", "Soil Bag"],
    "Fashion": ["T-Shirt", "Jeans", "Sneakers", "Jacket", "Dress"],
    "Sports": ["Football", "Yoga Mat", "Running Shoes", "Dumbbell", "Backpack"]
}

categories_weights = {
    "Books": 0.15,
    "Electronics": 0.30, # Globalmart has a strong focus on electronics
    "Makeup": 0.10,
    "Garden": 0.05,
    "Fashion": 0.20,
    "Sports": 0.20
}

prefixes = ["Super", "Ultra", "Mega", "Eco", "Pro", "Smart", "Easy", "Quick", "Best", "New"]    
suffixes = ["X", "Plus", "Max", "Pro", "Lite", "Go", "Air", "One", "Prime", "Elite"]

category_prefixes = {
    "Books": "BOOK",
    "Electronics": "ELEC",
    "Makeup": "MAKE",
    "Garden": "GARD",
    "Fashion": "FASH",
    "Sports": "SPOR"
}

category_counters = {
    "Books": 0,
    "Electronics": 0,
    "Makeup": 0,
    "Garden": 0,
    "Fashion": 0,
    "Sports": 0
}

selected_category = np.random.choice(
    list(categories.keys()),
    p=list(categories_weights.values())
)

category_counters[selected_category] += 1

product_id = f"{category_prefixes[selected_category]}-{str(category_counters[selected_category]).zfill(4)}"
product_name = f"{np.random.choice(prefixes)} {np.random.choice(categories[selected_category])} {np.random.choice(suffixes)}"

print(product_id, selected_category, product_name)
