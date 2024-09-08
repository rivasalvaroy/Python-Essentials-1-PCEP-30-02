pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
}

print(len(pol_esp_dictionary))  # salida: 3
del pol_esp_dictionary["zamek"]  # eliminar un elemento
print(len(pol_esp_dictionary))  # salida: 2

pol_esp_dictionary.clear()  # eliminar todos los elementos
print(len(pol_esp_dictionary))  # salida: 0

del pol_esp_dictionary  # elimina el diccionario
