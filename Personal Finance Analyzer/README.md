# Personal Finance Analyzer

A Python-based Jupyter Notebook for analyzing personal finance transactions and gaining insights into spending habits.

## Overview

This project provides tools to analyze and visualize personal finance data from bank statements. It processes transaction data, categorizes expenses, and generates useful visualizations to help you understand your spending patterns.

## Features

- **Data Loading & Preprocessing**: Loads transaction data from CSV files and handles data cleaning
- **Expense Categorization**: Automatically categorizes transactions based on description keywords
- **Spending Analysis**:
  - Total spending by category
  - Monthly spending trends
  - Visualizations of spending patterns
- **Interactive Visualizations**: Uses Matplotlib to create clear, informative charts

## Prerequisites

- Python 3.6+
- Jupyter Notebook
- Required Python packages (install via `pip install -r requirements.txt`):
  - pandas
  - numpy
  - matplotlib

## Usage

1. Prepare your bank statement data in CSV format with the following columns:

   - Date
   - Description
   - Amount (negative for expenses, positive for income)
   - Category (optional, can be auto-filled)

2. Open `financeAnalyzer.ipynb` in Jupyter Notebook

3. Update the file path in the notebook to point to your bank statement CSV file

4. Run all cells to see the analysis and visualizations

## Example Output

The notebook will generate:

- Summary statistics of your transactions
- Total spending by category
- Monthly spending trends
- Visual charts showing spending distribution

## Customization

You can modify the `categorize()` function in the notebook to add or adjust the rules for how transactions are categorized based on your spending patterns.

## Contributing

Feel free to submit issues and enhancement requests. Pull requests are welcome!
