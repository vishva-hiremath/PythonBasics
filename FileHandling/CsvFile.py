import csv
import pandas as pd

try:
    with open('/Users/aa949501/Downloads/Duplicate_Status_For_Day.csv', 'r', newline='') as csvfile: # newline='' is important!
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader) # Read the header row
        print(f"Header: {header}")
        print("Data Rows:")
        for row in csv_reader:
            # Each row is a list of strings
            print(row)
except FileNotFoundError:
    print("Error: data.csv not found.")
except Exception as e:
    print(f"An error occurred: {e}")

df = pd.read_csv('/Users/aa949501/Downloads/Duplicate_Status_For_Day.csv');
print(df)