# Implementación recursiva de la función factorial.
def factorial(n):
    if n == 1:  # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))  # 4 * 3 * 2 * 1 = 24
