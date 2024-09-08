def hi(name):
    print("Hola,", name)


hi("Greg")


def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)


hi_all("Sebastián", "Konrad")


def address(street, city, postal_code):
    print("Tu dirección es:", street, city, postal_code)


s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")

address(s, c, p_c)
