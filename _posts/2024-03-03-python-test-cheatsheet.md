---
layout: post
title: Bob's Python Testing Cheatsheet (Ft. Pytest, Pandas)
categories: tutorial
---

## Note
I am currently using this post as a cheatshet for my development. In the future, I will turn this into a tutorial.

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



