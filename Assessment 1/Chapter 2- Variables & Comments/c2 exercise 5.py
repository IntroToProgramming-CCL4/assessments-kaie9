#define the budget and the price of the usb sticks
budget = 50
usb_stick_price = 6

#calculate the number of usb she can buy
num_usb_sticks = budget // usb_stick_price

#calculate how many money she will have left
leftover_pounds = budget % usb_stick_price

#print the result
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have {leftover_pounds} pounds left.")