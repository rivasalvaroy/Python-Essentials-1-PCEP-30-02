def name(first_name, last_name="Pérez"):
    print(first_name, last_name)


name("Andy")    # salida: Andy Pérez
# salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")
name("Bety", "Rodríguez")
