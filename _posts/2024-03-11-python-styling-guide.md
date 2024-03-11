---
layout: post
title: Python styling guide and automation
categories: cheatsheet
---

### Motivation

I have started to refactor my code and implement tests at a project level. It is time for me to check my work agaisnt the convention followed by the Python community.

> Many examples are derived from personal Python projects, Google's Python style guide and the official PEP 8 guide. Examples have been modified to enhance my understanding and learning.

### Automate formatting

I encountered two auto Python formatting tools known as `yapf` and `black`

```bash
$ pip install yapf
$ yapf --in-place main.py

$ pip install black
$ black main.py
```

#### Black or yapf

![Black Python VS Code](/files/blog/2024-03-11-python-styling-guide/1.png)

I have decided to use `Black` for two. reasons. First, `Black` does not offer customization but the line lenght. Second, `Black` is faster.

To summarize:

1. `yapf` scales quadratically ([Case 1](https://github.com/google/yapf/issues/39), [Case 2](https://github.com/google/yapf/issues/264))
2. `Black` produces deterministic codes amongst collaborators by design so the team does not argue on single quote vs. double quote, etc. No "point" of argument. ([Case 1](https://www.reddit.com/r/Python/comments/sidqze/black_vs_yapf_vs/?rdt=61802))
3. `Black` is used by Facebook, Dropbox Lyft, Tesla. ([README.md](https://github.com/psf/black?tab=readme-ov-file))
4. `Black` is one of the official Python community projects.

I can simply run `black folder-name`.

```bash
$ black postprocess 
reformatted /Users/imac/Documents/GitHub/cif-bond-analyzer/postprocess/writer.py
reformatted /Users/imac/Documents/GitHub/cif-bond-analyzer/postprocess/excel.py
reformatted /Users/imac/Documents/GitHub/cif-bond-analyzer/postprocess/histogram.py
```

To change the line-width,

```bash
black -l 80 tests
```

To lint multiple files and folders,

```bash
black -l 80 postprocess preprocess tests util main.py filter
```

or simply 

```bash
bash-l 80 src
```

### Line-Width

I have noticed that every linter often has a differnt line-width limitation. PEP 8 concludes:

> *"Some teams strongly prefer a longer line length. For code maintained exclusively or primarily by a team that can reach agreement on this issue, it is okay to increase the line **length limit up to 99 characters**, provided that **comments and docstrings are still wrapped at 72 characters**." https://peps.python.org/pep-0008/#maximum-line-length*

#### My decision line-width

I chose the 80 character limit. I have two reasons. First, I do not use a dual monitor to minimize neck strain and mouse usage. Second, I carry a laptop as a student. I want to maximize productivity using the limited screen real estate. I must be able to view content with Temrinal and two panels open.


### Format

```python
# :( longer than 80 characters per line
excel_file_path = os.path.join(output_dir, f"{folder_name}_{pair_tpye}pairs.xlsx")

# :| works but wrong position of parenthesis
excel_file_path = os.path.join(
	output_dir, f"{folder_name}_{pair_tpye}pairs.xlsx")

# :) 
excel_file_path = os.path.join(
	output_dir, f"{folder_name}_{pair_tpye}pairs.xlsx"
)
```


### Comprehensions

```python
# :(
result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

# :)
result = [
      is_valid(metric={'key': value})
      for value in interesting_iterable
      if a_longer_filter_expression(value)
  ]
```

> Examples from Google's Python style guide section 2.7. Modified for my understanding.

### Conditional Statements

If short, make a single line.

```python
# :( no need for 2 lines
bad_line_breaking = ('yes' if predicate(value) else
                    'no')
# :) 
one_line = 'yes' if predicate(value) else 'no'
```

If long, do not clutter the inner parenthesis.

```python
# :( function inside makes it hard to read
portion_too_long = ('yes'
                    if some_long_module.some_long_predicate_function(
                     really_long_variable_name)
                    else 'no, false, negative, nay')
# :)
one_line = 'yes' if predicate(value) else 'no'
```

Split into two lines if necessary.

```python
# :| long and two lines ok but no
slightly_split = ('yes' if predicate(value)
                    else 'no, nein, nyet')
```

The longest version possible, if only needed.

```python
# :| extra long, but ok
the_longest_ternary_style_that_can_be_done = (
    'yes, true, affirmative, confirmed, correct'
    if predicate(value)
    else 'no, false, negative, nay')
```

> Example from Google's Python style guide section 2.11


### Dictionary

```python
# :(
d = {'hello': 'world'}
if d.has_key('hello'):
    print(d['hello'])  
else:
    print('default_value')

# :)
d = {'hello': 'world'}
print(d.get('hello', 'default_value')) 
print(d.get('thingy', 'default_value'))

# :)
if 'hello' in d:
    print(d['hello'])
```

> Example from https://docs.python-guide.org/

### References

- PEP 8 – Style Guide for Python Code (https://peps.python.org/pep-0008/)
- https://google.github.io/styleguide/pyguide.html
- https://docs.python-guide.org/