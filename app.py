# Importing necessary modules:
    # csv      => to read/write to CSV files
    # os       => enables python to interact with the operating system (e.g. checking files, creating folders, ect.)
    # datetime => enables me to work with dates and times in my code 

import csv, os 
from datetime import datetime 

# Defining CSV  file path and column headers:
    # CSV_PATH => path to the inventory CSV file 
    # COLUMNS  => headers for the inventory CSV file (columns of inventory table)

CSV_PATH = "inventory.csv"
COLUMNS = ["item_id", "item_name", "quantity", "unit", "added_by", "date_added"]

# Function, that when called, checks the CSV file exists and has headers 
# If the file is missing or empty, create it and write column headers

def ensure_csv_ready(): 
    """Create the CSV with a header if it doesn't exist or is empty."""  # Docstring      - Explians what function does 
    if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:   # if Statement   - Checks if CSV file doesn't exist or is empty
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:     # with statement - opens CSV file in write mode (creating CSV if it doesn't exist) 
            csv.writer(f).writerow(COLUMNS)                              # Writes header row (Column names) to CSV

