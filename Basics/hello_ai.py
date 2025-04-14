print("Hello, AI World!")

#Assigning a string (text) to a variable named 'greeting'
greeting = "Hello, AI World!"

# Assigning an integer (whole number) to a variable named 'training_examples'
training_examples = 1000

# Assigning a float (decimal number) to a variable named 'learning_rate'
learning_rate = 0.01

# Let's see what's inside our boxes!
print(greeting)
print(training_examples)
print(f"learning_rate: {learning_rate}")

message = "Processing text data..."
word_count = 55
accuracy = 0.95
is_processed = True
tokens = ["natural", "language", "processing"]

print(type(message))       # Output: <class 'str'>
print(type(word_count))    # Output: <class 'int'>
print(type(accuracy))      # Output: <class 'float'>
print(type(is_processed))  # Output: <class 'bool'>
print(type(tokens))        # Output: <class 'list'>


# Our input text (a string)
raw_text = "AI helps us understand language."
print(f"Original Text: {raw_text}") # f-strings are a neat way to print variables!

# Splitting the string into a list of words (tokens)
# The .split() method is built-in for strings!
tokens = raw_text.split()
print(f"Tokens (List): {tokens}")

# Accessing individual tokens using list indexing (starts from 0!)
first_token = tokens[0]
third_token = tokens[2]
print(f"First Token: {first_token}")
print(f"Third Token: {third_token}")

# Finding the number of tokens (length of the list)
num_tokens = len(tokens) # len() is a built-in function
print(f"Number of Tokens: {num_tokens}")

# Adding a new token (lists are mutable!)
tokens.append(".") # Add punctuation
print(f"Tokens after adding punctuation: {tokens}")


#Some more examples for defining variables
#Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
print(a, b)