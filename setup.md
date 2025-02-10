# Environment Setup Guide

This document provides a step-by-step guide to setting up the Python environment for the data cleaning task.

## Step 1: Install Python & Required Libraries
Ensure Python is installed and install the required libraries:

```bash
pip install pyspark pandas
```

## Step 2: Download Dataset
The dataset should be downloaded from the following link:

```
https://github.com/erkansirin78/datasets/raw/master/dirty_store_transactions.csv
```

Move the downloaded file to your working directory.

## Step 3: Running the Script
Execute the data cleaning script:

```bash
python clean_data_script.py
```

The cleaned dataset will be saved in ORC format.
