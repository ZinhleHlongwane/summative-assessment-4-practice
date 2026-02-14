# Assessment 4 – Python Summative Practice (Group Fork Repo)

This repository is a **summative practice assessment** designed to prepare students for  
Assessment 4.

It follows the **same structure and testing style** used in previous assessments.

---

## Learning Outcomes Assessed

- Loops  
- Functions  
- Algorithms  
- Command Line Commands  
- Data Structures  
- Data Manipulation  
- String Formatting  

---

## Instructions

1. Fork this repository to your own GitHub account  
2. Clone your fork to your local machine  
3. Create and activate a virtual environment (recommended)  
4. Install the dependencies  
5. Implement the required functions inside the `problems/` folder  
6. Do **not** modify any test files  
7. Run the tests until all tests pass  

---

## Setup

Check that Python is installed:

```bash
python --version
or

python3 --version
```

--- 

## Create a virtual environment


Create a virtual environment:

```bash
python -m venv venv
```

---


## Install dependencies:

```bash
pip install pytest
```

---


## How to Run Tests

- Run tests from the project root.

- Run all tests (full summative simulation):

```bash
python -m pytest
```

---

# Run tests per section
## Loops:

```bash
python -m pytest tests/test_loops.py -v
```

## Functions:

```bash
python -m pytest tests/test_functions.py -v
```

## Algorithms:

```bash
python -m pytest tests/test_algorithms.py -v
```

## Command Line Commands:

```bash
python -m pytest tests/test_cli_tools.py -v
```

## Data Structures:

```bash
python -m pytest tests/test_data_structures.py -v
```

## Data Manipulation:

```bash
python -m pytest tests/test_data_manipulation.py -v
```

## String Formatting:

```bash
python -m pytest tests/test_strings.py -v
```

