from datetime import datetime
from gzip import READ
from operator import add
import csv
import os


GCT_RATE = 0.15
STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05
BULK_DISCOUNT_THRESHOLD = 2500.00
BULK_DISCOUNT_AMOUNT = 200.00
POINTS_PER_100 = 1
REDEEM_COST = 50
FREE_COFFEE_CODE = "B04"          # Regular Coffee (price overwritten to 0 on redeem)
MANAGER_PIN = "1234"
MENU_FILE = "menu.csv"
LOYALTY_FILE = "loyalty.csv"
ORDERS_FILE = "orders.csv"
MIN_QUANTITY = 1
MAX_QUANTITY = 20
MONEY_FORMAT = "${:,.2f} JMD"

# PART A: Menu and Order Functions
def get_menu():
    """
    Returns the default menu as a dictionary keyed by item code.

    Returns:
        dict: code -> {"name": str, "category": str, "price": float}
    """
    menu = {
        "C01": {"name": "Regular Coffee", "category": "c", "price": 350.00},
        "C02": {"name": "Cappuccino", "category": "Hot Drinks", "price": 550.00},
        "C03": {"name": "Hot Chocolate", "category": "Hot Drinks", "price": 450.00},
        "D01": {"name": "Iced Latte", "category": "Cold Drinks", "price": 600.00},
        "D02": {"name": "Fruit Smoothie", "category": "Cold Drinks", "price": 750.00},
        "D03": {"name": "Bottled Water", "category": "Cold Drinks", "price": 150.00},
        "F01": {"name": "Beef Patty", "category": "Food", "price": 400.00},
        "F02": {"name": "Chicken Sandwich", "category": "Food", "price": 850.00},
        "F03": {"name": "Banana Muffin", "category": "Food", "price": 300.00},
        "F04": {"name": "Ackee and Saltfish Wrap", "category": "Food", "price": 950.00},
        
    }
    return menu
#READ
#add

#creating the function defintion for display menu(); This is responsible for showing the menu items
def display_menu(menu):
    #creating and formatting the Menu title
    print("-" * 80)
    #centering the starter menu ins the terminal
    print("STARTER MENU".center(80))
    print("-" * 80)
    
    #adding a new line for display purposes 
    print("\n")
    #adding the category title for Hot Drinks
    print("\nHOT DRINKS\n".center(100))
    #formatting the headers for organizational puposes using format specifiers
    print(f"{'Item Code':<20}{'Item Name':<30}{'Category':<20}{'Price(JMD)':<10}")
    print("-" * 80)
    
    #accessing each item in the dictionary using the for loop for iterating over each item and the items function to get the key value pair
    for itemcode, details in menu.items():
        #using a if statement so that we can easily organise each category
        if details["category"] == "Hot Drinks":
            #using format specifiers so that we can format the details of the product and ensure that it is inline with the headers
            print(f"{itemcode:<20} {details['name']:<30} {details['category']:<20} ${details['price']:<20.2f}")
    print("\n")
    print("\nCOLD DRINKS\n")
    print(f"{'Item Code':<20}{'Item Name':<30}{'Category':<20}{'Price(JMD)':<10}")
    print("-" * 80)
    
    #using for loop to acess the key value pair in the menu dictionary
    for itemcode, details in menu.items():
        if details["category"] == "Cold Drinks":
            print(f"{itemcode:<20} {details['name']:<30} {details['category']:<20} ${details['price']:<20.2f}")

    print("\n")
     #adding the category title for Hot Drinks
    print("\nFOOD\n")
    print(f"{'Item Code':<20}{'Item Name':<30}{'Category':<20}{'Price(JMD)':<10}")
    print("-" * 80)
    for itemcode, details in menu.items():
        if details["category"] == "Food":
            print(f"{itemcode:<20} {details['name']:<30} {details['category']:<20} ${details['price']:<20.2f}\n")
 
#Invoking the display menu function

def display_main_menu():
    print("\n")
    print("-" * 80)
    print("WELCOME TO BREW & BYTE CAFE".center(80))
    print("Campus Ordering System".center(80))
    print("=" * 80)
    print("\n")
    print("""1.View Menu\n2.Add Item to Order \n3.Remove Item from Order\n4.View Current Order\n5.Update Item Quantity\n6.Checkout \n7.Cancel Order\n8.Manager Options\n0.Exit
          """)
    print("-" * 80)    



#defining the get_menu_choice function
def get_menu_choice(min_option,max_option):
    #The while loop will continue to execute once the condition is true
    while True:
        #try is implememented here to exceute the code
        try:
            #the user will enter their which action they would like to carry out
            menu_action = int(input("Enter your choice:  "))
            #This checks to see if the user entered a valid range
            if menu_action >= min_option and menu_action <= max_option:
                #stops the loop and sends back the valid selection to where the function was called
                return menu_action
            else: 
                #If the user enter a invalid range, an error message will be displayed
                print(f"Invalid Selection, Please enter a value between {min_option} and {max_option}")
        #This catches any invalid data type and displays an error message        
        except ValueError:
            print("Invalid input! Please enter a numeric option.")
           
 
 
def add_item(order,menu, item_code, quantity=1):
    '''
    Add an item to the customer's existing order
    '''
    try:
        #convert the quanity variable to an integer
        quantity = int(quantity)
        
        #quantity check
        if quantity<=0:
            print("Quantity must be greater than zero")
            #stops the function if the condition is not met
            return
        #Since, menu is a dictionary the 'in' opertor checks whether the item code exists as a key in the menu dictionary
        if item_code in menu:
            #order is a dictinary, that contains the customers order the in operator also checks to if the item_code exist in the customers' order
            if item_code in order:
                #retrieving the value using it keys.
                order[item_code] +=quantity
            else:
                #If the item code does not already exist in the order, this code block adds it as a new item with the specified quantity.
                order[item_code]= quantity
            #Displays a message to the user
            print("Item added sucessfully!")
        else:
            #print an error message to the user if the code does not exist
            print("Inavlid item code")
    
    except ValueError:
        print("Invalid quantity. please enter a whole number")
            

def remove_item(order, code):
    #check to see is empty
    if order == {}:
        print("Your order is empty")
        #stop the execution of the code if the order is empty
        return
    #check the code that is in the order the; the in key word return a true or false value. It is is true the code block is exceuted
    if code in order:
        #The pop() method removes an item in the customer's order by it keys
        order.pop(code)
        print("Item removed sucessfully!")
    else:
        #if the item code does not exist in the order
        print("Item is not in your order.")
    
def view_item(order, menu):
    print("need to be worked on")
    
def view_item(order, menu): 
    #check to see the customer has any items in their cart
    if order == {}:
        print("Your order is empty")
        #if the cart is empty the code stops executing
        return 
    #Looping through the customers' order
    print("\n")
    print("YOUR CURRENT ORDER".center(80))
    print("\n")
    #List item headers
    print(f"{'Item':<25}{'Quantity':<15}{'Unit Price':<15}{'Line Total(JMD)':<20}")
    print("=" * 80)
    #looping through orders
    for item_code, quantity in order.items():
        #Displaying the customer order using f string formatter
        print(f"{menu[item_code]['name']:<25} {quantity:<15}{menu[item_code]['price']:<15.2f}${quantity * menu[item_code]['price']:<15.2f}")
        print("_"*80)


def update_quantity(order, item_code):
    
   	#Checks whether the order dictionary is empty.
    if order == {}:
        print("Your Order is empty")
        return
    
    #Checking whether the item_code exists in the customer's. 
    if item_code in order:
        try:
            #The user will enter the updated quantity here.
            new_quantity = input("Enter new quantity: ")
            #change the data type from a string to integer
            new_quantity = int(new_quantity)
            #	Ensures the quantity is greater than 0 before updating
            if new_quantity > 0:
                #accessing the order key_value pair
                order[item_code] = new_quantity
                print("Quantity Updated")
            else:
                print("Quantity must be greater than zero")
        except ValueError:
            #Ensure the user enters a valid input without crashing the code
            print("Please Enter a valid whole number.")     
    else:
        #	Prints a message if the item does not exist
        print("Item not found in your order")
    

def main():
    order = {}
    menu = get_menu()
    while True:
        display_main_menu()
        menu_selection = get_menu_choice(0, 8)
        if menu_selection ==1:
            display_menu(menu)
        elif menu_selection ==2:
            while True:
                item_code = input("Enter item Code ('done' to finish):  ")     
                if item_code.lower() == "done":
                    break
                quantity = input("Enter quantity: ")
                add_item(order,menu, item_code, quantity)
                print(order)                 
        elif menu_selection ==3:
            while True: 
                item_code = input("Enter item Code to remove('done' to finish): ")
                if item_code.lower() == "done":
                    break
                remove_item(order, item_code)             
        elif menu_selection ==4:
             view_item(order,menu)       
        elif menu_selection ==5:
                item_code = input("Enter item code to update:  ")
                update_quantity(order, item_code)
        elif menu_selection ==6:
            None
        elif menu_selection == 7:
            print("feature is not available")
        elif menu_selection ==8:
            print("feature not available as yet")
        elif menu_selection==0:
            print("Exiting System Goodbye :)")
            break
        else:
            print("Please enter a valid selection")   
main() 

# Part B (billing, Discounts, Validation)
def calculate_subtotal(order, menu):
    if order == {}:
        print("Order is empty")
        return
    #subtotal accumalator
    subtotal = 0
    
    #looping through the order item and using the items method to loop through for the key_value pairs
    for item_code, quantity in order.items():
        unit_price = menu[item_code]["price"]
        line_total = quantity * unit_price
        subtotal +=line_total
    #send the final calculated subtotal back to where the function was called    
    return subtotal
  
def calculate_discount(subtotal, customer_type):
    """
    Returns the discount amount for the given customer type.
    Parameters:
        subtotal (float): subtotal before discount.
        customer_type (str): "student", "staff" or "regular".

    Returns:
        float: discount amount.
    """
    discount = 0.0
    if customer_type == "student":
        discount += subtotal * STUDENT_DISCOUNT
    elif customer_type == "staff":
        discount += subtotal * STAFF_DISCOUNT
    if subtotal >= BULK_DISCOUNT_THRESHOLD:
        discount += BULK_DISCOUNT_AMOUNT
    return discount

def calculate_tax(amount, rate=GCT_RATE):
    """
    Returns the GCT on the given amount.

    Parameters:
        amount (float): taxable amount.
        rate (float): tax rate (default GCT_RATE).

    Returns:
        float: tax amount.
    """
    return amount * rate

def calculate_total(order, menu, customer_type):
    """
    Calculates subtotal, discount, tax and total.

    Parameters:
        order (dict): code -> quantity.
        menu (dict): menu dictionary.
        customer_type (str): "student", "staff" or "regular".

    Returns:
        tuple: (subtotal, discount, tax, total)
    """
    subtotal = calculate_subtotal(order, menu)
    discount = calculate_discount(subtotal, customer_type)
    taxable = subtotal - discount
    tax = calculate_tax(taxable)
    total = taxable + tax
    return subtotal, discount, tax, total

def get_valid_quantity(prompt):
    """
    Prompts until the user enters a whole number from 1 to 20.

    Parameters:
        prompt (str): message to display.

    Returns:
        int: validated quantity.
    """
    while True:
        raw = input(prompt).strip()
        try:
            qty = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if MIN_QUANTITY <= qty <= MAX_QUANTITY:
            return qty
        print(f"Quantity must be between {MIN_QUANTITY} and {MAX_QUANTITY}.")

def get_valid_code(prompt, menu):
    """
    Prompt until the user enters a code that exists in the menu.
    Accepts upper or lower case.

    Parameters:
        prompt (str): message to display.
        menu (dict): the menu dictionary.

    Returns:
        str: a valid uppercase item code.
    """
    while True:
        code = input(prompt).strip().upper()
        if code in menu:
            return code
        print(f"Invalid code '{code}'. Please enter a code from the menu.")

def get_yes_no(prompt):
    """
    Return True for y/yes and False for n/no; re-prompts otherwise.

    Parameters:
        prompt (str): message to display.

    Returns:
        bool: user's answer.
    """
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")

# PART C: (Loyalty, Reports and Integration)
# Loads the menu from a CSV file. If the file is missing or broken, it falls back to the default menu.
def load_menu(filename):
    # Check if the file exists before trying to open it
    if not os.path.exists(filename):
        print(f"Warning: menu file '{filename}' not found. Using default menu.")
        return get_menu()
    menu = {}
    try:
        # Open the CSV file and use DictReader to read rows as dictionaries
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line_no, row in enumerate(reader, start=2):
                try:
                      # Extract and clean the data from each row
                    code = row["code"].strip().upper()
                    menu[code] = {
                        "name": row["name"].strip(),
                        "category": row["category"].strip(),
                        "price": float(row["price"])
                    }
                except (KeyError, ValueError, AttributeError):
                     # If a row is formatted badly, skip it and warn the user instead of crashing
                    print(f"Warning: skipping badly formatted line {line_no} in '{filename}'.")
    except OSError as exc:
         # Catch file read errors (like permission issues) and fall back safely
        print(f"Warning: could not read '{filename}' ({exc}). Using default menu.")
        return get_menu()
    # If the file was empty, fall back to the default menu
    if not menu:
        print(f"Warning: menu file '{filename}' was empty. Using default menu.")
        return get_menu()
    return menu

# Reads the loyalty members from a CSV file and returns them as a dictionary.
def load_loyalty(filename):
    members = {}
    if not os.path.exists(filename):
        return members
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for line_no, row in enumerate(reader, start=1):
                if not row or not row[0].strip():
                    continue
                try:
                    member_id = row[0].strip().upper()
                    name = row[1].strip()
                    points = int(row[2])
                    members[member_id] = {"name": name, "points": points}
                except (IndexError, ValueError):
                    print(f"Warning: skipping badly formatted line {line_no} in '{filename}'.")
    except OSError as exc:
        print(f"Warning: could not read '{filename}' ({exc}).")
    return members

# Saves the current loyalty members dictionary back to the CSV file.
def save_loyalty(filename, members):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for member_id, info in members.items():
                writer.writerow([member_id, info["name"], info["points"]])
    except OSError as exc:
        print(f"Warning: could not save loyalty file '{filename}' ({exc}).")

# Prompts the manager to add a new member and assigns them a unique ID.
def register_member(members):
    name = input("Enter member name: ").strip()
    # Don't allow empty names
    if not name:
        print("Error: name cannot be empty.")
        return members
    # Generate a unique ID by starting at M001 and counting up
    number = 1
    while f"M{number:03d}" in members:
        number += 1
    member_id = f"M{number:03d}"
    # Add the new member to the dictionary with 0 points
    members[member_id] = {"name": name, "points": 0}
    print(f"Registered {name} with member ID {member_id}.")
    return members

# Adds loyalty points based on how much the customer spent.
def award_points(members, member_id, amount_spent):
    member_id = member_id.upper()
    # Make sure the member actually exists before giving points
    if member_id not in members:
        print(f"Error: member '{member_id}' not found.")
        return 0
    earned = int(amount_spent // 100) * POINTS_PER_100
    members[member_id]["points"] += earned
    return earned

# Redeems points for a free coffee if the member has enough.
def redeem_points(members, member_id, order):
    member_id = member_id.upper()
     # Check if the member exists
    if member_id not in members:
        return False
    if members[member_id]["points"] < REDEEM_COST:
        return False
    # Deduct the points and add a free coffee to the order
    members[member_id]["points"] -= REDEEM_COST
    order[FREE_COFFEE_CODE] = order.get(FREE_COFFEE_CODE, 0) + 1
    return True

# Saves a completed order to the orders CSV file.
def save_order(filename, order, totals):
    subtotal, discount, tax, total = totals
    try:
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["datetime", "items", "subtotal", "discount", "tax", "total"])
                # Format the order items into a single string (e.g., "C01:2;F01:5")
            items_str = ";".join(f"{code}:{qty}" for code, qty in order.items())
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                items_str,
                f"{subtotal:.2f}",
                f"{discount:.2f}",
                f"{tax:.2f}",
                f"{total:.2f}",
            ])
    except OSError as exc:
        print(f"Warning: could not save order to '{filename}' ({exc}).")

# Reads the saved orders from the CSV file so the manager report can calculate totals.
def load_orders(filename):
    orders = []
     # If the file doesn't exist, return an empty list
    if not os.path.exists(filename):
        return orders
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for line_no, row in enumerate(reader, start=1):
                if not row or row[0].strip() == "datetime":
                    continue
                try:
                    # Convert the saved items string back into a dictionary
                    items = {}
                    if row[1].strip():
                        for part in row[1].split(";"):
                            code, qty = part.split(":")
                            items[code.strip()] = int(qty)

                    # Rebuild the order dictionary and add it to the list
                    orders.append({
                        "datetime": row[0],
                        "items": items,
                        "subtotal": float(row[2]),
                        "discount": float(row[3]),
                        "tax": float(row[4]),
                        "total": float(row[5]),
                    })
                except (IndexError, ValueError):
                    print(f"Warning: skipping badly formatted order line {line_no}.")
    except OSError as exc:
        print(f"Warning: could not read orders file '{filename}' ({exc}).")
    return orders

# Calculates the daily report (order count, revenue, tax, best-seller) from the list of orders.
def generate_daily_report(orders):
    report = {
        "order_count": len(orders),
        "total_revenue": 0.0,
        "total_tax": 0.0,
        "best_selling_item": "N/A",
    }
    item_totals = {}
     # Loop through every saved order
    for record in orders:
    # Add to the total revenue and tax
        report["total_revenue"] += record.get("total", 0.0)
        report["total_tax"] += record.get("tax", 0.0)
        # Count how many of each item were sold
        for code, qty in record.get("items", {}).items():
            item_totals[code] = item_totals.get(code, 0) + qty
    if item_totals:
        report["best_selling_item"] = max(item_totals, key=item_totals.get)
    return report

# Prints the daily sales report on the screen in a neat format.
def display_report(report, menu=None):
    print("\n" + "=" * 45)
    print("DAILY SALES REPORT".center(45))
    print("=" * 45)
    print(f"Number of orders : {report['order_count']}")
    print(f"Total revenue    : {MONEY_FORMAT.format(report['total_revenue'])}")
    print(f"Tax collected    : {MONEY_FORMAT.format(report['total_tax'])}")
    # If we have the menu, show the name of the best-selling item along with its code
    best = report["best_selling_item"]
    if menu and best in menu:
        best = f"{menu[best]['name']} ({best})"
    print(f"Best-selling item: {best}")
    print("=" * 45)

# Interactive helpers
# Asks the user what type of customer they are (Student, Staff, or Regular).
def get_customer_type():
    print("Customer type: 1) Student  2) Staff  3) Regular")
    choice = get_menu_choice(1, 3)
    return {1: "student", 2: "staff", 3: "regular"}[choice]

# Asks for the item code and quantity, then calls add_item.
def handle_add_item(order, menu):
    item_code = get_valid_code("Enter item code: ", menu)
    quantity = get_valid_quantity(f"Enter quantity ({MIN_QUANTITY}-{MAX_QUANTITY}): ")
    return add_item(order, menu, item_code, quantity)

# Asks for the item code and calls remove_item.
def handle_remove_item(order, menu):
    if not order:
        print("Your order is empty; nothing to remove.")
        return order
    code = get_valid_code("Enter item code to remove: ", menu)
    remove_item(order, code)
    return order

# Shows the order, asks for an item code, and calls update_quantity.
def handle_update_quantity(order, menu):
    if not order:
        print("Your order is empty; nothing to update.")
        return order
    view_item(order, menu)
    code = get_valid_code("Enter item code to update: ", menu)
    return update_quantity(order, code)

# Manages the entire checkout process: customer type, loyalty, receipt, and saving.
def handle_checkout(order, menu, members):
    if not order:
        print("Cannot checkout: your order is empty.")
        return order
    # Ask for customer type
    customer_type = get_customer_type()
    # Handle loyalty member check
    member_id = None
    if get_yes_no("Is the customer a loyalty member? (y/n): "):
        entered = input("Enter member ID: ").strip().upper()
        if entered in members:
            member_id = entered
        else:
            print(f"Member '{entered}' not found; treating as non-member.")
    # Offer redemption if they have enough points
    if member_id and members[member_id]["points"] >= REDEEM_COST:
        prompt = (f"{members[member_id]['name']} has {members[member_id]['points']} points. "
                  f"Redeem {REDEEM_COST} for a free Regular Coffee? (y/n): ")
        if get_yes_no(prompt):
            if redeem_points(members, member_id, order):
                print("Free Regular Coffee added to the order.")
    # Calculate the final totals
    totals = calculate_total(order, menu, customer_type)
    # Print the receipt for the customer
    print_receipt(order, menu, totals, customer_type)
    # Give them a chance to cancel before saving
    if not get_yes_no("Confirm payment? (y/n): "):
        print("Checkout cancelled. Your order is still open.")
        return order
    # Save the order to the CSV file
    save_order(ORDERS_FILE, order, totals)
    if member_id:
        earned = award_points(members, member_id, totals[3])
        print(f"{earned} point(s) awarded to {members[member_id]['name']}. "
              f"New balance: {members[member_id]['points']}.")
        save_loyalty(LOYALTY_FILE, members)
    print("Payment complete. Thank you!")
    return {}

# The Manager sub-menu, protected by a PIN.
def handle_manager_options(menu, members):
    pin = input("Enter manager PIN: ").strip()
    if pin != MANAGER_PIN:
        print("Incorrect PIN. Access denied.")
        return members # Kick them back to the main menu

# Loop the manager menu until they choose 0 to exit
    while True:
        print("\nMANAGER OPTIONS")
        print("1. View daily sales report")
        print("2. Register loyalty member")
        print("3. View loyalty members")
        print("0. Return to main menu")
        choice = get_menu_choice(0, 3)
        if choice == 0:
            return members
        if choice == 1:
            # Load the orders from the file and generate the report
            orders = load_orders(ORDERS_FILE)
            display_report(generate_daily_report(orders), menu)
        elif choice == 2:
            # Register a new member and save the updated list
            members = register_member(members)
            save_loyalty(LOYALTY_FILE, members)
        elif choice == 3:
            # Print the list of all registered members
            if not members:
                print("No loyalty members registered.")
            else:
                print("\nLOYALTY MEMBERS")
                print(f"{'ID':<8}{'Name':<24}{'Points':>8}")
                for mid, info in members.items():
                    print(f"{mid:<8}{info['name']:<24}{info['points']:>8}")
