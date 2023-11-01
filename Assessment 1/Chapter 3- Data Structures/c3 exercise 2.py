#create a list of your friends names
names = ["Dhovie", "Janel", "Danish"]

#define the message
message = "Hello, {}! I hope you are fine today."

#print 
for name in names:
    personalized_message = message.format(name)
    print(personalized_message)
    