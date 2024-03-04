---
layout: post
title: Python Best Practices and Cheatsheet (Ft. Numpy, Sympy)
categories: tutorial
---

Due to the nature of scientific coding, where we often focus on achieving the final result within a limited time frame, I have prioritized producing the outputs. Now that the code has matured in terms of features to be built, I have decided to study and apply best practices in Python. I will use this documentation as the main reference to refactor and improve my code.

This blog post is constantly updated. Examples here are acquired from online sources and documentation, as noted in the references section."

## Section 1. Best practices

### `isClose` instead of `round` for comparing values

```python
# Returns True or False
URhIn_shortest_dist = 2.6967
print(np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4)) # True

URhIn_shortest_dist = 2.670
print(np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4)) # False
```

### Merge two dictionaries using `|`

```python
# Define two dictionaries with different keys
person_details = {"name": "Bob", "age": 56}
person_location = {"city": "New York", "country": "USA"}

# Merge the two dictionaries
merged_dict = person_details | person_location

print(merged_dict)
# {'name': 'Bob', 'age': 56, 'city': 'New York', 'country': 'USA'}
```

### Get most common elements and count from list

```python
from collections import Counter

# Define the list with different numbers
my_list = [15, 15, 15, 7, 7, 3, 12, 12, 12, 12, 12]

# Create a Counter object to count the frequencies of each element in the list
counter = Counter(my_list)

# Find the two most common elements
most_common = counter.most_common(2)

# Find the two most common elements
most_common = counter.most_common(1)
print(most_common)
# [(12, 5)]

two_most_common = counter.most_common(2)
print(two_most_common)
# [(12, 5), (15, 3)]
```

### Sort dictionary with lambda function

```python
# Sort complex iterables with sorted()
data = [
    {"name": "Alice", "age": 12},
    {"name": "Bob", "age": 56},
    {"name": "Charlie", "age": 17}
]

sorted_data = sorted(data, key=lambda x: x["age"])

print(sorted_data)
# [{'name': 'Alice', 'age': 12}, {'name': 'Charlie', 'age': 17}, {'name': 'Bob', 'age': 56}]
```

### Use enumerate instead of range for loop

```python
# List data
my_list = [1, 2, 3]

# :( 
for i in range(len(my_list)):
    print(i, my_list[i])

# :) - Get both index and value in the loop
for idx, num in enumerate(my_list):
    print(idx, num)
```

### enumerate for dict

```python
# Dictionary data
my_dict = {'a': 1, 'b': 2, 'c': 3}

# :( - Iterating over a dictionary without using enumerate
for key in my_dict:
    print(key, my_dict[key])

# :) - Using enumerate to get both the index and key-value pairs in the loop
for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)

# If index is not needed
for key, value in my_dict.items():
    print(index, key, value)
```

### Comprehensions

A comprehension in Python is a concise syntax for constructing a new sequence based on the values from an existing sequence or iterable.

```python
# Dictionary comprehension
dict_comp = {i: (i + 1) ** 2 for i in range(5)}

# List comprehension
list_comp = [(x + 1) ** 2 for x in range(5)]

# Set comprehension
set_comp = {(i + 3) % 5 for i in range(5)}

print("Dict Comprehension:", dict_comp)
print("List Comprehension:", list_comp)
print("Set Comprehension:", set_comp)
# Dict Comprehension: {0: 1, 1: 4, 2: 9, 3: 16, 4: 25}
# List Comprehension: [1, 4, 9, 16, 25]
# Set Comprehension: {0, 1, 2, 3, 4}
```

## Section 2. NumPy

### Create array

```python
# Create an empty 1D array
arr_1d = np.arange(10)
# [0, 1, ..., 8, 9]
arr_1d = np.empty(5)
# [0, 0, 0, 0, 0]

# Create an empty 2D array
arr_2d = np.empty((3, 4))
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
```

### Reshape array

```python
arr_1d = np.arange(10)
arr_2d = arr_1d.reshape((5, 2)) # 5 rows, 2 cols
```

### Broadcast

#### Example 1. Constant addition

```python
# Create a 2D array (e.g., 3x3)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Constant to add
constant = 10

# The constant is "broadcast" across the 2D array, adding it to every element
result = arr_2d + constant
```

#### Example 2. Addition between two arrays

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_1d = np.array([1, 0, -1])

# The 1D array is broadcast across each row of the 2D array
result = arr_2d + arr_1d
print(result)
# Output:
# [[2 2 2]
#  [5 5 5]
#  [8 8 8]]

arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
arr_1d = np.array([1, 2])
```

#### Example 3. Multiplication between two arrays

```python
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
arr_1d = np.array([1, 2])

result = arr_2d * arr_1d
print(result)
# Output:
# [[ 1  4]
#  [ 3  8]
#  [ 5 12]]
```

### Apply universal functions

```python
arr = np.array([1, 2, 3, 4, 5])
result_add = np.add(arr, 10)  # Adds 10 to each element
result_multiply = np.multiply(arr, 2)  # Multiplies each element by 2
result_sin = np.sin(arr)  # Computes the sine of each element
```

## Section 3. Prompt

### Get user input with option selection

```python
# Get the directory of the script being executed
script_directory = os.path.dirname(os.path.abspath(__file__))

print("\nWelcome! Please choose an option to proceed:")

options = {
    "1": "Move files based on unsupported CIF format",
    "2": "Move files based on unreasonable distance",
    "3": "Move files based on tags",
    "4": "Move files based on supercell atom count",
    "5": "Copy files based on atomic occupancy and mixing",
    "6": "Get file info in the folder",
    "7": "Check CIF folder content against Excel file"
}

# Print options
for key, value in options.items():
    print(f"[{key}] {value}")

# Get user input
choice = input("Enter your choice (1-7): ")

if choice in options:
    print(f"You have chosen: {options[choice]}\n")
else:
    print("Invalid choice!")
    return
```

### Choose folder containing specific file type

```python
# Allows the user to select a directory from the given path.
# Here, I list folders containing .cif
def choose_CIF_directory(directory):
    directories = [d for d in os.listdir(directory) 
                   if os.path.isdir(join(directory, d)) 
                   and any(file.endswith('.cif') for file in os.listdir(join(directory, d)))]
    
    if not directories:
        print("No directories found in the current path containing .cif files!")
        return None

    print("\nAvailable folders containing CIF files:")

    for idx, dir_name in enumerate(directories, start=1):
        num_of_cif_files = get_cif_file_count_from_directory(dir_name)
        print(f"{idx}. {dir_name}, {num_of_cif_files} files")

    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the folder containing .cif files: "))
            if 1 <= choice <= len(directories):
                return join(directory, directories[choice-1])
            else:
                print(f"Please enter a number between 1 and {len(directories)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
```

## Section 4. Pandas

### Read CSV

```python
csv_file_path = join(base_dir, "csv", "info_cif_files_info.csv")
csv_data = pd.read_csv(csv_file_path)
# 'CIF file' column matches 'URhIn.cif' and selects the 'Min distance' column
# iloc[0] refers to the first element
URhIn_min_dist = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Min distance'].iloc[0]
```

### Save CSV

```python
def save_to_csv_directory(folder_info, df, base_filename):
    """
    Saves the dataframe as a CSV inside a 'csv' sub-directory of the provided folder.
    """
        
    csv_directory = join(folder_info, "csv")
    if not os.path.exists(csv_directory):
        os.mkdir(csv_directory)

    # Extract the name of the chosen folder
    folder_name = os.path.basename(folder_info)

    # Set the name for the CSV file based on the chosen folder
    csv_filename = f"{folder_name}_{base_filename}.csv"

    # Save the DataFrame to the desired location (within the 'csv' sub-directory)
    df.to_csv(join(csv_directory, csv_filename), index=False)

    print(csv_filename, "saved")
```

## Section **5**. Math

### Sympy

Generate symbolic answers

```python
import sympy as sp

# Define the symbols
a11, a12, a21, a22, t11, t12, t21, t22 = sp.symbols('a11 a12 a21 a22 t11 t12 t21 t22')

# Define the matrix A and its inverse A_inv
A = sp.Matrix([[a11, a12], [a21, a22]])
A_inv = A.inv()

# Define the matrix T
T = sp.Matrix([[t11, t12], [t21, t22]])

# Calculate the transformed matrix T' using the formula T' = A * T * A_inv
T_prime = A * T * A_inv

# Extract the elements of the transformed matrix T'
T_prime_elements = T_prime.tolist()

# Output the elements of T' as a list of lists (matrix form)
print(T_prime_elements) # Symbolic answers
# [[-a21*(a11*t12 + a12*t22)/(a11*a22 - a12*a21)...]]
```

## Other topics not covered

- Matplotlib
- Generator for memory management
- Scipy - Optimization
- Logging

## Other tips

- Do not import specific functions, but modules
- Do not use getter/setter if it does not add any extra value

## Source Code

[Google Codelab](https://colab.research.google.com/drive/1vgFlN-33wQKpQFoG1aaiRklZnNidlZtK?usp=sharing)

## References

- https://www.youtube.com/watch?v=qUeud6DvOWI
- https://google.github.io/styleguide/pyguide.html