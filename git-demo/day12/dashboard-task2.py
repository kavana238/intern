# dashboard.py

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example trend)
months = [1, 2, 3, 4, 5]
revenue = [2000, 3500, 3000, 5000, 6500]

# Create figure
plt.figure(figsize=(10, 5))

# First subplot (Bar Chart)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Second subplot (Line Plot)
plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()
