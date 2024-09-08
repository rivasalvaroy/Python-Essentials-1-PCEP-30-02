the_mask = 8

flag_register = 0b00000000000000000000000000001000

if flag_register & the_mask:
    print("Mi bit se estableció en 1")
else:
    print("Mi bit se restableció a 0.")
