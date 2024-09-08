pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
}

item_1 = pol_esp_dictionary["gleba"]    # Ejemplo 1.
print(item_1)   # Salida: tierra

item_2 = pol_esp_dictionary.get("woda")  # Ejemplo 2.
print(item_2)   # Salida: agua
