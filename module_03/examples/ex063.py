my_list = [1, None, True, 'Soy una cadena', 256, 0]

print(my_list[3])  # salida: Soy una cadena
print(my_list[-1])  # salida: 0

my_list[1] = '?'
# salida: [1, '?', True, 'Soy una cadena', 256, 0]
print(my_list)

my_list.insert(0, "primero")
my_list.append("último")
# outputs: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']
print(my_list)
