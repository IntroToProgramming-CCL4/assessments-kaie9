#make a list of sandwich orders, make an empty list, loop then print
sandwich_orders = ['turkey', 'ham and cheese', 'vegetarian', 'tuna']

finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first order from the list
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)