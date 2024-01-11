class IceCreamVendingMachine:
    def __init__(self):
        self.flavors = {
            'Vanilla': 2.00,
            'Chocolate': 2.50,
            'Rocky Road': 3.00,
            'Double Dutch': 3.50,
            'Butter Pecan' : 4.00,
        }

        self.flavor_descriptions = {
            'Vanilla': 'The classic vanilla flavor.',
            'Chocolate': 'Rich and indulgent chocolate flavor.',
            'Rocky Road': 'A mix of chocolate, marshmallows and nuts.',
            'Double Dutch': 'A combination of chocolate and vanilla with various swirls also with marshmallows and nuts.',
            'Butter Pecan' : 'Browned butter, toasted pecans, and a rich custard base.'
        }

        self.total_price = 0.0
        self.selected_flavor = None
        self.amount_paid = 0.0

    def display_menu(self):
        print("Welcome to the Ice Cream Vending Machine!")
        print("Available Flavors:")
        for flavor, price in self.flavors.items():
            print(f"{flavor}: ${price:.2f} - {self.flavor_descriptions[flavor]}")

    def select_flavor(self):
        flavor = input("Enter the flavor you want to buy: ")
        if flavor in self.flavors:
            price = self.flavors[flavor]
            self.total_price += price
            self.selected_flavor = flavor
            print(f"You selected {flavor}. Price: ${price:.2f}")
        else:
            print("Invalid flavor. Please select a valid flavor.")
            self.total_price = 0.0

    def make_payment(self):
        if self.total_price > 0:
            while True:
                try:
                    self.amount_paid = float(input("Enter the amount you want to pay: $"))
                    if self.amount_paid >= self.total_price:
                        break
                    else:
                        print("Insufficient payment. Please enter a sufficient amount.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            change = self.amount_paid - self.total_price
            print(f"Payment successful.")
            if change > 0:
                print(f"Change: ${change:.2f}")
        else:
            print("No valid flavor selected. Please select a valid flavor.")

    def display_receipt(self):
        print("\nReceipt:")
        if self.selected_flavor:
            print(f"Selected Flavor: {self.selected_flavor}")
            print(f"Description: {self.flavor_descriptions[self.selected_flavor]}")
            print(f"Total Price: ${self.total_price:.2f}")
            print(f"Amount Paid: ${self.amount_paid:.2f}")
            if self.amount_paid > self.total_price:
                print(f"Change: ${self.amount_paid - self.total_price:.2f}")
            print("Thank you for purchasing and enjoy!")
        else:
            print("No purchase made.")

    def start(self):
        self.display_menu()
        self.select_flavor()
        self.make_payment()
        self.display_receipt()


if __name__ == "__main__":
    vending_machine = IceCreamVendingMachine()
    vending_machine.start()




