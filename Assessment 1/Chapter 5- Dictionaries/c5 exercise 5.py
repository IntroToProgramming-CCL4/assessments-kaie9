# Create dictionaries for different pets
pet1 = {'kind': 'dog', 'owner': 'Dhovie'}
pet2 = {'kind': 'cat', 'owner': 'Danish'}
pet3 = {'kind': 'parrot', 'owner': 'Janel'}
pet4 = {'kind': 'fish', 'owner': 'Vince'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print information about each pet
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"The {kind} is owned by {owner}.")