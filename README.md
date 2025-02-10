# Dirty Store Transactions Data Cleaning

This project demonstrates how to clean a dirty dataset and store it in ORC format using Python and PySpark.

## 🚀 Features
- Cleaning messy store transaction data
- Removing special characters from string columns
- Converting currency fields to numerical format
- Writing clean data in ORC format

## 📁 Repository Structure
- `clean_data_script.py` → Python script for data cleaning
- `setup.md` → Step-by-step guide for setting up the environment
- `solutions.md` → Detailed explanation of the cleaning process

## 🔧 Prerequisites
- Python 3 installed with PySpark
- Dataset downloaded from:
  ```
  https://github.com/erkansirin78/datasets/raw/master/dirty_store_transactions.csv
  ```

## 🏗️ Running the Cleaning Script
1. Install required libraries:
   ```bash
   pip install pyspark pandas
   ```

2. Run the cleaning script:
   ```bash
   python clean_data_script.py
   ```

3. The cleaned ORC file will be saved in the specified directory.
