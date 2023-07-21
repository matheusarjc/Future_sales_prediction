import pandas as pd
import numpy as np
from random import choice

# Define the categories, products, and seasons
categories = ["Male", "Female", "Child"]
products = ["Shirt", "Blouse", "Pants", "Shorts", "Coat", "Accessories"]
seasons = ["Summer", "Autumn", "Winter", "Spring"]

# Generate dates for 2 years
dates = pd.date_range(start="2021-01-01", end="2022-12-31")

data = []

# Generate data for each day
for date in dates:
    # Assume each product has a chance of being sold each day
    for product in products:
        for category in categories:
            # Generate the quantity sold (assume a normal distribution with mean 100 and std deviation 20)
            quantity_sold = int(np.random.normal(100, 20))

            # Assume the price is normally distributed, but depends on the product
            if product == "Accessories":
                price = int(np.random.normal(20, 3))
            elif product in ["Shirt", "Blouse"]:
                price = int(np.random.normal(50, 10))
            elif product in ["Pants", "Shorts"]:
                price = int(np.random.normal(75, 15))
            else:  # Coat
                price = int(np.random.normal(100, 25))

            # Assume promotion happens 20% of the time
            promotion = np.random.rand() < 0.2

            # Define the season based on the month
            month = date.month
            if 3 <= month <= 5:
                season = "Spring"
            elif 6 <= month <= 8:
                season = "Summer"
            elif 9 <= month <= 11:
                season = "Autumn"
            else:
                season = "Winter"

            # Assume a special event happens 10% of the time
            special_event = np.random.rand() < 0.1

            # Add the row of data
            data.append([date, product, category, quantity_sold, price, promotion, season, special_event])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Date", "Product", "Category", "Quantity Sold", "Price", "Promotion", "Season", "Special Event"])

# Convert 'Promotion' and 'Special Event' columns to 'Yes'/'No'
df["Promotion"] = df["Promotion"].map({True: "Yes", False: "No"})
df["Special Event"] = df["Special Event"].map({True: "Yes", False: "No"})

# Save the data to an Excel file
df.to_excel('sales_MAC_Clothes.xlsx', index=False)
