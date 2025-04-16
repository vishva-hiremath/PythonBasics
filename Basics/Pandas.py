import pandas as pd
import numpy as np # Often used together!

# --- Creating a Pandas Series ---
print("--- Pandas Series ---")
my_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(my_series)
print("Value at index 'b':", my_series['b'])

# --- Creating a Pandas DataFrame ---
print("\n--- Pandas DataFrame ---")
# From a dictionary (keys become column names)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)

# --- Viewing Data ---
print("\n--- Viewing Data ---")
print("First 2 rows (head):")
print(df.head(2)) # Show the first N rows (default 5)

print("\nLast 2 rows (tail):")
print(df.tail(2)) # Show the last N rows (default 5)

print("\nDataFrame Info:")
df.info() # Get concise summary (dtypes, non-null counts)

print("\nDescriptive Statistics:")
print(df.describe()) # Get summary statistics for numerical columns

# --- Selecting Data ---
print("\n--- Selecting Data ---")
# Select a single column (returns a Series)
ages = df['Age']
print("Selecting the 'Age' column:")
print(ages)
print("Type:", type(ages))

# Select multiple columns (returns a DataFrame)
name_city = df[['Name', 'City']]
print("\nSelecting 'Name' and 'City' columns:")
print(name_city)

# Select rows by label (index) using .loc
print("\nSelecting row with index 1 (using .loc):")
print(df.loc[1])

# Select rows by integer position using .iloc
print("\nSelecting row at position 2 (using .iloc):")
print(df.iloc[2])

# Select specific rows and columns
print("\nSelecting Name and Age for rows 0 and 2:")
print(df.loc[[0, 2], ['Name', 'Age']])

# --- Basic Manipulation ---
print("\n--- Basic Manipulation ---")
# Adding a new column
df['Salary'] = [50000, 60000, 75000, 55000]
print("DataFrame with added 'Salary' column:")
print(df)

# Filtering data (basic condition)
print("\nFiltering for Age > 30:")
print(df[df['Age'] > 30])