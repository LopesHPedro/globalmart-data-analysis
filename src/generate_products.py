import pandas as pd
import numpy as np

np.random.seed() # For reproducibility

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

# Teste
selected_category = np.random.choice(list(categories.keys()), p=list(categories_weights.values())) # Only works because the keys and values are in the same order
print(np.random.choice(prefixes),np.random.choice(categories[selected_category]), np.random.choice(suffixes))
