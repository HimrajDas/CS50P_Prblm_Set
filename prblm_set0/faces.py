def main():
    greeting = input("Say: ")
    print(convert(greeting))


def convert(greet):
    if ":)" in greet:
        return f"{greet.replace(':)', '🙂')}"
    else:
        return f"{greet.replace(':(', '😓')}"


main()
