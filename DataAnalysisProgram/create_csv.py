import csv
import random

# Define the number of data points
num_data_points = 100

# Generate sample data
data = []
data.append(["X", "Y", "Z"])  # Header row
for _ in range(num_data_points):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    z = random.uniform(0, 100)
    data.append([x, y, z])

# Define the CSV file name
csv_file_name = "scatter_data.csv"

# Write the data to the CSV file
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_name}' has been created.")
