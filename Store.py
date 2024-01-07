class Store:
    def __init__(self):
        self.products = {'1': 10.00,'2': 20.00,'3': 30.00,'4': 15.00,}

    def display_menu(self):
        print("Welcome to the Store!")
        print("Product Code \n Product \n Price")
        for code, price in self.products.items():
            print(f"{code} \n\n Product-{code} \n ₹{price}")

    def generate_bill(self, quantities):
        total_amount = 0.0
        price = self.products.get(code, 0.0)
        total = price * quantity
        total_amount += total
        print("The total bill is ",total_amount)

store = Store()
store.display_menu()
quantities = {}
for code in store.products.keys():
    quantity = int(input(f"Enter the quantity of Product-{code}: "))
    quantities[code] = quantity
store.generate_bill(quantities)