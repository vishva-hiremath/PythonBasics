import numpy as np

# --- Creating NumPy Arrays ---

# From a Python list
my_list = [1, 2, 3, 4, 5]
np_array_from_list = np.array(my_list)
print("Array from list:", np_array_from_list)
print("Type:", type(np_array_from_list))

# Create an array with a range of numbers
np_range = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
print("Array using arange:", np_range)

# Create an array of zeros or ones (specify shape)
np_zeros = np.zeros((2, 3)) # Shape: 2 rows, 3 columns
print("Array of zeros:\n", np_zeros)

np_ones = np.ones(4) # Shape: 4 elements (1D)
print("Array of ones:", np_ones)

# --- Basic Array Attributes ---
print("\n--- Array Attributes ---")
print("Shape:", np_array_from_list.shape) # Dimensions of the array
print("Data Type:", np_array_from_list.dtype) # Type of elements
print("Number of Dimensions:", np_array_from_list.ndim) # Number of axes

# --- Basic Operations (Element-wise) ---
print("\n--- Basic Operations ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a)
print("b:", b)
print("a + b:", a + b)       # Element-wise addition
print("a * 2:", a * 2)       # Scalar multiplication
print("a > 1:", a > 1)       # Element-wise comparison

# --- Indexing and Slicing ---
print("\n--- Indexing and Slicing ---")
my_array = np.arange(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original array:", my_array)
print("Element at index 3:", my_array[3])
print("Elements from index 2 to 5 (exclusive):", my_array[2:5])
print("Elements from index 5 onwards:", my_array[5:])
