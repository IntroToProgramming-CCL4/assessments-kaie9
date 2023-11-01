#make a list of people to invite
invited = ["Dhovie", "Janel", "Danish"]

#define a function to send the invitations
def send_invitation(name):
    return f"Dear {name}, You are invited to dinner at my place. Please join me tonight!"
    
#print the name of the guest who cant go
guest_cant_go = "Danish"
print(f"{guest_cant_go} can't make it to the dinner.")

#replace the guest who can't go with a new person
new_invited = "Christian"
invited.remove(guest_cant_go)
invited.append(new_invited)

#print a second set of invitation messages
for person in invited:
    invitation = send_invitation(person)
    print(invitation)