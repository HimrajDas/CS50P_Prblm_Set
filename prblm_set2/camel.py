def main():
    camel_case = input("camelCase: ").strip()
    print(camel_to_snake(camel_case))


def camel_to_snake(camel_str):
    for i in camel_str:
        if i.isupper():
            new_letter = i.lower()
            snake_str = camel_str.replace(i, f"_{new_letter}")
            return f"snake_case: {snake_str}"
    return f"snake_case: {camel_str}"


main()
