---
layout: post
title: Bob's Python Testing Guide and Cheatsheet (Ft. Pytest)
categories: tutorial
---

## Note
I am currently using this post as a cheatsheet for my development. In the future, I will turn this into a tutorial. This current document is updated constantly and is not meant to be used as a tutorial but rather a "cheatsheet".

## Test types

### Expect a value
```python
assert full_occupancy_dir_cif_count == 2, "Not all expected files were copied."
```

### Expect no error 
```python
for cif_file_path in cif_file_path_list:
    try:
        preprocess_supercell_operation(cif_file_path)
    except Exception as e:
        assert False, f"An unexpected error occurred for {cif_file_path}: {str(e)}"
```

### Expect error to occur
```python
for cif_file_path in cif_file_path_list:
    with pytest.raises(Exception):
        preprocess_supercell_operation(cif_file_path)
```

## Folder and file management
```python
def get_file_count_from_directory(directory):
    return len(glob.glob(join(directory, "*.pdf")))
```

```python
def get_file_path_list_from_directory(directory):
    return glob.glob(os.path.join(directory, "*.pdf"))
```

```python
def remove_directories(directory_list):
    for direcotry in directory_list:
        if exists(direcotry):
            rmtree(direcotry)
```

```python
def move_files(to_directory, file_path_list):
    for file_path in file_path_list:
        move(file_path, to_directory)
```
```python
def remove_file(file_path):
    if exists(file_path):
       os.remove(file_path)
```

A test script for one of my files.

```python
import pandas as pd
import numpy as np
from filter.info import get_cif_folder_info
from os.path import join, exists
from util.folder import (
    remove_file,
    get_cif_file_count_from_directory
)

def test_cif_folder_info():
    base_dir = "test/info_cif_files"
    csv_file_path = join(base_dir, "csv", "info_cif_files_info.csv")
    
    # Setup
    remove_file(csv_file_path)
    initial_cif_file_count = get_cif_file_count_from_directory(base_dir)

    # Start
    get_cif_folder_info(base_dir, False)
    assert exists(csv_file_path), "CSV log file was not created."
    csv_data = pd.read_csv(csv_file_path)
    assert len(csv_data.index) == initial_cif_file_count, "CSV log does not match the # of moved files."

    # Test atom count
    URhIn_supercell_atom_count = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Number of atoms in supercell'].iloc[0]
    error_msg_supercell_atom_count = f"Incorrect number of atoms for URhIn, expected 206"
    assert URhIn_supercell_atom_count == 206, error_msg_supercell_atom_count

    # Test shortest distance from Excel
    error_msg_shortest_dist = "Incorrect shortest distance for URhIn, expected ~2.69678, got {urhIn_min_distance}"
    URhIn_shortest_dist = csv_data[csv_data['CIF file'] == 'URhIn.cif']['Min distance'].iloc[0]
    assert np.isclose(URhIn_shortest_dist, 2.69678, atol=1e-4), error_msg_shortest_dist

    # Cleanup
    remove_file(csv_file_path)
```

### Pytest Collectonly
In pytest, collectonly is a command-line option that allows you to quickly gather information about the test cases in your project without actually running them.

```bash
pytest --collect-only
pytest --collectonly tests/test_fixture.py
```

### Pytest Fixture
A fixture in pytest is a function that sets up a test environment before the tests run and cleans it up afterwards. This is extremely handy for handling repetitive tasks like establishing database connections, creating test data, or preparing system state before executing tests.

Our use of the `conftest.py` file is central to our fixture strategy. This special file is recognized by pytest and is used for sharing fixtures across multiple test files. By defining fixtures in conftest.py, we make them accessible to any test in the same directory or subdirectories without the need for imports.

```python
#conftest.py
import pytest

@pytest.fixture
def resource_setup():
    print("Setup resource")
    resource = {"data": 123}  # Setup code
    yield resource  # This value is passed to the test function
    # Teardown code follows
    print("Teardown resource")
    del resource

@pytest.fixture
def initial_value():
    return 5
```

```python
# test_fixture.py
import pytest

def square(num):
    return num * num

def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value**2

def test_using_fixture(resource_setup):
    assert resource_setup["data"] == 123
```

> No need for a `del` statement to release resources in pytest fixtures. Resource management is handled by the setup and teardown logic encapsulated within the fixture itself, using the pattern of initializing resources before yield and cleaning them up after `yield`.


### Get test coverage
```bash
pip install pytest-cov
pytest --cov

# create an html file
coverage html
```

### Path error

```
ERROR tests/test_format.py
ERROR tests/test_info.py
ERROR tests/test_occupancy.py
ERROR tests/test_supercell_size.py
ERROR tests/test_tags.py
```

If your project's directory isn't being recognized like above, you might need to add it to the PYTHONPATH environment variable. You can do this by running the following command in your terminal (adjust the path as necessary for your project):

```
export PYTHONPATH="${PYTHONPATH}:/Users/imac/Documents/GitHub/cif-cleaner-main"
```

## Concept of `yield`
```python
import pytest

@pytest.fixture
def setup_database():
    # Setup code for database, e.g., creating a temp test database
    print("Setting up database")

    yield  # Here you can return a database connection if needed

    # Teardown code for database, e.g., deleting the test database
    print("Tearing down database")
```

## Cheatsheet for command line
```bash
# Run tests marked as 'slow'
pytest -m slow

# Disable output capturing, allowing print statements to show up in the console
pytest -s

# Increase verbosity for more detailed test output
pytest -v

# Reduce verbosity for a more concise test output
pytest -q

# Control traceback printing for test failures (options: long, short, line, native, no, auto)
pytest --tb=style

# Report the durations of the N slowest tests
pytest --durations=N

# Measure code coverage (requires pytest-cov plugin)
pytest --cov

# Ignore a specific file or directory during test discovery
pytest --ignore=path

# Stop the test session after N failures
pytest --maxfail=num
```

```python
@pytest.mark.slow
def test_some_slow_process():
    # slow test logic here

@pytest.mark.fast
def test_quick_function():
    # fast test logic here

@pytest.mark.skip(reason="not implemented yet")
def test_feature_x():
    # test logic here

@pytest.mark.skip(reason="not implemented yet")
def test_feature_x():
    # test logic here

@pytest.mark.parametrize("input,expected", [(1, 2), (3, 4)])
def test_addition(input, expected):
    assert input + 1 == expected

@pytest.mark.usefixtures("setup_database")
def test_database_query():
    # use the fixtures 
```

## References
I have collected the examples from many places.

- https://www.youtube.com/watch?v=mTMu8AtdG-E
- https://docs.pytest.org/
- ChatGPT
