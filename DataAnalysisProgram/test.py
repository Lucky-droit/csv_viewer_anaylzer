import pandas as pd

# Create a sample DataFrame with missing data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, None, 30, 22, 28],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'San Francisco'],
    'Salary': [50000, 60000, 75000, None, 80000]
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('sample_data_with_missing.csv', index=False)
