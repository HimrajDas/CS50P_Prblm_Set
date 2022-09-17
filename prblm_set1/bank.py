def main():
    greeting = input("Greeting: ")
    greet(greeting)


def greet(greeting):
    price = 0
    if "hello" in greeting:
        price = 0
    elif greeting[0] == 'h':
        price += 20
    else:
        price += 100
    print(f"${price}")

main()