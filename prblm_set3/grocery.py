items = []

while True:
    try:
        product = input("").lower()
        items.append(product)
    except EOFError:
        for index, item in enumerate(set(items)):
            print(f"{index + 1} {item.upper()}")
        exit()
