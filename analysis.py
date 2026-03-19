import pandas as pd

# Load dataset
data = pd.read_csv("Dataset.csv")

# Split cuisines
cuisines = data['Cuisines'].str.split(', ').explode()

# Count cuisines
cuisine_count = cuisines.value_counts()

# Top 3 cuisines
top3 = cuisine_count.head(3)

print("Top 3 Cuisines:")
print(top3)

# Percentage
total_restaurants = len(data)
percentage = (top3 / total_restaurants) * 100

print("\nPercentage of restaurants serving these cuisines:")
print(percentage)
