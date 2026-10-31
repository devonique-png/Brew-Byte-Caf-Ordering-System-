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
    Return the default menu as a dictionary keyed by item code.

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
 
#Invoking the display menu dunction
display_menu(menu)


def display_main_menu():
    print("\n")
    print("-" * 80)
    print("WELCOME TO BREW & BYTE CAFE".center(80))
    print("=" * 80)
    print("1.View Menu\n2.Add Item\n3.Remove Item\n4.View Current Order\n5.Exit")
    
    
    
display_main_menu()