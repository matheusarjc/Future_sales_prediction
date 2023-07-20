import pandas as pd
import numpy as np
import random
import datetime
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)

numb_registers = 1000

date_start = datetime.datetime(2020, 1, 1)
date_end = datetime.datetime(2022, 12, 31)
date_list = [date_start + datetime.timedelta(days=random.randint(0, (date_end - date_start).days)) for _ in range(numb_registers)]

products = ["T-shirt", "Pants", "Dress", "Blouse", "Jacket", "Shorts", "Skirt", "Coat", "Shirt", "Tissue"]

categories = ["Male", "Female", "Kids", "Accessories"]

discount_codes = ["DESC10", "FREEDELIV", "DESC20", "DESC30", "DESC50", "DESC5"]

date = []
product = []
category = []
price = []
quantity = []
discount_code = []

for _ in range(numb_registers):
    date.append(random.choice(date_list))
    product.append(random.choice(products))
    category.append(random.choice(categories))
    price.append(round(random.uniform(20, 200), 2))
    quantity.append(random.randint(1, 800))
    discount_code.append(random.choice(discount_codes))

# Dataframe
df = pd.DataFrame({
    "Date": date,
    "Product": product,
    "Category": category,
    "Price": price,
    "Quantity": quantity,
    "Discount_Code": discount_code
})

# Sales
plt.figure(figsize=(10, 6))
plt.hist(df["Quantity"], bins=20, edgecolor="k", alpha=0.7)
plt.xlabel("Sold quantity")
plt.ylabel("Frequency")
plt.title("Sale's distribution")
plt.show()

# Sales x Date
sales_per_date = df.groupby("Date")["Quantity"].sum()
plt.figure(figsize=(12, 6))
plt.plot(sales_per_date.index, sales_per_date.values, marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Sold Quantity")
plt.title("Sales over time")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Discount codes
discount_count = df["Discount_Code"].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(discount_count.index, discount_count.values, color='lightgreen')
plt.xlabel("Discount Code")
plt.ylabel("Occurrences number")
plt.title("Discount code counting")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Dataframe Copy
df_preprocessed = df.copy()

# LabelEncoder para coluna "Category"
label_encoder = LabelEncoder()
df_preprocessed["Category_Encoded"] = label_encoder.fit_transform(df_preprocessed["Category"])

# New Date
df_preprocessed["Date"] = pd.to_datetime(df_preprocessed["Date"])  # Convert to datetime if not already done
df_preprocessed["Day"] = df_preprocessed["Date"].dt.day
df_preprocessed["DayOfWeek"] = df_preprocessed["Date"].dt.dayofweek
df_preprocessed["Month"] = df_preprocessed["Date"].dt.month
df_preprocessed["Year"] = df_preprocessed["Date"].dt.year

# DISCOUNT
df_preprocessed["Discount_Applied"] = df_preprocessed["Discount_Code"].apply(lambda x: 1 if x != "None" else 0)
df_preprocessed.drop(columns=["Date", "Discount_Code"], inplace=True)

# Feature Engineering (Engenharia de Recursos)
df_preprocessed = pd.get_dummies(df_preprocessed, columns=["Product", "Category"], drop_first=True)

scaler = StandardScaler()
df_preprocessed[["Price", "Quantity"]] = scaler.fit_transform(df_preprocessed[["Price", "Quantity"]])

# TARGET
y = df_preprocessed["Quantity"]
df_preprocessed.drop(columns=["Quantity"], inplace=True)

# SEASON
def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

df_preprocessed["Season"] = df_preprocessed["Month"].apply(get_season)

# DAY OF WEEK AS CATEGORY
df_preprocessed["DayOfWeek"] = df_preprocessed["DayOfWeek"].astype("category")

# Média de vendas por categoria
category_mean_sales = df.groupby("Category")["Quantity"].mean()
print(category_mean_sales)

print(df_preprocessed.head())
