vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one)  # salida: [carro', 'bicicleta', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0]  # elimina 'carro'
print(vehicles_two)  # salida: ['bicicleta', 'motor']
