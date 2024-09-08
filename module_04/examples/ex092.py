my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)

empty_tuple = ()
print(type(empty_tuple))    # Salida: <class 'tuple'>

one_elem_tuple_1 = ("uno", )  # Paréntesis y una coma.
one_elem_tuple_2 = "uno",  # Sin paréntesis, solo la coma.

my_tuple_1 = 1,
print(type(my_tuple_1))  # salida: <class 'tuple'>

my_tuple_2 = 1  # Esto no es una tupla.
print(type(my_tuple_2))  # salida: <class 'int'>
