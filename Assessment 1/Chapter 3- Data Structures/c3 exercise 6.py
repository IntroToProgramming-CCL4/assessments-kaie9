#create a program from chapter 3-5 that invites only 2 people from your list,remove guests using pop(), print a message for the 2 remaining people and using del remove the 2 people from the list making it blank
invited = ["Dhovie", "Janel", "Danish"]

def send_invitation(name):
    return f"Dear {name}, You are invited to dinner at my place. Please join me tonight!"

print("I can invite only two people.")

while len(invited) > 2:
    removed_guest = invited.pop()
    print(f"Sorry, {removed_guest}, I cant invite you to dinner.")

for person in invited:
    invitation = send_invitation(person)
    print(invitation)

del invited[0]  
del invited[0]  

print("Remaining invited guests:", invited)