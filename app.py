####################################
### Importing necessary libraries: ###
####################################

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



##########################
### Back-End Functions ###
##########################



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
    """Return all inventory items as a list of dictionaries"""                # Docstring        => Explains what the function does 

    is_csv_ready()                                                            # Function Calling => calls is_csv_ready() fuction, ensuring CSV exists before inventory_read_all() function tries to read 

    with open(csv_path, mode="r", encoding="utf-8", newline="") as csv_file:  # with statement   => opens CSV file in read mode, preparing to read each row
        reader = csv.DictReader(csv_file)                                     # Tells function to read each row of CSV as a dictionary (name:value)
        item_dictionary_list  = list(reader)                                  # Collects all the item dictionaries, orders them in a list 

    return item_dictionary_list                                               # Function Result Return => Function reads all rows, returning them as list of dictionaries 



# Function, that when called, checks all existing items in CSV, finding the highest ID
# Function then assigns the next number

def make_next_item_id():
    """Return next available numeric ID for Inventory item awaiting ID"""  # Docstring        => Explains what the function does 

    items = item_dictionary_list()                                         # Function calling => calls item_dictionary_list() which reads whole Inventory CSV file, returning list of dictionaries => saves function list to variable; items
    highest_id = 0                                                         # Begins tracking highest ID found in items, initialised to zero 

    for item in items:                                                     # Loop => this loop goes through (loops over) each item in the list (item in items)
        try:                                                               # Try => Begins appempts to convert items ID to an integer, it won't crash if it cant
            current_id = int(item.get("item_identification", "0") or "0")              # Tries to get item_id from dictionary , if empty it uses zero => converting id to integer 
            if current_id > highest_id:                                    # Checks if the current ID is the biggest its seen so far 
                highest_id = current_id                                    # Updates highest_id if current_id is biggest so far
        except ValueError:                                                 
            continue                                                       # Where item_id isn't a number, the function skips the row
    
    return str(highest_id + 1)                                             # Function returns the next available ID as a string 



# Function, that when called, adds (appends) a new row (item) to the inventory CSV file 
# Function does not delete/ overwrite any previous rows/ data when called

def add_new_row(row):
    """Add one new row to the Inventory CSV file without removig previous data"""  # Docstring => Explains what the function does
    
    is_csv_ready()                                                                 # Function Calling => makes sure CSV file exists before trying to open it and write new data to it 

    with open(csv_path, mode="a", encoding="utf-8", newline="") as csv_file:       # Opens CSV file in append mode => adding data to the end of the file => avoiding overwriting 
        writer = csv.DictWriter(csv_file, fieldnames=column_header)                # Setting up dictionary writer tool => matches values to correct column header 
        writer.writerow(row)                                                       # Writes new dictionary row of data into CSV file 
 


###########################
### Front-End Functions ###
###########################



# Function that, when called, enables user to intput new item into the inventory CSV file 
# Function collects the data (using input), ckecks the data is valid => then adds data to new appended row in the CSV file 

def add_item_to_inventory():
    """Collect inputted item data via user input and add new entry to inventory CSV file """                           # Docstring => Explains what the function does
  
    print("\n***Add a New Item to Inventory***")                                                                       # Prints heading on console to make text clear

    # Collecting user inputs 

    item_name      = input("Enter Item Name: ").strip()                                                                # User Item name input field => .strip() removes extra spaces before/after name 
    quantity_unit  = input("Enter Unit of Quantity: ").strip() or "units"                                              # Unit input field => if left blank, defaults to "units"
    username       = input("Enter Username: ").strip()                                                                 # Records user who added item

    # Quantity Validation Loop - Keeps asking until valid number entered 

    while True: 

        quantity_input = input("Enter Item Quantity (Whole Integer): ").strip()                                        # Quantity input field => stored as text 

    # Checks if input is a valid integer (including negative numbers)
 
        try:
            quantity = int(quantity_input)                                                                             # Attempt to convert input to integer 
            if quantity > 0:                                                                                                                                      
                break                                                                                                  # Valid positive number => Loop ends 
            else:
                print("***NEGATIVE NUMBER or ZERO DETECTED: QUANTITY MUST BE A WHOLE INTEGER GREATER THAN ZERO***\n")  #If integr isn't a decimal (can't be) it must be a negative number 
        except ValueError:                                                                                             # ValueError triggers if python interpreter couldn't convert quantity_input into an integer 
            if "." in quantity_input:                                                                                  # Checks specifically if the quantity_input is a decimal
                print("***DECIMAL DETECTED: QUANTITY MUST BE A WHOLE INTEGER GREATER THAN ZERO***\n")
            else:                                                                                                      # Covers all other invalid inputs 
                print("***INVALID INPUT: QUANTITY MUST BE A WHOLE INTEGER GREATER THAN ZERO***\n")

    # Creating dictionary (for Inputted Item) which matches CSV column headers 

    new_row = {
        "item_identification" : make_next_item_id(),                                                                   # Creates next unique ID number 
        "item_name"           : item_name,
        "item_quantity"       : str(quantity),                                                                         # Stores as string, so is written to CSV in correct format
        "item_unit"           : quantity_unit, 
        "name_of_inputter"    : username,
        "date_inputted"       : datetime.now().strftime("%Y-%m-%d")                                                    # Records today's date in CSV file 
        }
    
    add_new_row(new_row)                                                                                               # Adds new dictionary row to CSV file
    print("***Item Successfully added to Fylde Aero Inventory Management System***")



# Function, that when called, will read the inventory as a list of dictionaries, and then delete an item from the inventory using the Item ID

def delete_item_from_inventory(): 
    """Removes an item from the CSV file using items ID"""                                                                 # Docstring => Explains what the function does
 
    # Read all items into a list  
    items = item_dictionary_list()                                                                                          # Calls function that reads every line of CSV file and turns them into list of dictionaries

    # Check if inventory has items available for deletion - if empty, function ends early    
    if not items:
        print("\n***Inventory is Empty - No Items to Delete***\n")
        return 
        
    # Begin Item deletion process - gain Item ID from user via input 
    print("\n***Delete Item***\n")
    item_id_to_delete = input("Enter the ID of the Item you would like to delete: ").strip()

    # Check if Item ID exists 
    item_exists = False                                                                                                      # item_exists checks if the given ID exists in the list - initially set to false 
    updated_items = []                                                                                                       # updated_items holds all the items which should stay in CSV 

    for item in items:                                                                                                       # goes through every item in inventory dictionary list, if current ID matches deletion request ID, it skipped (not coppied to updated_items list)
        if item.get("item_identification") == item_id_to_delete:                                             
            item_exists = True 
            print(f"Item '{item.get('item_name')}' has been deleted for the Fylde Aero Inventory System") 
        else:
            updated_items.append(item)

    if not item_exists:                                                                                                       # if loop ends and no match is found, it tells the user that the ID doesn't exist - stops function 
        print("\n***No Item found with that ID***\n")
        return 

    # Write Updated list back to CSV file 
    with open("inventory.csv", mode="w", newline="") as csv_file:                                                             # Opens CSV in Write Mode, erasing old content - writes column headers, then writes all remaining (non-deleted) items 
        fieldnames = ["item_identification", "item_name", "item_quantity", "item_unit", "name_of_inputter", "date_inputted"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_items)

    print("\n***Fylde Aero Inventory Updated Sucessfully***\n")                                                               # Success message - know deletion worked

    

# Function, that when called, will display all inventory items, in a column-aligned formatted table 

def display_inventory():
    """Show all inventory enteries in column aligned-table format"""                                                      # Docstring => Explains what the function does

    print("\n***Inventory Item Display***")

    all_items = item_dictionary_list()                                                                                    # Reads all of inventory rows into a list of dictionaries 

    if len(all_items) == 0:                                                                                               # Checks if the list is empty 
        print("***The Fylde Aero Inventory Management System is empty***")
        return
    
    # Print table headers with their aligment 
    print(f"{'Identification':<6} {'Item Name':<35} {'Quantity':<10} {'Item Unit':<12} {'Username':<20} {'Date Inputted':<20}")  # Prints table headers with their allignment 
    print("-" * 110)
    # loop through each item and print the data in aligned columns 

    for item in all_items:                                                                                                  # Loops through each inventory row => getting the value for each field of each dictionary 
        print(
            f"{item.get('item_identification', ''):<5} "  
            f"{item.get('item_name', ''):<25} "  
            f"{item.get('item_quantity', ''):<10} "  
            f"{item.get('item_unit', ''):<10} "  
            f"{item.get('name_of_inputter', ''):<15} "  
            f"{item.get('date_inputted', '')} "  
        )

    print()                                                                                                                  # Blank Line left for readability
    
################################                                                                                                                
### Inventory Start Function ###
################################

# Function, that, when called will give the user a number of options => enabling them to decide what they would like to do with the Inventory Management System 
# This function is the main program loop => runs the inventory system 

def start_inventory_system():
    """Main function that runs the menu and handles user choices"""

    is_csv_ready()                                                                  # Makes sure CSV file exists before trying to perform any action requiring CSV

    while True:                                                                     # Keeps program running until user decided to quit 
        print ("\n --- Fylde Aero Inventory Management System Main Menu --- ")      # Shows menu options available to user 
        print ("1) Add New Item to inventory")
        print ("2) View All Inventory Items")
        print ("3) Delete an Item ")
        print ("4) Exit Inventory")

        user_decision = input("Enter your choice (1/2/3/4): ").strip()               # Asks user what the want to do with the system => takes in their answer as an input 

        # Option 1 : Add Item

        if user_decision == "1":
            add_item_to_inventory()

        # Option 2 : Display Items

        elif user_decision == "2":
            display_inventory()

        # Option 3 : Delete an Item

        elif user_decision == "3":
            delete_item_from_inventory()

        # Option 4 : Exit Program 

        elif user_decision == "4":
            print("\n Exiting Fylde Aero Inventory Management System - Goodbye!\n")
            break

        # Invalid Choice Handling 
        else:
            print("*** Invalid Choice - Please enter 1, 2, 3 or 4 ***\n")

        
if __name__ == "__main__":                                                   # Ensures program only runs if this file is the one being executed directly 
    start_inventory_system()
