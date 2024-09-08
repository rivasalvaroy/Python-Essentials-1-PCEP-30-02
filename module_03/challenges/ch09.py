x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int(x) > 1:
        print("dos")
    elif int(x) < 1:
        print("tres")
    else:
        print("cuatro")

if int(x) == 1:
    print("cinco")
else:
    print("seis")
