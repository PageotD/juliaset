[![Python 3.8](https://github.com/PageotD/juliaset/actions/workflows/python3-8.yaml/badge.svg?branch=develop)](https://github.com/PageotD/juliaset/actions/workflows/python3-8.yaml)

![BSD 3-Clause License](https://img.shields.io/badge/%20License%20-BSD%203--Clause-informational)

# juliaset
A simple random Julia set generator.

Can take some time to run, so be patient !

## Installation

```bash
https://github.com/PageotD/juliaset.git
pip install ./juliaset --use-feature=in-tree-build
```

## Some examples

```python
# Import julia from the juliaset module
from juliaset import julia

# Create a new set with all default parameters
newset1 = julia()

# Run the newset. It should result in the creation of a new image file
# named newset1.png
newset1.run(fname='newset1')

# Create a new set with some parameters
# size = 512 will generate a 512x512 pixel image
# norm = False means no normalization will be performed before plotting
newset2 = julia(size=512, norm=False)
```