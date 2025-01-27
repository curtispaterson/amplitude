import json
import pandas as pd

# Load the JSON file
filename = r"C:\Users\CurtisPaterson\Documents\GitHub\amplitude\data\product.txt"
with open(filename, 'r') as file:
    data = json.load(file)

# Normalize JSON to flatten nested structures
df = pd.json_normalize(data)

# Dynamically handle arrays in columns by checking if the column contains an array
for column in df.columns:
    if isinstance(df[column].iloc[0], list):  # Check if the column contains a list/array
        df = df.explode(column)  # Explode arrays into separate rows

# Display the structured table
print(df)

# Save to a CSV file (optional)
df.to_csv('output.csv', index=False)
