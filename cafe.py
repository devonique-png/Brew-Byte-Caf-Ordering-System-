from gzip import READ
from operator import add
import csv


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


"""PART C"""
def load_menu(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            menu={}
            
            for row in reader:
                code = row["code"]
                
                menu[code] = {
                    "name":row["name"],
                    "category": row["category"],
                    "price":row["price"]     
                }
            return menu
    except FileNotFoundError:
        ("Menu File was not found")