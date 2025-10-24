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