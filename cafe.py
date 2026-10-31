from gzip import READ
from operator import add


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
    return {
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
READ
add
    
#Calling / invoking the get men function
menu = get_menu() 

#creating the function defintion for the display menu(); This is responsible for showing the menu items
def display_menu(menu):
    #creating and formatting the Menu title
    print("-" * 80)
    #centering the starter menu ins the terminal
    print("STARTER MENU".center(80))
    print("-" * 80)
    
    #adding a new line for display purposes 
    print("\n")
    #adding the category title
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
    
    for itemcode, details in menu.items():
        if details["category"] == "Cold Drinks":
            print(f"{itemcode:<20} {details['name']:<30} {details['category']:<20} ${details['price']:<20.2f}")

    print("\n")
    print("\nFOOD\n")
    print(f"{'Item Code':<20}{'Item Name':<30}{'Category':<20}{'Price(JMD)':<10}")
    print("-" * 80)
    for itemcode, details in menu.items():
        if details["category"] == "Food":
            print(f"{itemcode:<20} {details['name']:<30} {details['category']:<20} ${details['price']:<20.2f}\n")
 
#Invoking the display menu function
display_menu(menu)


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
            print("Invalid input! Please enter a numeric option")
           
           
def add_item(order,menu, item_code, quantity=1):
    
    '''
    Add an item to the customer's existing order
    '''
    try:
        
        quantity = int(quantity)
        
        if quantity<=0:
            print("Quantity must be greater than zero")
        
        if item_code in menu:
            if item_code in order:
                order[item_code] +=quantity
            else:
                order[item_code]= quantity
        
            print("Item added sucessfully!")
        else:
            print("Inavlid item code")
    
    except ValueError:
        print("Invalid quantity. please enter a whole number")
            

def remove_item(order, code):
    #check to see is empty
    if order == {}:print("Your order is empty")
    #check the code that is in the order the; the in key word return a true or false value. It is is true the code block is exceuted
    if code in order:
        #removing item form the user order by using the pop () method
        order.pop(code)
        print("Item removed sucessfully!")
    else:
        #if the custome order is empty
        print("Item is not in your order.")
    
    
def view_item(order, menu):
    print("needt to be worked on")
    
def main():
    print("Print needs to be worked on")

def calculate_subtotal(order, menu):
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

