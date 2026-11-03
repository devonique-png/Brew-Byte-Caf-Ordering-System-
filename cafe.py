import csv
import os
from datetime import datetime

GCT_RATE = 0.15
STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05
BULK_DISCOUNT_THRESHOLD = 2500.00
BULK_DISCOUNT_AMOUNT = 200.00
POINTS_PER_100 = 1
REDEEM_COST = 50
FREE_COFFEE_CODE = "C01"          # Regular Coffee in your menu
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

def display_menu(menu):
    print("-" * 80)
    print("STARTER MENU".center(80))
    print("-" * 80)
    print("\n")
    print("\nHOT DRINKS\n".center(100))
    print(f"{'Item Code':<20}{'Item Name':<30}{'Category':<20}{'Price(JMD)':<10}")
    print("-" * 80)
    
    for itemcode, details in menu.items():
        if details["category"] == "Hot Drinks":
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

def display_main_menu():
    print("\n")
    print("-" * 80)
    print("WELCOME TO BREW & BYTE CAFE".center(80))
    print("Campus Ordering System".center(80))
    print("=" * 80)
    print("\n")
    print("""1.View Menu
2.Add Item to Order
3.Remove Item from Order
4.View Current Order
5.Update Item Quantity
6.Checkout
7.Cancel Order
8.Manager Options
9.Exit
          """)
    print("-" * 80)

def get_menu_choice(min_option, max_option):
    while True:
        try:
            menu_action = int(input("Enter your choice:  "))
            if menu_action >= min_option and menu_action <= max_option:
                return menu_action
            else: 
                print(f"Invalid Selection, Please enter a value between {min_option} and {max_option}")
        except ValueError:
            print("Invalid input! Please enter a numeric option.")

def add_item(order, menu, item_code, quantity=1):
    item_code = item_code.upper()
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be greater than zero")
            return order
        if item_code in menu:
            if item_code in order:
                order[item_code] += quantity
            else:
                order[item_code] = quantity
            print("Item added successfully!")
        else:
            print("Invalid item code")
    except ValueError:
        print("Invalid quantity. Please enter a whole number")
    return order

def remove_item(order, code):
    code = code.upper()
    if order == {}:
        print("Your order is empty")
        return False
    if code in order:
        order.pop(code)
        print("Item removed successfully!")
        return True
    else:
        print("Item is not in your order.")
        return False

def view_item(order, menu):
    if order == {}:
        print("Your order is empty")
        return 
    print("\n")
    print("YOUR CURRENT ORDER".center(80))
    print("\n")
    print(f"{'Item':<25}{'Quantity':<15}{'Unit Price':<15}{'Line Total(JMD)':<20}")
    print("=" * 80)
    for item_code, quantity in order.items():
        print(f"{menu[item_code]['name']:<25} {quantity:<15}{menu[item_code]['price']:<15.2f}${quantity * menu[item_code]['price']:<15.2f}")
        print("_" * 80)

def update_quantity(order, item_code):
    item_code = item_code.upper()
    if order == {}:
        print("Your Order is empty")
        return order
    if item_code in order:
        try:
            new_quantity = input("Enter new quantity: ")
            new_quantity = int(new_quantity)
            if new_quantity > 0:
                order[item_code] = new_quantity
                print("Quantity Updated")
            else:
                print("Quantity must be greater than zero")
        except ValueError:
            print("Please Enter a valid whole number.")     
    else:
        print("Item not found in your order")
    return order

# PART B: Billing, Discounts and Validation
def calculate_subtotal(order, menu):
    if order == {}:
        print("Order is empty")
        return 0
    subtotal = 0
    for item_code, quantity in order.items():
        unit_price = menu[item_code]["price"]
        line_total = quantity * unit_price
        subtotal += line_total
    return subtotal
  
def calculate_discount(subtotal, customer_type):
    discount = 0.0
    if customer_type == "student":
        discount += subtotal * STUDENT_DISCOUNT
    elif customer_type == "staff":
        discount += subtotal * STAFF_DISCOUNT
    if subtotal >= BULK_DISCOUNT_THRESHOLD:
        discount += BULK_DISCOUNT_AMOUNT
    return discount

def calculate_tax(amount, rate=GCT_RATE):
    return amount * rate

def calculate_total(order, menu, customer_type):
    subtotal = calculate_subtotal(order, menu)
    discount = calculate_discount(subtotal, customer_type)
    taxable = subtotal - discount
    tax = calculate_tax(taxable)
    total = taxable + tax
    return subtotal, discount, tax, total

def get_valid_quantity(prompt):
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
    while True:
        code = input(prompt).strip().upper()
        if code in menu:
            return code
        print(f"Invalid code '{code}'. Please enter a code from the menu.")

def get_yes_no(prompt):
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")

def print_receipt(order, menu, totals, customer_type):
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

# PART C: Loyalty, Reports and File Handling
def load_menu(filename):
    if not os.path.exists(filename):
        print(f"Warning: menu file '{filename}' not found. Using default menu.")
        return get_menu()
    menu = {}
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line_no, row in enumerate(reader, start=2):
                try:
                    code = row["code"].strip().upper()
                    menu[code] = {
                        "name": row["name"].strip(),
                        "category": row["category"].strip(),
                        "price": float(row["price"])
                    }
                except (KeyError, ValueError, AttributeError):
                    print(f"Warning: skipping badly formatted line {line_no} in '{filename}'.")
    except OSError as exc:
        print(f"Warning: could not read '{filename}' ({exc}). Using default menu.")
        return get_menu()
    if not menu:
        print(f"Warning: menu file '{filename}' was empty. Using default menu.")
        return get_menu()
    return menu

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

def save_loyalty(filename, members):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for member_id, info in members.items():
                writer.writerow([member_id, info["name"], info["points"]])
    except OSError as exc:
        print(f"Warning: could not save loyalty file '{filename}' ({exc}).")

def register_member(members):
    name = input("Enter member name: ").strip()
    if not name:
        print("Error: name cannot be empty.")
        return members
    number = 1
    while f"M{number:03d}" in members:
        number += 1
    member_id = f"M{number:03d}"
    members[member_id] = {"name": name, "points": 0}
    print(f"Registered {name} with member ID {member_id}.")
    return members

def award_points(members, member_id, amount_spent):
    member_id = member_id.upper()
    if member_id not in members:
        print(f"Error: member '{member_id}' not found.")
        return 0
    earned = int(amount_spent // 100) * POINTS_PER_100
    members[member_id]["points"] += earned
    return earned

def redeem_points(members, member_id, order):
    member_id = member_id.upper()
    if member_id not in members:
        return False
    if members[member_id]["points"] < REDEEM_COST:
        return False
    members[member_id]["points"] -= REDEEM_COST
    order[FREE_COFFEE_CODE] = order.get(FREE_COFFEE_CODE, 0) + 1
    return True

def save_order(filename, order, totals):
    subtotal, discount, tax, total = totals
    try:
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["datetime", "items", "subtotal", "discount", "tax", "total"])
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

def load_orders(filename):
    orders = []
    if not os.path.exists(filename):
        return orders
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for line_no, row in enumerate(reader, start=1):
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
    report = {
        "order_count": len(orders),
        "total_revenue": 0.0,
        "total_tax": 0.0,
        "best_selling_item": "N/A",
    }
    item_totals = {}
    for record in orders:
        report["total_revenue"] += record.get("total", 0.0)
        report["total_tax"] += record.get("tax", 0.0)
        for code, qty in record.get("items", {}).items():
            item_totals[code] = item_totals.get(code, 0) + qty
    if item_totals:
        report["best_selling_item"] = max(item_totals, key=item_totals.get)
    return report

def display_report(report, menu=None):
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
    item_code = get_valid_code("Enter item code: ", menu)
    quantity = get_valid_quantity(f"Enter quantity ({MIN_QUANTITY}-{MAX_QUANTITY}): ")
    return add_item(order, menu, item_code, quantity)

def handle_remove_item(order, menu):
    if not order:
        print("Your order is empty; nothing to remove.")
        return order
    code = get_valid_code("Enter item code to remove: ", menu)
    remove_item(order, code)
    return order

def handle_update_quantity(order, menu):
    if not order:
        print("Your order is empty; nothing to update.")
        return order
    view_item(order, menu)
    code = get_valid_code("Enter item code to update: ", menu)
    return update_quantity(order, code)

def handle_checkout(order, menu, members):
    if not order:
        print("Cannot checkout: your order is empty.")
        return order
    customer_type = get_customer_type()
    member_id = None
    if get_yes_no("Is the customer a loyalty member? (y/n): "):
        entered = input("Enter member ID: ").strip().upper()
        if entered in members:
            member_id = entered
        else:
            print(f"Member '{entered}' not found; treating as non-member.")
    if member_id and members[member_id]["points"] >= REDEEM_COST:
        prompt = (f"{members[member_id]['name']} has {members[member_id]['points']} points. "
                  f"Redeem {REDEEM_COST} for a free Regular Coffee? (y/n): ")
        if get_yes_no(prompt):
            if redeem_points(members, member_id, order):
                print("Free Regular Coffee added to the order.")
    totals = calculate_total(order, menu, customer_type)
    print_receipt(order, menu, totals, customer_type)
    if not get_yes_no("Confirm payment? (y/n): "):
        print("Checkout cancelled. Your order is still open.")
        return order
    save_order(ORDERS_FILE, order, totals)
    if member_id:
        earned = award_points(members, member_id, totals[3])
        print(f"{earned} point(s) awarded to {members[member_id]['name']}. "
              f"New balance: {members[member_id]['points']}.")
        save_loyalty(LOYALTY_FILE, members)
    print("Payment complete. Thank you!")
    return {}

def handle_manager_options(menu, members):
    pin = input("Enter manager PIN: ").strip()
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

# ==========================================
# THIS IS THE PART THAT "CALLS" THE FUNCTIONS
# ==========================================
def main():
    menu = load_menu(MENU_FILE)
    members = load_loyalty(LOYALTY_FILE)
    order = {}

    while True:
        display_main_menu()
        menu_selection = get_menu_choice(1, 9)

        if menu_selection == 1:
            display_menu(menu)
        elif menu_selection == 2:
            order = handle_add_item(order, menu)
        elif menu_selection == 3:
            order = handle_remove_item(order, menu)
        elif menu_selection == 4:
            view_item(order, menu)
        elif menu_selection == 5:
            order = handle_update_quantity(order, menu)
        elif menu_selection == 6:
            order = handle_checkout(order, menu, members)
        elif menu_selection == 7:
            if order:
                if get_yes_no("Cancel the entire order? (y/n): "):
                    order = {}
                    print("Order cancelled.")
            else:
                print("There is no order to cancel.")
        elif menu_selection == 8:
            members = handle_manager_options(menu, members)
        elif menu_selection == 9:
            print("Exiting System Goodbye :)")
            break

if __name__ == "__main__":
    main()