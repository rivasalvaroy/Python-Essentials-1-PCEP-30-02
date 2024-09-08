def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    elif a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    elif b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    else:
        return False


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(5, 4, 3))
print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(3, 5, 4))
print(is_a_right_triangle(4, 3, 5))
print(is_a_right_triangle(4, 5, 3))

print(is_a_right_triangle(1, 3, 4))
print(is_a_right_triangle(2, 1, 2))
