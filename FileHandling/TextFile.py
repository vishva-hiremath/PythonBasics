# Safely writing to a text file
try:
    with open('my_first_file.txt', 'w') as f:
        f.write("Hello, Python files!\n")
        f.write("This is the second line.")
    print("Successfully wrote to my_first_file.txt")
except IOError as e:
    print(f"An error occurred during writing: {e}")

# Safely reading from a text file
try:
    with open('my_first_file.txt', 'r') as f:
        # Read the entire file content
        content = f.read()
        print("\nReading the whole file:")
        print(content)

    # You can also read line by line
    print("\nReading line by line:")
    with open('my_first_file.txt', 'r') as f:
        for line in f:
            print(line.strip()) # .strip() removes leading/trailing whitespace (like the newline character)

except FileNotFoundError:
    print("Error: my_first_file.txt not found.")
except IOError as e:
    print(f"An error occurred during reading: {e}")