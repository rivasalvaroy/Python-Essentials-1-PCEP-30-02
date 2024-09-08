# Ejemplo 1
squares = [x ** 2 for x in range(10)]

# Ejemplo 2
twos = [2 ** i for i in range(8)]

# Ejemplo 3
odds = [x for x in squares if x % 2 != 0]


print(squares)
print(twos)
print(odds)
