a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)
