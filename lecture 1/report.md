# Python Scripts Summary

This document summarizes the Python scripts created in the Operation-analytics project.

## Scripts Overview

### 1. name.py
A simple interactive script that:
- Asks the user for their name using `input()`
- Prints a personalized greeting: "Hello, {name}."

**Usage:** `python name.py`

---

### 2. read_sales.py
A data processing script that:
- Reads sales data from `sales.csv` using the standard `csv` module
- Calculates the total revenue by summing all monthly revenues
- Prints the total revenue

**Features:**
- Uses Python's built-in `csv` module
- Skips the header row when processing data
- Converts revenue strings to integers for calculation

**Usage:** `python read_sales.py`

---

### 3. functions.py
A script demonstrating function definition and testing:
- Defines `yearly_cost(monthly_cost)` function that returns monthly cost multiplied by 12
- Includes two assertions to verify function correctness:
  - `yearly_cost(100) == 1200`
  - `yearly_cost(0) == 0`
- Calls the function with 100 and prints the result (1200)

**Usage:** `python functions.py`

---

## Data Files

### sales.csv
Contains monthly sales data with the following structure:
- Column headers: `month,revenue`
- Data rows: Monthly revenue figures for January through April

## Summary
All scripts use only standard Python libraries and are designed for beginner-level understanding. They cover basic Python concepts including:
- User input/output
- File I/O and CSV processing
- Function definition and testing with assertions
