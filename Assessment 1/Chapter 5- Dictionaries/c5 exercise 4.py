# Create a dictionary of major rivers and their countries then print 
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

print("Sentences about each river:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

print("\nNames of rivers:")
for river in rivers.keys():
    print(river.title())

print("\nNames of countries:")
for country in rivers.values():
    print(country)