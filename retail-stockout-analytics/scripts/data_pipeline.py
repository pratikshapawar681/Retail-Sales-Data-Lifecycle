import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Show dataset head
print("Sample Data:")
print(df.head())

# Check for stockouts
stockouts = df[df["Stock_Available"] <= 0]
print("\nStockout Records:")
print(stockouts)

# Plot Units Sold over Time
plt.figure(figsize=(8,5))
for product in df["Product"].unique():
    subset = df[df["Product"] == product]
    plt.plot(subset["Date"], subset["Units_Sold"], marker="o", label=product)

plt.title("Units Sold Trend")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()