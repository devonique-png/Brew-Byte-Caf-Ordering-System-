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
        "B01": {"name": "Espresso", "category": "Beverages", "price": 300.00},
        "B02": {"name": "Cappuccino", "category": "Beverages", "price": 550.00},
        "B03": {"name": "Iced Latte", "category": "Beverages", "price": 600.00},
        "B04": {"name": "Regular Coffee", "category": "Beverages", "price": 400.00},
        "F01": {"name": "Beef Patty", "category": "Food", "price": 400.00},
        "F02": {"name": "Chicken Patty", "category": "Food", "price": 450.00},
        "F03": {"name": "Cheese Sandwich", "category": "Food", "price": 700.00},
        "S01": {"name": "Croissant", "category": "Snacks", "price": 350.00},
        "S02": {"name": "Chocolate Muffin", "category": "Snacks", "price": 300.00},
    }
add
    