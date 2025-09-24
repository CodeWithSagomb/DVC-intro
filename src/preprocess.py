import pandas as pd
import json

# Load the data from the iris.json file
with open('iris.json', 'r') as f:
    data_list = json.load(f)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Perform a simple preprocessing step: multiply a feature by 2
# Use the correct key name from the JSON file: 'sepalLength'
df['sepalLength'] = df['sepalLength'] * 2

# Save the preprocessed data to a new CSV file
# The output will have the same column names as the input
df.to_csv('iris_clean.csv', index=False)

print("Data preprocessing complete. Saved to iris_clean.csv")