from gzip import READ
from operator import add
from csv import DictReader , writer, reader
from os import path 
from datetime import datetime


GCT_RATE = 0.15
STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05
BULK_DISCOUNT_THRESHOLD = 2500.00
BULK_DISCOUNT_AMOUNT = 200.00
#point awarded for every 100 that is spent
POINTS_PER_100 = 1
#Reedem cost for the coffee
REDEEM_COST = 50
#Free coffee code variable used when the a loyalty member ga
FREE_COFFEE_CODE = "C01"          # Regular Coffee (price overwritten to 0 on redeem)
#manager pin that would authorize the manager acess
MANAGER_PIN = "brewsscaffee@2026"
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
        "C01": {"name": "Regular Coffee", "category": "Hot Drinks", "price": 350.00},
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
    
    
    
def view_order(order, menu): 
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
    #Displating subtotal
     # Display subtotal
    subtotal = calculate_subtotal(order, menu)
    print(f"{'ORDER SUBTOTAL:':<55}${subtotal:,.2f}")

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
    This is a simple yes/ no prompt function, which allows the user to select yes or no
    depending on where the function was invoked
    """
    while True:
       #user input
       answer = input(prompt).strip().lower()
       
       #conditional checks
       if answer == "y" or answer == "yes":
           return True
       elif answer == "n" or answer == "no":
           return False
       else:
           #if the user did not select one of the valid answer
           print("Please enter yes or no")

def print_receipt(order, menu, totals, customer_type):
    """
    Print a formatted receipt showing every line item and the four totals.

    Parameters:
        order (dict): code -> quantity.
        menu (dict): the menu dictionary.
        totals (tuple): (subtotal, discount, tax, total).
        customer_type (str): "student", "staff" or "regular".

    Returns:
        None
    """
    subtotal, discount, tax, total = totals
    print("\n" + "=" * 55)
    print("BREW & BYTE CAFE".center(55))
    print("=" * 55)
    for code, qty in order.items():
        item = menu.get(code)
        if item is None:
            continue
        line = item["price"] * qty
        print(f"{item['name']:<24}x{qty:<4}{f'${line:,.2f}':>20}")
    print("-" * 55)
    print(f"{'Subtotal':<40}{f'${subtotal:,.2f}':>15}")
    if discount > 0:
        label = f"Discount ({customer_type} + bulk)" if subtotal >= BULK_DISCOUNT_THRESHOLD else f"Discount ({customer_type})"
    else:
        label = "Discount"
    print(f"{label:<40}{f'-${discount:,.2f}':>15}")
    print(f"{'GCT (15%)':<40}{f'${tax:,.2f}':>15}")
    print(f"{'TOTAL':<40}{f'${total:,.2f} JMD':>15}")
    print("=" * 55)
    
    
def cancel_order(order):
    """
    This function was designed to cancel an customer order completely
    """
    if order == {}:
        print("Your order is empty. Unable to cancel order.")
        return order

    confirmation = get_yes_no("Would you like to cancel the customer's order? (y/n): ")

    if confirmation:
        order.clear()
        print("Your order was successfully cancelled.")
    else:
        print("Order cancellation aborted.")

    return order


"""PART C"""


def load_menu(filename):
    try:
        #reading a file 
        with open (filename, "r") as f: 
            
            reader = DictReader(f)
            #empty menu dictionary to store menu items from the menu.csv files
            menu = {}
    
            #Iterating the the csv file 
            for row in reader:
                #print(row)
                code = row["code"]
                """
                creating an object to store the menu items from the csv file
                and using the strip () string method to remove trailling spaces
                
                """
                menu[code] = {
                    "name": row["name"],
                    "category": row["category"],
                    "price":float(row["price"])
                }
            #print("File opended sucessfully")  
            #once the menu is loaded the code stops exceuting
            return menu 
    #If menu does not exist python will raisE a FileNotFoundError    
    except FileNotFoundError:
        print("Warning: Menu file not found. Using default menu")
        #if the csv file menu fails to load we use the default get_menu function ()
        return get_menu()
    
menu = (load_menu("menu.csv"))
#print(menu)

def load_loyalty(filename):
    
    try:
        #reading file
        
        with open(filename, "r") as f:
            reader = DictReader(f)
            #empty dictionaty to store members
            member = {}
            #Iterating over csv file
        
            for row in reader:
                member_id = row["member_id"] 
                """
               Creating an object to store the loyalty members, along with their points 
               and using the strip () string method to remove any white trailing spaces.
                                
                """
                
                member[member_id] = {
                    "name": row["name"].strip(),
                    "points": int(float(row["points"].strip()))
                }
                
            return member
            
    except FileNotFoundError:
        print("Warning: Loyalty file not found. Starting with an empty member list! ")
        
        
def save_loyalty(filename, members):
    
    try: 
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer_obj = writer(f)
            #Write Column Headings
            writer_obj.writerow(["member_id", "name", "points"])
            #Iterate through member dictionary
            for member_id, details in members.items():
                writer_obj.writerow([
                    member_id,
                    details["name"],
                    details["points"]     
                ])
    except OSError as exc:
        print(f"Warning: Could not save loyalty file ({exc}).")
                

def register_member(members):
    name = input("Enter member name: ").strip()
    #checks if the name input is empty
    if name =="":
        print("Error: name cannot be empty.")
        return members   
    """
    Python starts with the number 1. It would create the the ID in the format M001.
    This then checks if the ID alreday exists in members. If it exist it increase the ID number. 
    """
    number = 1
    while f"M{number:03d}" in members:
        number += 1
    member_id = f"M{number:03d}"
    members[member_id] = {
        "name": name, 
        "points": 0}
    print(f"Registered {name} with member ID {member_id}.")
    return members


def award_points(members, member_id, amount_spent):
    #check if member id exists
    if member_id not in members:
        print(f"Error: member '{member_id}' not found.")
        #return 0 is we are unable to find customer id
        return 0
    #calculate points earned based on the amount that was spent
    earned = int(amount_spent // 100) * POINTS_PER_100
    members[member_id]["points"] += earned
    
    #returned the point that were earned
    return earned
    
    
def redeem_points(members, member_id, order):
    #check if member exists
    
    if member_id not in members:
        return False
    
    """
    check to see if a member has enough points; stops the execution of the 
    code once the points are less than the REDEEM_COST
    
    """
    if members[member_id]["points"]< REDEEM_COST:
        return False
    
    #Deduct the redemtion cost
    members[member_id]["points"] -= REDEEM_COST
    
    #Adding the free coffee to the order
    
    if FREE_COFFEE_CODE in order:
        order[FREE_COFFEE_CODE] +=1
    else:
        order[FREE_COFFEE_CODE] = 1
 
    #confirm sucessful 
    return True
 
 
def save_order(filename, order, totals):
    """
    Saves a completed customer order to a CSV file.
    """
    subtotal, discount, tax, total = totals

    try:
        # Check whether the file exists and is not empty
        file_exists = path.exists(filename) and path.getsize(filename) > 0

        # Open the file in append mode
        with open(filename, "a", newline="", encoding="utf-8") as f:
            obj_writer = writer(f)

            # Write column headers if the file is new or empty
            if not file_exists:
                obj_writer.writerow([
                    "datetime",
                    "items",
                    "subtotal",
                    "discount",
                    "tax",
                    "total"
                ])

            # Convert order dictionary into a string
            items_str = ";".join(
                f"{code}:{qty}" for code, qty in order.items()
            )

            # Write the order details to the CSV file
            obj_writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                items_str,
                f"{subtotal:.2f}",
                f"{discount:.2f}",
                f"{tax:.2f}",
                f"{total:.2f}"
            ])

    except OSError as exc:
        print(f"Warning: could not save order to '{filename}' ({exc}).")
     
def load_orders(filename):
    orders = []
    if not path.exists(filename):
        return orders
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            obj_reader = reader(f)
            for line_no, row in enumerate( obj_reader, start=1):
                if not row or row[0].strip() == "datetime":
                    continue
                try:
                    items = {}
                    if row[1].strip():
                        for part in row[1].split(";"):
                            code, qty = part.split(":")
                            items[code.strip()] = int(qty)
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

def generate_daily_report(orders):
    """
    Generates a daily sales report.
    """
    # Create a dictionary to store the report results
    report = {
        "order_count": len(orders),
        "total_revenue": 0.0,
        "total_tax": 0.0,
        "best_selling_item": "N/A",
    }
    # Dictionary to keep track of the total quantity sold for each item
    item_totals = {}
    for record in orders:
        report["total_revenue"] += record.get("total", 0.0)
        report["total_tax"] += record.get("tax", 0.0)
        for code, qty in record.get("items", {}).items():
            item_totals[code] = item_totals.get(code, 0) + qty
    if item_totals:
        report["best_selling_item"] = max(item_totals, key=item_totals.get)
    return report

def display_report(report, menu):
    print("\n" + "=" * 45)
    print("DAILY SALES REPORT".center(45))
    print("=" * 45)
    print(f"Number of orders : {report['order_count']}")
    print(f"Total revenue    : {MONEY_FORMAT.format(report['total_revenue'])}")
    print(f"Tax collected    : {MONEY_FORMAT.format(report['total_tax'])}")
    best = report["best_selling_item"]
    if menu and best in menu:
        best = f"{menu[best]['name']} ({best})"
    print(f"Best-selling item: {best}")
    print("=" * 45)

# Interactive helpers
def get_customer_type():
    print("Customer type: 1) Student  2) Staff  3) Regular")
    choice = get_menu_choice(1, 3)
    return {1: "student", 2: "staff", 3: "regular"}[choice]

def handle_add_item(order, menu):
    
    """
    This is an interactive helper function that allows us to add more than one item
    in an order. It also helps to keep the main () function cleaner and organized. 
    """
    
    #contines to execute the code once the condition is True
    while True:
        item_code = input("Enter item code ('done' to finish): ").strip().upper().replace(" ", "")
        #This stops the while loop
        if item_code == "DONE":
            break
        
        """
        Check to see if item code is not in the menu, if the code is invalid
        python displayy an error. The contiue execution send back to the begining of the while loop.
        """
        
        if item_code not in menu:
            print("Invalid item code. Please try again.")
            continue

        quantity = input("Enter quantity: ")
        #The add item function()
        add_item(order, menu, item_code, quantity)
    #returning the order back to where it was invoked
    return order



def handle_remove_item(order, menu):
    
    """
    This is an helper function that allows us to remove more than one item from
    the customer's order.
    """
    
    while True:
        item_code = input("Enter item code to remove ('done' to finish): ").strip().upper()
        #user would type DONE ton escape the loop
        if item_code == "DONE":
            break
        #remove item from the orders
        if item_code in menu:
            remove_item(order, item_code)
        else:
            #This is if the code is invalid
            print("Invalid item code. Please try again.")

    return order

def handle_update_quantity(order, menu):
    #Display the items that are currently in customers order
    view_order(order, menu)
    #stop is the customer has no items in their order
    if not order:
        return order
    #Ask the customer which order they would like to update
    code = get_valid_code("Enter item code to update: ", menu)

    return update_quantity(order, code)


def handle_checkout(order, menu, members):
    """
    This function handles the checkout
    """
    #checks whether the order is empty
    if not order:
        print("Cannot checkout: your order is empty.")
        return order

    customer_type = get_customer_type()
    #Assigned none because no loyalty members has been indentified
    member_id = None
    #check to see if the customer has loyalty points. It is false intially because the customer has not redeemed the point as yet
    redeemed = False

    if get_yes_no("Is the customer a loyalty member? (y/n): "):
        entered = input("Enter member ID: ").strip().upper()

        if entered in members:
            member_id = entered
        else:
            print(f"Member '{entered}' not found; treating as non-member.")

    if member_id and members[member_id]["points"] >= REDEEM_COST:
        prompt = (
            f"{members[member_id]['name']} has {members[member_id]['points']} points. "
            f"Redeem {REDEEM_COST} for a free Regular Coffee? (y/n): "
        )

        if get_yes_no(prompt):
            points_before = members[member_id]["points"]
            coffee_before = order.get(FREE_COFFEE_CODE, 0)

            if redeem_points(members, member_id, order):
                redeemed = True
                print("Free Regular Coffee added to the order.")

    totals = calculate_total(order, menu, customer_type)
    print_receipt(order, menu, totals, customer_type)

    if not get_yes_no("Confirm payment? (y/n): "):
        if redeemed:
            members[member_id]["points"] = points_before

            if coffee_before == 0:
                order.pop(FREE_COFFEE_CODE, None)
            else:
                order[FREE_COFFEE_CODE] = coffee_before

        print("Checkout cancelled. Your order is still open.")
        return order

    save_order(ORDERS_FILE, order, totals)

    if member_id:
        earned = award_points(members, member_id, totals[3])
        print(
            f"{earned} point(s) awarded to {members[member_id]['name']}. "
            f"New balance: {members[member_id]['points']}."
        )
        save_loyalty(LOYALTY_FILE, members)

    print("Payment complete. Thank you!")
    return {}


def handle_manager_options(menu, members):
    pin = input("Enter manager PIN: ").strip()
    #check to see if the pin is incorrect 
    if pin != MANAGER_PIN:
        print("Incorrect PIN. Access denied.")
        return members
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
            orders = load_orders(ORDERS_FILE)
            display_report(generate_daily_report(orders), menu)
        elif choice == 2:
            members = register_member(members)
            save_loyalty(LOYALTY_FILE, members)
        elif choice == 3:
            if not members:
                print("No loyalty members registered.")
            else:
                print("\nLOYALTY MEMBERS")
                print(f"{'ID':<8}{'Name':<24}{'Points':>8}")
                for mid, info in members.items():
                    print(f"{mid:<8}{info['name']:<24}{info['points']:>8}")


def main():
    order = {}
    menu = get_menu()
    members = load_loyalty(LOYALTY_FILE)
    while True:
        display_main_menu()
        menu_selection = get_menu_choice(0, 8)
        if menu_selection ==1:
            display_menu(menu)
        elif menu_selection ==2:
           handle_add_item(order, menu)             
        elif menu_selection ==3:
           handle_remove_item(order, menu)            
        elif menu_selection ==4:
             view_order(order,menu)       
        elif menu_selection ==5:
            handle_update_quantity(order, menu)
        elif menu_selection ==6:
           order = handle_checkout(order, menu, members)
        elif menu_selection == 7:
            cancel_order(order)
        elif menu_selection ==8:
            handle_manager_options(menu, members)
        elif menu_selection==0:
            print("Exiting System Goodbye :)")
            break
        else:
            print("Please enter a valid selection")   

if __name__ == "__main__":
    main()