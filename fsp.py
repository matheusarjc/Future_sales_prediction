import pandas as pd
import numpy as np
import random
import datetime
import matplotlib.pyplot as plt

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

#Dataframe
df = pd.DataFrame({
    "Date": date,
    "Product": product,
    "Category": category,
    "Price": price,
    "Quantity": quantity,
    "Discount_Code": discount_code
})

col_numb = df.select_dtypes(include=[np.number]).columns.tolist()

print(df.head())
print(df[col_numb].describe())
print(df.nunique())

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

numeric_columns = df_preprocessed.select_dtypes(include=[np.number]).columns
df_preprocessed[numeric_columns] = df_preprocessed[numeric_columns].fillna(df_preprocessed[numeric_columns].mean())

# Feature Engineering
df_preprocessed = pd.get_dummies(df_preprocessed, columns=["Product", "Category"], drop_first=True)

# New Date
df_preprocessed["Month"] = df_preprocessed["Date"].dt.month
df_preprocessed["DayOfWeek"] = df_preprocessed["Date"].dt.dayofweek

df_preprocessed["TotalSales"] = df_preprocessed["Price"] * df_preprocessed["Quantity"]

df_preprocessed.drop(columns=["Date", "Discount_Code"], inplace=True)

print(df_preprocessed.head())