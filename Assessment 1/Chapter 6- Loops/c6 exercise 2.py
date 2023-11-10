#using infinite loop to keep asking for age until the user decides to quit then print the ticket price
while True:

    age_input = input("Please enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        break

    age = int(age_input)

    if age < 3:
        ticket_cost = 0
    elif 3 <= age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15

    print(f"The cost of your movie ticket is ${ticket_cost}\n")