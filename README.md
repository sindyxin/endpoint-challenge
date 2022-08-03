# Challenge

Implement commands that allow a user to create, move and delete directories.

## Installation

Check if python have installed in local

```bash
python3 --version
```

or

```bash
python --version
```

Any version of Python can be downloaded from Python Software Foundation website at python.org.

## Run

Open terminal and then type in python, or python3 depending on your Python installation, and python file name with .py then hit Enter.

```bash
python3 directories.py
```

or

```bash
python directories.py
```

## Output

```bash
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
fruits
  apples
    fuji
grains
vegetables
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist
DELETE foods/fruits/apples
LIST
foods
  fruits
  grains
  vegetables
    squash
```
