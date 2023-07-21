import pandas as pd
import numpy as np
from random import choice

pd.set_option('display.max_columns', None)

# Define the categories, products, and seasons
categories = ["Male", "Female", "Child"]
products = ["Shirt", "Blouse", "Pants", "Shorts", "Coat", "Accessories"]
seasons = ["Summer", "Autumn", "Winter", "Spring"]

# DATES
dates = pd.date_range(start="2021-01-01", end="2022-12-31")

# STOCK FOR EACH PRODUCT
initial_stock = 200
stock = {product: initial_stock for product in products}

data = []

# GENERATING DATA FOR EACH DAY
for date in dates:
    # THESE DATAS ARE RANDOM CREATED
    available_products = [product for product in products if stock[product] > 0]
    if not available_products:  # IF NO PRODUCTS ARE AVAILABLE, CONTINUE NEXT DAY
        continue

    selling_products = np.random.choice(available_products, size=np.random.randint(1, len(available_products) + 1), replace=False)
    for product in selling_products:
        for category in categories:
            # If no stock left, continue to next product
            if stock[product] == 0:
                continue

            # GENERATING THE QUANTITY SOLD
            quantity_sold = np.random.randint(0, min(21, stock[product] + 1))  # To allow for 0 sales
            stock[product] -= quantity_sold

            # PRICE WITH CONDITIONS
            if product == "Accessories":
                price = int(np.random.normal(20, 3))
            elif product in ["Shirt", "Blouse"]:
                price = int(np.random.normal(50, 10))
            elif product in ["Pants", "Shorts"]:
                price = int(np.random.normal(75, 15))
            else:  # Coat
                price = int(np.random.normal(100, 25))

            # CONDITION FOR PROMOTION
            promotion = "Yes" if (np.random.rand() < 0.2 and quantity_sold > 0) else "No"

            # SEASON
            month = date.month
            if 3 <= month <= 5:
                season = "Spring"
            elif 6 <= month <= 8:
                season = "Summer"
            elif 9 <= month <= 11:
                season = "Autumn"
            else:
                season = "Winter"

            # SPECIAL EVENT LIKE COMMEMORATIVE DATES
            special_event = "Yes" if np.random.rand() < 0.1 else "No"

            # Add the row of data
            data.append([date, product, category, quantity_sold, price, promotion, season, special_event, stock[product]])

    # RESTOCK MONTHLY
    if date.day == 1:
        stock = {product: initial_stock for product in products}

# Create a DataFrame
df = pd.DataFrame(data, columns=["Date", "Product", "Category", "Quantity Sold", "Price", "Promotion", "Season", "Special Event", "Stock"])

df.to_excel('sales_MAC_Clothes.xlsx', index=False)