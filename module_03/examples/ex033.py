text = "OpenEDG Python Institute"

for letter in text:
    if letter == "P":
        break
    print(letter, end="")

print("\n")

text = "pyxpyxpyx"

for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
