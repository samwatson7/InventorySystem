# Importing necessary modules:
    # csv      => to read/write to CSV files
    # os       => enables python to interact with the operating system (e.g. checking files, creating folders, ect.)
    # datetime => enables me to work with dates and times in my code 

import csv, os 
from datetime import datetime 

# Defining CSV  file path and column headers:
    # csv_path      => path to the inventory CSV file 
    # column_header => headers for the inventory CSV file (columns of inventory table)

csv_path      = "inventory.csv"
column_header = ["item_identification", "item_name", "item_quantity", "item_unit", "name_of_inputter", "date_inputted"]

# Function, that when called, checks the CSV file exists and has headers 
# If the file is missing or empty, create it and write column headers

def is_csv_ready(): 
    """Create the CSV with a header if CSV doesn't already exist / CSV is empty"""   # Docstring      => Explians what function does 

    file_not_exist = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0  # variable to check if CSV file exits or doesnt exist/is empty

    if file_not_exist:
        with open(csv_path, mode="w", encoding="utf-8", newline="") as csv_file:     # if statement says "if the CSV file doesn't exist/ is empty => Create CSV file and input column headers"
            writer = csv.writer(csv_file)                                            # creates a CSV writer => writes into CSV file 
            writer.writerow(column_header)                                           # Tells the writer to write the header row (column names) on CSV file 

# Function, that when called, reads all inventory items in CSV file 
# Function then returns a list of dictionaries => each row in CSV becomes a dictionary

def item_dictionary_list():
    """Return all inventory items as a list of dictionaries"""            # Docstring        => Explains what the function does 
    is_csv_ready()                                                        # Function Calling => calls is_csv_ready() fuction, ensuring CSV exists before inventory_read_all() function tries to read 
    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:  # with statement   => opens CSV file in read mode, preparing to read each row
        reader = csv.DictReader(file)                                     # Tells function to read each row of CSV as a dictionary (name:value)
        item_dictionary_list  = list(reader)                              # Collects all the item dictionaries, orders them in a list 
    return item_dictionary_list ()                                        # Function Result Return => Function reads all rows, returning them as list of dictionaries 

