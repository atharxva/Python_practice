import time
import datetime
import random

class Electronics_:
    def __init__(self, name, menu, special_offers=None):
        self.name = name
        self.menu = menu
        self.special_offers = special_offers or {}
        self.user = None
        
    def create_account(self):
        print("\nCreate Your Account:")
        name = input("Enter your name: ")
        acc_number = input("Enter your account number: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return {"name": name, "acc_number": acc_number, "username": username, "password": password}

    def welcome_user(self):
        current_time = datetime.datetime.now().time()
        greeting = "\033[92mGood morning\033[0m"
        if current_time >= datetime.time(12, 0) and current_time < datetime.time(17, 0):
            greeting = "\033[93mGood afternoon\033[0m"
        elif current_time >= datetime.time(17, 0):
            greeting = "\033[91mGood evening\033[0m"

        print(f"{greeting}, {self.user['name']}! Welcome to {self.name}.")

    def display_menu(self):
        print(f"\n{self.name} Products:")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        
        if self.special_offers:
            print("\nSpecial Offers:")
            for offer, discount in self.special_offers.items():
                print(f"{offer}: {discount}% off")

    def take_order(self):
        order = {}
        while True:
            item = input("Enter the Product you want to order (or type 'done' to finish): ")
            if item.lower() == 'done':
                break
            elif item in self.menu:
                quantity = int(input(f"How many {item}s do you want? "))
                order[item] = quantity
            else:
                print("Invalid item. Please choose from the menu.")
        return order

    def calculate_total(self, order):
        total = sum(self.menu[item] * quantity for item, quantity in order.items())
        return total

    def generate_bill(self, order, total):
        print("\nCalculating your bill...", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end='', flush=True)
        print("\n\033[94mOrder Summary:\033[0m")
        for item, quantity in order.items():
            print(f"{item}: {quantity} x ₹{self.menu[item]} = ₹{quantity * self.menu[item]}")
        print(f"\033[94mTotal: ₹{total}\033[0m")
        print("\033[92mThank you for ordering with us!\033[0m")

    def feedback(self):
        feedback_responses = [
            "Thank you for your feedback! You rated us {rating} stars.",
            "We appreciate your input! Your rating: {rating} stars.",
            "Your feedback is important to us. You gave us {rating} stars. Thank you!",
        ]

        rating = input("Please rate your experience (1 to 5 stars): ")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            response = random.choice(feedback_responses).format(rating=rating)
            print(response)
        else:
            print("Invalid rating. Feedback not submitted.")

def main():
    # Define menus for Laptops and Smaptphones
    Laptops = {"Asus Rog gaming ": 100000, "Hp omen 16 ": 152000, "Asus ROG zephyrus": 78000, "MSI Katana ": 90000,
                        "Alienware F17👽": 300000, "RAZER Blade 15": 250000, "Acer Nitro 5": 580000,
                        "ROG Strix Gaming": 700000, "Dell G15 Gaming": 200000, "Macbook Air M2": 119000, "MAcbook pro M3 max": 250000}
    
    Smartphones = {"Oneplus 10 pro": 70000, "Iphone 14": 58000, "Oneplus 6T": 42000, "Mi mix 3": 88000,
                "Redmi note 12 pro": 30000, "GOOGLE pixel 8 pro": 98000, "Samsung S23 Ultra": 150000, "Iphone 15 plus":90000, "Huawei mate 6": 100000}

    # Example of special offers
    Lapptops_special_offers = {"Christmas Discount": 15, "Student Discount": 10}
    Smartphones_offers = {"Big billion days": 20, "Happy Hour": 15}

    # Create instances of Electronics_
    Laptops_ = Electronics_("Laptops", Laptops, Lapptops_special_offers)
    Smaptphones = Electronics_("Smaptphones", Smartphones, Smartphones_offers)

    # Create user account
    user_account = Laptops_.create_account()

    # Set user account in the Electronics_ instances
    Laptops_.user = user_account
    Smaptphones.user = user_account

    # Display the user's information
    print("\nUser Information:")
    print(f"Name: {user_account['name']}")
    print(f"Account Number: {user_account['acc_number']}")
    print(f"Username: {user_account['username']}")

    # Offer a choice for ordering
    print("\nSelect a food outlet to order from:")
    print("1. Laptops")
    print("2. Smartphones")

    outlet_choice = input("Enter the product you want to buy outlet: ")

    if outlet_choice == "1":
        Croma = Laptops_
    elif outlet_choice == "2":
        Croma = Smaptphones
    else:
        print("Invalid choice. Exiting.")
        return

    # Welcome user to the selected food outlet
    Croma.welcome_user()

    # Display menu and take orders
    Croma.display_menu()
    order = Croma.take_order()

    # Introduce a fun loading animation
    time.sleep(1)
    print("\nGenerating your bill", end='', flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)

    total = Croma.calculate_total(order)
    Croma.generate_bill(order, total)

    # Ask for feedback
    time.sleep(1)  # Add a delay for a better user experience
    Croma.feedback()

if __name__ == "__main__":
    main()