import json

try:
    with open('sample.json', 'r') as jsonfile:
        data = json.load(jsonfile) # Loads the entire file into a Python object (usually dict or list)
        print("\nSuccessfully read config.json:")
        print(data)
        for d in data:
            print(f"Printing Customer: {d['customer']['Number']}")
            print(f"First Name: {d['customer']['firstName']}")
            print(f"Number: {d['customer']['partnerDetails']['partnerAccountNumber']}")
except FileNotFoundError:
    print("Error: sample.json not found.")
# json.JSONDecodeError handles errors if the file isn't valid JSON
except json.JSONDecodeError:
    print("Error: sample.json contains invalid JSON.")
except IOError as e:
    print(f"An error occurred reading sample.json: {e}")
