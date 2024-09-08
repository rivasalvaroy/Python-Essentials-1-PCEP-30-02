# continue - ejemplo
print("\nLa instrucción continue:")

for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)

print("Fuera del bucle.")
