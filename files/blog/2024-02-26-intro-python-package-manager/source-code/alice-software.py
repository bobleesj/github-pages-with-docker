# alice-software.py (Python v3.11 or higher and NumPy v1.26.3)
import numpy as np
import sys

# Get Python and Numpy verisons used in your computer
numpy_version = np.__version__
python_verison = sys.version_info
print("NumPy version:", numpy_version, "\nPython version:", python_verison)

# Determine version compatibility
if numpy_version == "1.26.3" and python_verison >= (3, 11):
    print("Good! Your NumPy version is 1.26.3 and your Python version is 3.11 or higher!")
else:
    print("FAIL to compile. Check your Python and NumPy versions")

