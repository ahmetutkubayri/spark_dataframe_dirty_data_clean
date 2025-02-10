# Solutions to Data Cleaning Tasks

This file contains solutions to the given data cleaning tasks.

## Q-1: Clean Data and Match the Given Schema

### 1.1 Expected Schema
```text
root
 |-- STORE_ID: string (nullable = true)
 |-- STORE_LOCATION: string (nullable = true)
 |-- PRODUCT_CATEGORY: string (nullable = true)
 |-- PRODUCT_ID: integer (nullable = true)
 |-- MRP: float (nullable = true)
 |-- CP: float (nullable = true)
 |-- DISCOUNT: float (nullable = true)
 |-- SP: float (nullable = true)
 |-- Date_Casted: date (nullable = true)
```

### 1.2 String Cleaning
All string columns were stripped of special characters and leading/trailing spaces.

### 1.3 Currency Cleaning
Currency symbols and special characters were removed from price columns.

### 2. Writing to ORC Format
The cleaned data was written in ORC format using PySpark.

### Execution
To run the script and generate cleaned data, execute:

```bash
python clean_data_script.py
```
