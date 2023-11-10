#removed pastrami from sandwich orders, made other sandwiches, and listed finished sandwiches excluding pastrami.
sandwich_orders = ['turkey', 'pastrami', 'ham and cheese', 'vegetarian', 'pastrami', 'tuna', 'pastrami']

finished_sandwiches = []

print("Sorry, we've run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop(0)  
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)