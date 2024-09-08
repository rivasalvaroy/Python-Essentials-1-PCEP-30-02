the_mask = 0b00000000000000000000000000001000

flag_register = 0b00000000000000000000000000001000
print(bin(flag_register & the_mask))

flag_register = 0b00000000000000000000000000000000
print(bin(flag_register & the_mask))
