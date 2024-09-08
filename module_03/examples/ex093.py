my_list = [1, 2, 3, 4, 5]

del my_list[0:2]
print(my_list)  # salida: [3, 4, 5]

del my_list[:]
print(my_list)  # delimina el contenido de la lista, genera: []
