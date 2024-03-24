---
layout: post
title: How to distribute Python package via pip (Ft. Twine)
categories: tutorial
---

## Motivation

This guide provides steps for packaging your Python code and installing it via `pip`.

The tutorial should not take more than 5 minutes to follow.


## Folder structure

Begin by creating the following folder structure:

```
├── src/
│   └── bobtwine/
│       ├── __init__.py (package initialization file)
│       └── example.py (example module within the package)
│── setup.py
├── main.py (main script to run your package functionality, if needed)
└── README.md (README file with project info and documentation)
```

### Key Python files

Below are the contents for each of the Python files generated.

`setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name='bobtwine',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[],  # List your dependencies here
)
```

`example.py`:

```python
def square(number):
    return number**2
```

`main.py`:

```python
from bobtwine import example

value = example.square(2)
print(value) # 4
```

## Distribution process

Install `twine`. `twine` helps upload files to PyPI.

PyPI is an online repository for packages. pip communicates with PyPI to download packages.

```bash
# Install twine
pip install twine

# Generate distribution files for your package
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

Twine will prompt you for your API key. Register and generate an API key at [https://pypi.org/manage/account/](https://pypi.org/manage/account/) shown below.

![](/files/blog/2024-03-22-python-package-distribution/img/1.png)


Your Python package is available at [https://pypi.org/project/bobtwine/](https://pypi.org/project/bobtwine/).

![](/files/blog/2024-03-22-python-package-distribution/img/2.png)

## Downloading the package

In `main.py`, we will try to import `bobtwine`.

```bash
# Install bobtwine
pip install bobtwine==0.1

# Run main.py
python main.py  # This prints 4
```

## Source code

