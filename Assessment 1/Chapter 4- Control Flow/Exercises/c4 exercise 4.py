#set a value for the variable age then if-elif-else chain to determine the person's stage in life
age = 25

if age < 2:
    print("baby.")
elif age < 4:
    print("toddler.")
elif age < 13:
    print("kid.")
elif age < 20:
    print("young adult.")
elif age < 65:
    print("adult.")
else:
    print("elder.")
