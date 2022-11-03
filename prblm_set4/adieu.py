import inflect

p = inflect.engine()


name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        name = p.join(name_list)
        print(f"Adieu, adieu, to {name}")
        exit()
