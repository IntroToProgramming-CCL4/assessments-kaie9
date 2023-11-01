#make a list of people to invite
invited = ["Dhovie", "Janel", "Danish"]

#define a function to send the invitations
def send_invitation(name):
    return f"Dear {name}, You are invited to dinner at my place. Please join me tonight!"

#loop through the list and print
for person in invited:
    invitation = send_invitation(person)
    print(invitation)