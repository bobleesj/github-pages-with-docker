---
layout: post
title: Python static type checking tutorial (Ft. MyPy)
categories: python
---

## Motivation

Software tools are built upon broadly defined as functions. Functions are reusable blocks of code. The better we manage and use functions, the more efficient and our code becomes. `Numpy`, for example, provide functions that enhance productivity. 

Functions enhance our productivity. Before any, we must *write* excellenct functions. Functions that are **(1) clear**, **(2) descriptive**, **(3) concise** in that order.

Type checking is one way to attain the above goals by providing attributes to functions.

> Here, I limit my introduction to functions. Type checking is broadly applicable to variables, classes, properties, methods, enums, etc.


## Toy examles

Functions that we know what is required and what is returns explicitly across documentation and the function block itself.

We write functions. Functions may require a parameter(s). For those who are new to types, let us first briefly 

```python
def print_hello_world(name):
    print(f"Hello, {name}!")
```

Above, the parameter required is `name`. But we may also explicitly define that the type of `name` must be `str`.

```python
def print_hello_world(name: str):
    print(f"Hello, {name}!")
```

If you have a returning value, you can assign `-> str` to write it.

```python
def return_hello_world(name: str) -> str:
    return f"Hello, {name}!"
```

This was a toy example for beginners. Let us provide a real-example that I used in my own resaerch code for publications.


## Real examples

```python
def generate_random_numbers(
    count: int, low: int | float, high: int | float, is_float=True
):
    """
    Generate a list of random numbers (floating-point or integer).
    """
    if is_float:
        return [random.uniform(low, high) for _ in range(count)]
    else:
        return [random.randint(int(low), int(high)) for _ in range(count)]
```

```python
def test_generate_min_distance_histogram():
    # Generate 100 random minimum distances between 2.0 Å and 4.0 Å
    min_dists = generate_random_numbers(100, 2.0, 4.0)
    generate_histogram(min_dists, output_dir_path, distance_settings)
```

```python
def test_generate_supercell_size_histogram():
    # Generate 100 random atom counts between 1000 to 3000
    atom_counts = generate_random_numbers(100, 1000, 3000, is_float=False)
    generate_histogram(atom_counts, output_dir_path, supercell_settings)
```

## Dyanmic vs static type checking

I used to write extensive tutorials on the `Swift` programming langauge. Swift is the main language for iOS/MacOS applications. The main difference between `Swift` and `Python` the requirement to know the types such as `bool`, `float` for every function variables. In Python, it is possible to have

```python
my_name = None

# sleep for 2 seconds
time.sleep(2)

my_name = "Bob"
```

In Python, we call this dynamic typing, where the type of `my_name` is not assignment but later assigned as `str`. Hence, we call this **dynamic type checking** in Python

But, in `Swift`, the above would not compile because it has to know the type in advance and the type can not be changed. Hence, we must have it as, and this is **static type chking** in Swift.

```python
# my_name is a string before compiling
my_name = "Bob"
```


