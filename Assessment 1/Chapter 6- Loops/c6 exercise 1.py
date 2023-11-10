#ask user to input a topping and list the toppings that was added by the user and print
pizza_toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping)