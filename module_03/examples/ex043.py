the_mask = 0b00000000000000000000000000001000

flag_register = 0b00000000000000000000000000001000
flag_register ^= the_mask
print(bin(flag_register))

flag_register = 0b00000000000000000000000000000000
flag_register ^= the_mask
print(bin(flag_register))
