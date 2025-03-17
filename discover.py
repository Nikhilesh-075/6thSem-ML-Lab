import matplotlib.pyplot as plt
import seaborn as sns

# Summary statistics of the data
print(data.describe())

# Visualize correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Visualize relationships between features and target
sns.pairplot(data[['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'median_income', 'median_house_value']])
plt.show()

# Distribution of the target variable
plt.figure(figsize=(6, 4))
sns.histplot(data['median_house_value'], bins=50, kde=True)
plt.title('Distribution of Median House Value')
plt.show()
