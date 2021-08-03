[![Python 3.8](https://github.com/PageotD/juliaset/actions/workflows/python3-8.yaml/badge.svg?branch=develop)](https://github.com/PageotD/juliaset/actions/workflows/python3-8.yaml)

![BSD 3-Clause License](https://img.shields.io/badge/%20License%20-BSD%203--Clause-informational)

# juliaset
A simple random Julia set generator. Can take some time to run, so be patient !

This is a small personal project I did to apply some of the skills I learned during my DevOps career transition training.

This package is not initially intended to be distributed and is therefore not present on the Python Package Index ([PyPi](https://pypi.org/)). However, if you wish, you can clone it, fork it, modify it etc. within the limits of the license.

## Installation

Clone the repository:
```bash
https://github.com/PageotD/juliaset.git
```

Install julia using `pip`:
```bash
pip install ./juliaset --use-feature=in-tree-build
```

Or using `poetry`:
```bash
poetry install ./juliaset
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
```

![newset1](https://raw.githubusercontent.com/PageotD/juliaset/develop/docs/images/juilaset-output-example.png)

```python
# Import julia from the juliaset module
from juliaset import julia

# Create a new set with all default parameters
newset2= julia()

# Create a new set with some parameters
# size = 512 will generate a 512x512 pixel image
# norm = False means no normalization will be performed before plotting
newset2 = julia(mirror=True)

# Run the newset. It should result in the creation of a new image file
# named newset2.png
newset2.run(fname='newset2')
```

![newset2](https://raw.githubusercontent.com/PageotD/juliaset/develop/docs/images/juilaset-output-mirror-example.png)

## Parameters

- `size`: size of the array in height and width (not of the output image), default `size=256`
- `dpi`: _dot per inch_ for the output image, default `dpi=300`
- `norm`: normalize the julia set by its maximum value, default `norm=True`
- `mirror`: mirroring the julia set horizontally and vertically, default `mirror=False`
- `escrad`: escape radius, default `escrad=3`
- `niter`: maximum number of iterations, default `niter=250`

## Useful links

- https://en.wikipedia.org/wiki/Julia_set
