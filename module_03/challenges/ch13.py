text = """¡Estás atrapado en un bucle infinito!
Ingresa la palabra secreta para dejar el bucle: """

while True:
    word = input(text)
    if word == "chupacabra":
        break

print("¡Has dejado el bucle con éxito!")
