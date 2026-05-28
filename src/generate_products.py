import pandas as pd
import numpy as np

np.random.seed(42)

N_PRODUCTS = 500

categories ={
    "Books": ["Novel", "Cookbook", "History Book", "Science Book", "Biography"],
    "Electronics": ["Smartphone", "Laptop", "Headphones", "Smartwatch", "Tablet"],
    "Makeup": ["Lipstick", "Foundation", "Mascara", "Eyeliner", "Blush"],
    "Garden": ["Plant Pot", "Garden Hose", "Flower Seeds", "Pruning Shears", "Soil Bag"],
    "Fashion": ["T-Shirt", "Jeans", "Sneakers", "Jacket", "Dress"],
    "Sports": ["Football", "Yoga Mat", "Running Shoes", "Dumbbell", "Backpack"]
}