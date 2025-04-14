# --- Example 1: Simple 'if' ---
temperature = 35

print("Checking temperature...")
if temperature > 30:
    print("It's a hot day! Stay hydrated.") # This line runs because 35 > 30 is True

print("Weather check complete.") # This line always runs



2
3
4
5
6
7
8
9
10
# --- Example 2: 'if-else' ---
age = 17

print("Checking voting eligibility...")
if age >= 18:
    print("You are eligible to vote.")
else: # Executes if the 'if' condition (age >= 18) is False
    print("You are not yet eligible to vote.")

print("Eligibility check complete.")

# --- Example 3: 'if-elif-else' ---
score = 75

print("Calculating grade...")
if score >= 90:
    grade = "A"
elif score >= 80: # Checked only if score < 90
    grade = "B"
elif score >= 70: # Checked only if score < 80
    grade = "C" # This condition is True (75 >= 70)
elif score >= 60:
    grade = "D"
else: # Executes if score < 60
    grade = "F"

print(f"Your grade is: {grade}") # Output: Your grade is: C


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
# --- Example 4: Looping through a list ---
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits: # 'fruit' takes the value of each item in 'fruits' one by one
    print(f"- {fruit}")

# --- Example 5: Looping through a string ---
message = "Hello"
print("\nCharacters in the message:")
for char in message:
    print(f"- {char}")

# --- Example 6: Looping a specific number of times using range() ---
print("\nCounting to 5:")
for i in range(5): # range(5) generates numbers 0, 1, 2, 3, 4
    print(f"Number: {i}")


# --- Example 7: Looping through a simple dataset (list of dictionaries) ---
student_data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

print("\nProcessing student data:")
for student in student_data: # Each 'student' is a dictionary
    # Access data using dictionary keys
    name = student["name"]
    score = student["score"]
    print(f"Processing {name}...")
    if score >= 80:
        print(f"  {name} passed with a score of {score}.")
    else:
        print(f"  {name} needs improvement with a score of {score}.")

# --- Example 8: Simple 'while' loop ---
count = 0
print("\nUsing a while loop:")
while count < 5: # Condition: loop as long as count is less than 5
    print(f"Count is: {count}")
    count = count + 1 # IMPORTANT: Update the variable used in the condition!

print("While loop finished.")


2
3
4
5
6
7
8
9
10
11
# --- Example 9: Defining and calling a simple function ---

# Define the function
def greet(name): # 'name' is a parameter (input)
    """This function greets the person passed in as a parameter.""" # Docstring (optional but good practice)
    print(f"Hello, {name}! Nice to meet you.")

# Call the function
print("Calling the greet function:")
greet("Alice") # "Alice" is the argument passed to the 'name' parameter
greet("Bob")

# --- Example 10: Function that returns a value ---

# Define the function
def add_numbers(num1, num2):
    """This function adds two numbers and returns the sum."""
    result = num1 + num2
    return result # Sends the value of 'result' back to where the function was called

# Call the function and store the result
print("\nCalling the add_numbers function:")
sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}") # Output: The sum is: 8

another_sum = add_numbers(100, 50)
print(f"Another sum is: {another_sum}") # Output: Another sum is: 150


# --- Example 11: Combining functions, loops, and conditionals ---

# Define a function to process a single student's data
def process_student(student_record):
    """Processes a student dictionary and prints their status."""
    name = student_record["name"]
    score = student_record["score"]
    print(f"Processing {name}...")
    if score >= 80:
        status = "Passed"
        print(f"  Status: {status} (Score: {score})")
    else:
        status = "Needs Improvement"
        print(f"  Status: {status} (Score: {score})")
    # We could also return the status if needed elsewhere
    # return status

# Our dataset from before
student_data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 65}
]

print("\nProcessing student data using a function:")
# Loop through the data and call the function for each student
for student in student_data:
    process_student(student) # Call the function for each dictionary

print("\nData processing complete.")
