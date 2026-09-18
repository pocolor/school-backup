confirm = ""
while confirm not in ("y", "yes", "ano", "a", "1"):
    name = input("Ahoj, jak se jmenuješ?\n")
    confirm = input(f"Opravdu se jmenuješ: {name}?\n").lower()
