pol_esp_dictionary = {"kwiat": "flor"}
pol_esp_dictionary.update({"gleba": "tierra"})

print(pol_esp_dictionary)   # salida: {'kwiat': 'flor', 'gleba': 'tierra'}

pol_esp_dictionary.popitem()
print(pol_esp_dictionary)   # salida: {'kwiat': 'flor'}
