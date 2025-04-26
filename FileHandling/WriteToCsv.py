import csv

# Data to write (list of lists/tuples)
data_to_write = [
    ['Name', 'Score', 'Subject'],
    ['David', 85, 'Math'],
    ['Eve', 92, 'Physics'],
    ['Frank', 78, 'Chemistry']
]

try:
    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write multiple rows at once
        csv_writer.writerows(data_to_write)
        # Or write row by row
        # csv_writer.writerow(['Grace', 88, 'Biology'])
    print("\nSuccessfully wrote data to output.csv")
except IOError as e:
    print(f"An error occurred writing output.csv: {e}")

# Using DictWriter (often more readable)
data_dict_to_write = [
    {'ID': 1, 'Product': 'Laptop', 'Price': 1200},
    {'ID': 2, 'Product': 'Mouse', 'Price': 25},
    {'ID': 3, 'Product': 'Keyboard', 'Price': 75}
]
fieldnames = ['ID', 'Product', 'Price'] # Define the header order

try:
    with open('products.csv', 'w', newline='') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        dict_writer.writeheader() # Write the header row
        dict_writer.writerows(data_dict_to_write)
    print("Successfully wrote dictionary data to products.csv")
except IOError as e:
    print(f"An error occurred writing products.csv: {e}")